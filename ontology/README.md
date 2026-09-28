# Leiomano Tier 1 semantic baseline

Version 0.1.0 · draft · 2026-09-21

This is the first machine-readable vocabulary for the [automation architecture](../docs/architecture/automation-runtime.md). It is a semantic design baseline, not an executable gateway or a standards-conformance claim.

## Directory
- `core/`: universal factory roles, resources, hierarchy and runtime concepts.
- `domains/`: machinery and mobile-robot specializations.
- `safety/`: safety vocabulary and authority boundaries.
- `mappings/protocols/`: versioned external-model crosswalks.
- `mappings/vendors/`, `mappings/projects/`: supplier and site interpretation.
- `schemas/`: glossary contract; `examples/`: synthetic observations.
- `sources.json`: provenance, edition and evidence limitations.

Equipment role hierarchy: Enterprise → Site → Area → Work center → Work unit. Physical assets are assigned to roles; location is a separate relation. Functional levels 0–4 are a different axis, not one layer per directory.

## Contract and usage
Stable IDs use `factory.`, `runtime.`, `machinery.`, `mobile.` and `safety.` prefixes. English labels are display text, never identity. Every term has a definition, tier, draft status, source IDs, related IDs and a scope note. Definitions are concise Leiomano paraphrases, not copied normative terminology.

Load glossary files, resolve source/related IDs, then apply a versioned mapping. Preserve raw source values, timestamps, quality, units and mapping identity. Unsupported, unknown and stale are distinct. A missing boolean must not become false. State, mode, connectivity and safety are independent dimensions.

Mappings classify preservation, generalization or adapter-only retention. VDA order identity is not a universal task ID. OPC UA mode describes activity intent and cannot simply replace a mobile robot's control mode. Operational zones do not establish safety protection.

## Evidence and limits
The [source registry](sources.json) pins VDA 5050 3.0.0 and Machinery 1.04.1. ISA-95 concepts use public ISA/OPC material; no complete licensed edition was reviewed. ISO 3691-4:2023 supplies the driverless-truck scope; the remaining safety terms are provisional Leiomano vocabulary pending licensed-clause review. No clause-level safety requirements, PL values or certification are asserted.

Run `python3 ontology/validate.py` from the repository root. This checks vocabulary structure, references, layer separation, mappings and the synthetic observation. It does not test protocol conformance or equipment safety.

## Extension policy
Add domain details without importing protocol fields into universal definitions. Record exact source editions and mapping assumptions. Change meaning with a new ID or major version; add aliases without changing identity. Review safety terms with the responsible engineer before operational use. Next: select a pilot workflow, supplier interface and licensed standards corpus, then define executable asset/event schemas and adapter acceptance tests.

## Operational Value Model
The [Operational Value Model](core/operational-value.json) adds activity classifications and operational objectives in the existing `factory.` namespace. Its relationships, assessment fields and ordered improvement policy extend [the existing hierarchy](core/hierarchy.json). It creates no second equipment tree or software stack.

Classify a scoped `factory.process-segment` as ValueCreating, NecessaryNonValueAdding or AvoidableWaste. Record the rationale and current constraints; split mixed activities and leave unassessed work unclassified. A runtime task realizes a process segment, and operations performance evaluates its objectives. The seven objective types specialize `factory.operational-objective`; existing task outcomes and lifecycles remain intact.

Material handling generally adds no customer value directly, but some transport sustains value creation. Eliminate unnecessary movement, minimize necessary movement, then automate the irreducible remainder where practical. Automation alone never changes its classification to ValueCreating. JIT and Kanban coordinate readiness and replenishment; they do not themselves remove the need for physical transport.

Use existing equipment roles to scope assessments, runtime observations/events as evidence, and operations performance for results. Preserve evidence quality, units and evaluation windows. Targets are not actuals. See the [synthetic assessment](examples/operational-value.json) and [management proposal guide](../docs/business/operational-value-model.md). Safety concepts and command authority remain independent of business objectives.
