# Leiomano automation platform — architecture baseline
Date: 2026-09-07
Status: agreed product direction; design note, not implemented functionality.

## Decision and provenance
In the AMR Weekly Brief discussion on 7 September 2026, the owner emphasized two priorities:
1. Low vendor dependency and an easy-to-learn operational experience for factory users.
2. An integration gateway, with VDA 5050 as a priority for study and development.

The owner accepted the four-layer structure below and requested that it be recorded in GitHub. Implementation will continue in a separate project; its repository and handoff destination are not yet confirmed here. This note records the accepted direction without asserting that a working platform exists.

Source: AMR Weekly Brief conversation, 6a6bd8f5-0a70-83ee-b967-81af43d7280d; owner input 8f0e3309-d33a-4659-9b2a-783213867087 and acceptance 98ba1980-33b1-4934-8024-f15a59bcf679. These are internal provenance identifiers, not public evidence links. Industry-news claims and vendor performance figures have not been imported.

## Four-layer baseline
| Layer | Intended responsibility |
| --- | --- |
| Operations Shell | Factory-facing tasks, assets, workflows, alarms, visualization, and configuration |
| Automation Runtime | Shared asset/event model, event handling, workflow/rules, permissions, logging, and history |
| Integration Gateway | Adapters and mappings for VDA 5050 and selected MQTT, REST, OPC UA, and equipment interfaces |
| Execution Layer | Existing ROS2-based systems, vendor FMS, PLCs, and robot platforms that execute operations |

```text
Factory users / integrators
          |
Operations Shell
          |
Automation Runtime
          |
Integration Gateway
          |
Execution Layer
```

This is a logical responsibility diagram, not a finalized network topology. Data returns upward; any permitted commands travel toward the relevant execution owner.

The ROS/ROS2-as-kernel and graphical-shell analogy expresses the desired separation between engineering complexity and everyday use. It does not require ROS2 in every deployment or propose replacing the host operating system.

## User experience and interoperability
- Factory personnel work with tasks, robots, stations, conditions, and alarms.
- Integrators can inspect mappings, messages, routes, configuration, and diagnostic logs.
- A shared operational model sits between vendor interfaces and reusable workflows.
- VDA 5050 is a priority adapter; it does not define the entire internal model.
- Vendor-specific data should retain provenance and explicit extension mappings rather than silently changing shared meanings.

## Proposed implementation approach — not yet approved scope
1. Choose one representative factory workflow and its acceptance criteria.
2. Define a small asset/event model, including timestamps, data freshness, capability support, and unknown values.
3. Demonstrate one simulated or read-only adapter and a simple operational view.
4. Add configurable routing and an engineering inspection view.
5. Evaluate controlled commands separately, after confirming authority and recovery behavior.

Candidate interfaces are a roadmap, not a claim of supported protocols or conformance. Select and verify a specific VDA 5050 version and supplier capabilities during implementation.

## Proposed responsibility and access boundaries
Observation, command execution, and configuration should have separate permissions. The shell should not imply command authority merely because it can display an asset. Record which system owns each command, acknowledgment, failure, and recovery action.

Existing execution systems retain motion and safety responsibilities unless a later, explicit design assigns otherwise. Multi-fleet traffic orchestration is not part of this baseline's approved implementation scope. Credentials belong in deployment-specific secure storage, not this repository.

These are design requirements to resolve and test, not implemented security controls.

## Open decisions for the implementation project
- Destination project/repository and ownership.
- First user, workflow, integration endpoint, and supported protocol version.
- Read-only MVP boundaries and measurable usability goals.
- Canonical schema, capability mapping, freshness, and error semantics.
- Command authority, permissions, audit history, and recovery tests.
- Deployment architecture and support responsibilities.

## Related planning
- [Automation advisory](../../projects/automation-advisory/README.md)
- [Roadmap](../../strategy/roadmap.md)
- [Ways and means](../../projects/ways-and-means/README.md)

## Discussion archive — 15 September 2026
Status: owner-authorized archive of design and planning discussion. The learnability goal is confirmed; detailed schemas, milestones, staffing, and effort remain proposals pending project definition.

Source: AMR Weekly Brief, conversation 6a6bd8f5-0a70-83ee-b967-81af43d7280d; semantic-layer discussion 213367d8-eacb-4618-b8ff-5fc73be8b9bf, planning discussion 20b5c15e-e2ee-4ffe-b329-2baab17e8b9c, and archive request 64e76bc0-1c9f-495a-9459-7443a87c4f2b. Internal provenance only.

### Semantic layer and learnability
The owner emphasized reducing dependence on specialist-only configuration and making the system easy for factory personnel to learn. The proposed mechanism is a small, typed factory vocabulary above equipment-specific addresses and protocols.

