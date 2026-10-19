# Roadmap
Updated: 2026-10-19
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
