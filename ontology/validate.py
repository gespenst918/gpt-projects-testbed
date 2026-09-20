"""Validate the Tier 1 vocabulary and cross-file contracts (Python standard library)."""
import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate():
    # Explicit checks mirror the published glossary schema, plus graph constraints.
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    sources = read("sources.json")["sources"]
    source_ids = {s["id"] for s in sources}
    require(len(source_ids) == len(sources), "Duplicate source ID")
    terms = {}
    groups = {
        "core/factory.json": ("universal", "factory."),
        "core/runtime.json": ("universal", "runtime."),
        "domains/machinery.json": ("domain", "machinery."),
        "domains/mobile-robot.json": ("domain", "mobile."),
        "safety/concepts.json": ("safety", "safety."),
    }
    keys = {"id", "label", "definition", "tier", "status", "sources", "related", "note"}
    for path, (layer, prefix) in groups.items():
        doc = read(path)
        require(set(doc) == {"version", "layer", "terms"}, f"{path}: document fields")
        require(doc["version"] == "0.1.0" and doc["layer"] == layer, f"{path}: layer/version")
        require(isinstance(doc["terms"], list) and doc["terms"], f"{path}: empty glossary")
        for term in doc["terms"]:
            require(set(term) == keys, f"{path}: term fields")
            ident = term["id"]
            require(isinstance(ident, str) and re.fullmatch(r"(factory|runtime|machinery|mobile|safety)\.[a-z][a-z0-9-]*", ident), "Invalid ID")
            require(ident.startswith(prefix) and ident not in terms, f"{ident}: prefix/duplicate")
            for key in ("label", "definition", "note"):
                require(isinstance(term[key], str), f"{ident}: {key} type")
            require(term["label"] and term["definition"], f"{ident}: empty text")
            require(type(term["tier"]) is int and term["tier"] == 1 and term["status"] == "draft", f"{ident}: tier/status")
            for key in ("sources", "related"):
                require(isinstance(term[key], list) and all(isinstance(v, str) for v in term[key]), f"{ident}: {key}")
                require(len(term[key]) == len(set(term[key])), f"{ident}: repeated {key}")
            require(term["sources"] and set(term["sources"]) <= source_ids, f"{ident}: sources")
            terms[ident] = term
    for ident, term in terms.items():
        require(set(term["related"]) <= terms.keys(), f"{ident}: dangling relationship")
        if ident.startswith(("factory.", "runtime.")):
            require(all(t.startswith(("factory.", "runtime.")) for t in term["related"]), f"{ident}: core depends on domain")
    hierarchy = read("core/hierarchy.json")
    path = hierarchy["equipment_role_path"]
    require(len(path) == len(set(path)) and set(path) <= terms.keys(), "Hierarchy cycle/reference")
    require([v["level"] for v in hierarchy["functional_levels"]] == list(range(5)), "Functional levels")
    for relation in hierarchy["relationships"]:
        require(relation["from"] in terms and relation["to"] in terms, "Relationship endpoint")
    for path in (ROOT / "mappings/protocols").glob("*.json"):
        doc = json.loads(path.read_text())
        require(set(doc["sources"]) <= source_ids, "Mapping sources")
        for entry in doc["entries"]:
            require(entry["target"] in terms, "Mapping target")
            require(entry["strategy"] in {"preserve", "generalize", "adapter-only"}, "Mapping strategy")
            require(entry["source"] and entry["transform"], "Missing mapping rule")
    sample = read("examples/observation.json")
    require(sample["example_only"] is True and sample["term_id"] in terms, "Example term")
    mapping = read(sample["mapping"])
    require(sample["mapping_version"] == mapping["version"], "Example mapping version")
    require(any(e["source"] == sample["source"]["field"] and e["target"] == sample["term_id"] for e in mapping["entries"]), "Example mapping mismatch")
    require(sample["quality"] in {"good", "uncertain", "bad", "unknown"}, "Quality")
    require(sample["freshness"] in {"fresh", "stale", "unknown"}, "Freshness")
    require(sample["support"] in {"supported", "unsupported", "unknown"}, "Support")
    require(datetime.fromisoformat(sample["observed_at"]) <= datetime.fromisoformat(sample["received_at"]), "Example timing")
    require(sample["control_authority"] == "none", "Safety observation authority")
    require(read("safety/boundaries.json")["normative"] is False, "Safety boundary")
    return len(terms)

if __name__ == "__main__":
    print(f"PASS: {validate()} terms; sources, hierarchy, mappings and example validated.")