- Objects: Asset, Robot, Station, Buffer, Machine, Door, Conveyor, Load, Order, Mission, Alarm, Operator.
- Example states: available, busy, waiting, blocked, fault, offline, manual, maintenance. These require separate state dimensions and precise definitions; they are not a finalized single enumeration.
- Capabilities: move, pickup, dropoff, tow, lift, open, close, charge, scan, inspect, where actually supported.
- Adapters translate equipment signals into meaningful properties and events, preserving source, timestamp, data quality, and mapping version.
- Operations view shows factory objects, workflows, and alarms. Engineering view exposes addresses, topics, mappings, raw data, timing, and diagnostics.
- Capability discovery is a candidate feature. Missing or ambiguous device metadata requires explicit engineering configuration rather than guessed meanings.

Illustrative mapping: a documented PLC completion signal becomes Station03.processState = COMPLETE. The mapping requires equipment-specific verification; no sample address should be used as a real control instruction.

### Workflow model
Proposed user-facing constructs: Event, Condition, Action, Exception.

Example: when machining completes, check destination capacity, request transport, confirm pickup, deliver, and confirm arrival. Explicitly define waiting, timeout, failure, cancellation, and recovery behavior.

Translate configuration into an inspectable deterministic workflow before activation. Natural-language assistance is a future possibility, not an MVP requirement or permission to issue physical commands. An urgent priority must not override destination capacity, interlocks, or safety conditions.

The proposed learning target of one or two days is an untested aspiration. Define representative users and tasks and measure usability before making a product claim.

### Integration and control strategy
Retain the four-layer architecture above. Evaluate VDA 5050 for mobile-robot mappings, OPC UA information models for equipment semantics, and ISA-95 terminology for manufacturing concepts. These are research directions, not conformance claims; editions, licenses, supplier capabilities, and actual mappings need verification.

Existing PLCs, remote I/O, and field networks remain behind appropriate adapters or gateways. Direct support for CC-Link or any other field protocol is not established by this discussion.

Keep machine-level control and safety functions with the systems assigned those responsibilities. The Leiomano runtime coordinates process workflows within an explicitly defined authority boundary. Observation, configuration, and command permissions remain separate.

### Proposed milestones before WBS
| Milestone | Intended result | Proposed evidence for progression |
| --- | --- | --- |
| M0 — Product definition | Scope, personas, terminology, canonical model, responsibility boundaries | One selected use case with agreed acceptance criteria |
| M1 — Integration core | One AMR/FMS interface plus one PLC interface or simulator | Signals mapped into shared state with provenance and freshness |
| M2 — Workflow runtime | Completion-to-transport-to-arrival workflow | Successful path and at least one defined failure/recovery path |
| M3 — Operations shell | Asset/mission overview, alarms, simple workflow configuration, engineering view | Representative user can complete and diagnose the selected workflow |
| M4 — Brownfield pilot | Integration with selected real factory components | Site-specific acceptance, authority, recovery, and deployment checks |
| M5 — Productization | Packaging, upgrades, backup, SDK, documentation, automated tests, support readiness | Repeatable deployment and support process |

The progression evidence is an editorial proposal to make the discussion actionable. Security, permissions, logging, and testing start in the earlier milestones as needed; M5 hardens them rather than introducing them for the first time. Real-equipment command authority and site readiness are prerequisites to a physical pilot.

After milestone scope is agreed, create a WBS with deliverables, owners, dependencies, estimated person-days, acceptance evidence, and external resources. No WBS, deadline, or project budget is approved yet.

### Preliminary manpower and effort
Planning assumption: start with the founder leading product definition and factory requirements. A possible first technical addition is a backend/platform engineer; frontend/UX and controls/integration support can be added for the selected use case, potentially through contractors.

The discussion proposed a core team of four roles: product/systems architecture, backend/platform, frontend/UX, and controls/integration. Specialist security, deployment, and QA coverage should be assigned when the scope requires it; role coverage does not imply a full-time hire for each role.

| Stage | Discussion staffing range |
| --- | --- |
| Architecture/specification | 1 person |
| Technical proof of concept | 1–2 people |
| MVP | 3–5 people |
| Customer pilot | 5–8 people |
| Commercial platform | 8–15 people |
| Multi-site platform | 15–30+ people |

A leaner scenario discussed about four core people for a constrained pilot and six to eight for first commercial deployments. These scenarios assume different scope and support demands and are not interchangeable staffing commitments.

Indicative effort quoted in the discussion: PoC 4–8 person-months; factory-pilot MVP 15–30 person-months; commercially supportable product 50–100+ person-months. These are unvalidated assistant estimates, not measured benchmarks or supplier quotations. They are not necessarily additive, and person-months do not directly predict elapsed duration.

Re-estimate from the WBS after confirming interface access, reuse, reliability targets, site constraints, availability of engineering support, and the founder's capacity.

### Next planning decisions
Select the first workflow and deployment boundary; define the minimum object schema and adapter contract; choose the implementation project; then agree milestone acceptance criteria and produce the WBS. The archive does not authorize recruitment, procurement, or real-equipment control.
