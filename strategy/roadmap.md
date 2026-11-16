# Roadmap
Updated: 2026-11-16
This is a starting sequence, not a dated delivery commitment.

## Initial priorities
1. Business development: draft a reusable company introduction and service outline.
2. Ways and means: document one end-to-end consulting method, starting with market assessment.
3. Orbit assistant: inventory the existing application and clarify its next milestone before importing any code.

## Build alongside these
- Add sourced Japan-market case studies and pricing references as research becomes available.
- Capture reusable manufacturing and automation knowledge.
- Improve templates after using them on real work.

## Later / exploratory
- Assess audit-services feasibility.
- Move substantial applications into dedicated repositories when needed.

Track individual actions in GitHub Issues. Keep this page focused on priorities and milestones.

## Weekly decision — 7 September 2026
The automation-platform direction now combines a factory-facing Operations Shell with an Automation Runtime, Integration Gateway, and Execution Layer. Low vendor dependency and ease of learning are joint priorities; VDA 5050 is a priority interface.

See the [architecture baseline](../docs/architecture/automation-runtime.md). The next planning step is to identify the separate implementation project and one representative factory workflow. MVP sequencing and technical choices in the note remain proposals, not delivery commitments. Existing priorities above remain in place.

## Proposed milestone — Minimum Test Laboratory, 19 October 2026

Status: proposed architecture validation and lab-structure plan; not implemented. See the [full plan](../docs/architecture/minimum-test-laboratory.md).

- L1: virtual VDA 5050 robot/FMS, PLC/WMS/equipment endpoints, event and fault injection.
- L2: real PLC, Ethernet remote I/O and 24 V integration bench; optional L2+ small ROS2 development robot.
- L3: separately agreed partner towing-AMR/AGF and warehouse validation.
- Progression evidence: semantic integrity, interoperability, workflow execution, failure recovery, then partner FAT/SAT. No gate has passed.
- Acceptance milestone: replace the virtual robot with a partner robot without altering the factory-facing machining-station replenishment workflow, including destination-unavailable and post-arrival communication-loss behavior.

This complements the architecture note's M0–M4 sequence without renumbering it. Next: choose the implementation repository, contract, measurable acceptance limits and owners, then build L1 and scope limited L2. Budgets are planning-only allowances; no equipment ownership, purchase, partner commitment or date is assumed. The Operational Value Model remains a separate proposal in [PR #2](https://github.com/gespenst918/gpt-projects-testbed/pull/2).

## Approved development baseline — 16 November 2026

The M0–M6 sequence below is the approved planning baseline from the AMR Weekly Brief discussion. Revisit it when implementation evidence reveals a substantial technical or resource constraint. All milestones are planned; none is recorded as implemented, tested or validated. No equipment ownership, partner commitment or delivery date is implied.

This sequence supersedes earlier proposed implementation sequencing for the on-premises development effort without renumbering historical architecture notes. The Minimum Test Laboratory L1–L3 environments and five validation gates remain applicable. Operations Shell, Automation Runtime, Integration Gateway and Execution Layer retain their existing responsibilities.

| Milestone | Planned scope | Acceptance evidence required |
| --- | --- | --- |
| M0 — Secure host and network | Host updates, account permissions, storage encryption, backups, segmentation and controlled remote access | Unauthorized cross-zone access is blocked; an encrypted backup is restored successfully. |
| M1 — Encrypted knowledge base and Qwen | Encrypted SQLite-compatible storage, local inference and a small approved reference collection | Local retrieval cites its sources; unauthorized retrieval is rejected. |
| M2 — Proposal-generation MVP | Structured requirements, verified calculations, simulation inputs, drafting and human approval | Reproduce one approved AMR/AGF proposal with correct assumptions, units and supporting evidence. |
| M3 — Operations Shell MVP | Browser interface for assets, documents, proposals, workflows, scenarios and events | Consistent operational objects are visible without requiring users to interpret protocol details. |
| M4 — Virtual simulation laboratory | Simulated towing AMR, AGF, workstation and material buffers, with equipment and network faults | A material-readiness scenario passes reproducible normal and exception tests. |
| M5 — PLC and remote-I/O integration | Physical controller interfaces, validated state mappings, handshakes and diagnostics | The same workflow operates through simulated and real PLC interfaces while preserving command authority. |
| M6 — Partner AMR/AGF validation | Replace the simulated transport executor under an agreed partner test plan | Factory-facing workflow remains unchanged; physical operation, recovery and safety are validated separately. |

### Architecture direction

Build an internal engineering environment that can inform a future on-premises reference implementation: encrypted know-how storage, local Qwen-assisted processing, a dashboard, proposal generation, simulation and controlled PLC interfaces. Hardware requirements must come from measured workloads, recovery tests and interface compatibility. Exact host, model, encryption implementation and deployment sizing remain subject to verification.

Keep language-model interpretation and drafting separate from deterministic calculations, simulation, authorization and workflow execution. Preserve provenance, permissions and the distinction between supplier claims, assumptions, simulations and measured results. External proposal release requires human approval. Neither AI access nor a business objective grants equipment command authority.

### Follow-up proposals — not yet approved acceptance additions

The later network-security discussion proposes explicit M0 security and resilience tests: unauthorized commands, stale or duplicated messages, lost connections and visible unresolved task status. Public cellular transport should not itself confer application trust. Define responsibility for credentials, remote maintenance, updates and communication-loss handling.

Cybersecurity and vehicle functional safety remain separate responsibilities. Vehicle safe-state behavior requires its own risk assessment and validation; no blanket stop behavior is specified here. Lost communication must not be treated as evidence of task completion. These proposed details need review before becoming additional acceptance criteria.

### Cadence and provenance

Daily development stand-ups are envisaged when implementation begins; no daily schedule is activated by this note. Track planned, implemented, tested and validated states separately.

Source: AMR Weekly Brief, 16 November 2026 — environment planning, explicit M0–M6 approval, then the subsequent network-security discussion. This public summary excludes private network configuration, credentials, client information and commercial pricing. It makes no hardware-availability, performance or standards-conformance claims.
