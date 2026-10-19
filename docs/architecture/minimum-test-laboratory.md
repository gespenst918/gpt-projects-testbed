# Minimum Test Laboratory — architecture milestone and lab structure

Date: 2026-10-19

Status: proposed plan; no lab equipment, software implementation, test results, procurement, partner commitment or delivery date is asserted.

## Purpose and provenance

Establish a small, vendor-neutral integration laboratory to test equipment behavior, operational workflows and failure recovery before an industrial pilot. Propose L1 and a limited L2 internally, optional L2+ later, and L3 through separately agreed partner access. Purchasing an industrial AGF is not a prerequisite for early software validation.

This records the Minimum Test Laboratory scheme discussed in AMR Weekly Brief (conversation `6a6bd8f5-0a70-83ee-b967-81af43d7280d`, laboratory proposal `21062c94-8ad8-487e-819b-6b7172da4862`) and the owner's request to publish it as a milestone. These identifiers provide internal provenance. Every stage, component, role, budget, gate and acceptance criterion below is proposed, not implemented or passed.

## Architecture and layer ownership

Retain the [four-layer baseline](automation-runtime.md) and [Tier 1 vocabulary](../../ontology/README.md). The laboratory is a validation environment across these layers, not a fifth software layer.

| Existing responsibility | Proposed laboratory use |
| --- | --- |
| Operations Shell | Factory-facing material requests, assets, workflows, alarms and outcome evidence; Engineering View exposes mappings and raw diagnostics |
| Automation Runtime | Shared asset/event model, deterministic Event → Condition → Action → Exception workflows, permissions, task lifecycle, timeouts, logging and recovery |
| Integration Gateway | Versioned adapters and semantic mappings for VDA 5050, MQTT, REST, OPC UA and selected PLC/I/O interfaces |
| Execution Layer | Simulated endpoints initially; later existing vendor FMS, ROS2 systems, PLCs, WCS and robots execute their assigned operations |
| Factory semantics / Operational Value Model | Explain purpose, process constraints and performance measures; confer no command or safety authority |

Conceptual lab topology; observations return upward and authorized requests travel downward:

```text
Operations Shell
       |
Automation Runtime ---- event history / replay / test evidence
       |
Integration Gateway
       |
       +-- VDA 5050 / vendor adapter --> virtual robot/FMS (L1)
       |                                partner robot/FMS (L3)
       +-- equipment adapters --------> simulated PLC/WMS/equipment (L1)
       |                                real PLC / Ethernet remote I/O (L2)
       +-- optional ROS2 adapter ------> small development robot (L2+)

Scenario runner / event and fault injection --> isolated test interfaces
```

ROS2/Gazebo may support optional navigation or physical simulation behind an execution endpoint. They are not required for every deployment, do not replace VDA 5050 mappings, and do not move navigation ownership into the runtime.

### Operational value continuity

The existing Operational Value Model is proposed in [open PR #2](https://github.com/gespenst918/gpt-projects-testbed/pull/2), separate from this plan. Reviewed references: [business guide](https://github.com/gespenst918/gpt-projects-testbed/blob/a25ad48b8ba1e8b5a2bc4dd9c3f6c7cd3f6961c1/docs/business/operational-value-model.md), [glossary extension](https://github.com/gespenst918/gpt-projects-testbed/blob/a25ad48b8ba1e8b5a2bc4dd9c3f6c7cd3f6961c1/ontology/core/operational-value.json) and [architecture extension](https://github.com/gespenst918/gpt-projects-testbed/blob/a25ad48b8ba1e8b5a2bc4dd9c3f6c7cd3f6961c1/docs/architecture/automation-runtime.md). Pinned links document the reviewed revision; this milestone neither merges that proposal nor introduces its schemas into main.

Preserve `Operational objective → Process segment → Runtime task/action → Asset/capability`, scoped by Enterprise → Site → Area → Work center → Work unit. Equipment roles, physical assets and locations remain distinct.

Use the existing classifications ValueCreating, NecessaryNonValueAdding and AvoidableWaste: eliminate unnecessary movement, minimize necessary movement, then automate the irreducible remainder where practical. Automation does not reclassify transport as value-creating.

For the first scenario, select MaterialAvailability and FlowContinuity as proposed primary objectives, with LaborRelease and WaitingReduction as supporting measures where evidence exists. Other existing objectives remain ExcessTransportReduction, WIPReduction and ErgonomicRiskReduction; do not assert them as benefits without matching measurements.

Record material identity, usable quantity, location, required time and point-of-use acceptance; measure ready-in-full-by-required-time and material-related interruption minutes. Include manual handling, supervision and recovery in net human effort. Define scope, units, baseline, target, actual, evaluation period, evidence quality, assumptions and owner for every selected objective. Simulator results remain synthetic; released capacity is not realized payroll savings, and the same time cannot count twice as labor savings and output gain.

“Material Readiness Contract” below is a proposed scenario contract for this evidence, not an implemented schema or new ontology ID.

## Proposed laboratory stages

| Stage | Proposed contents | What it can establish | Limits / progression |
| --- | --- | --- | --- |
| L1 — Virtual lab | Development host, isolated MQTT broker, VDA 5050 towing-AMR and AGF simulators, simulated FMS, PLC, WMS and equipment, event store, scenario runner and fault injection | Semantic mappings, interface behavior, workflow outcomes and repeatable abnormal cases | No evidence of physical motion, handling performance or industrial safety; complete G1–G4 virtually before physical fault trials |
| L2 — Hardware-in-the-loop bench | One real Ethernet PLC, 1–2 Ethernet remote-I/O modules, 24 V DC supply, buttons, lamps, switches, 2–4 presence sensors, protected enclosure, managed switch and Wi-Fi access point; robots remain simulated | Real signals, physical handshakes, timing, electrical/interface integration and communication recovery | Select one documented controller interface first; ordinary I/O signals are process signals, not validated safety functions |
| L2+ — Optional mobile robot bench | Small ROS2-compatible development robot and controlled wireless/motion test area; optional Gazebo | Physical integration, state publication and bounded recovery experiments | Optional, not a gate substitute; cannot validate production tugger/AGF payload, stopping or load-handling behavior |
| L3 — Partner validation | Separately arranged access to real towing AMR / AGF, representative carts/pallets/loads, peripherals and warehouse operations | Supplier-specific interfaces, handling/handoff behavior, operational fit and FAT/SAT evidence | Requires partner agreement, interface access, assigned execution/safety owners and assessed site readiness; no current access is implied |

### L1 simulator and injection requirements

Use the repository's [VDA 5050 3.0 mapping](../../ontology/mappings/protocols/vda5050-3.0.json) as a study baseline, not a conformance claim. Pin the exact specification/schema, adapter and simulator versions per run; verify each partner's supported version, action vocabulary and capabilities. Supplier differences belong in explicit vendor/project mappings, not universal definitions. VDA order identity must not silently become the universal task ID.

Propose two synthetic profiles: towing AMR movement and coupling/decoupling; AGF movement, pallet detection, pickup, lift/lower and placement. Payloads and timings must be labeled test assumptions, never attributed to Doup or an OEM. Unsupported actions should be rejected explicitly.

Simulate machining stations, material buffers, shutters, conveyors, charging and operator call stations, plus WMS reservation/release and inventory events. Represent intermediate states, delays, unknown observations and transition timeouts, not just success booleans.

Inject scripted events and faults: pickup/coupling failure, destination unavailable, identity mismatch, missing operator acceptance, conflicting requests, broker outage, disconnection, latency, loss, duplication, reordering, stale messages and gateway/runtime restart. Software network injection is needed for controlled delay/loss; a managed switch alone is insufficient. Reject and log unauthorized commands.

### Proposed bench structure and future implementation artifacts

Keep an isolated test network with host/broker, PLC, I/O and access point; separate observation traffic, authorized command paths and fault-injection controls. Do not bridge test injections into production endpoints. L1 uses virtual endpoints; L2 replaces only selected PLC/I/O endpoints.

In the eventual implementation project, propose separate areas for:

- Scenario definitions and fixtures, including synthetic material/WMS data and fault schedules.
- Robot/FMS, PLC/WMS and equipment simulators.
- Gateway adapters and versioned vendor/project mappings.
- Bench I/O lists, signal semantics, wiring/protection records and topology.
- Run evidence: manifest, workflow version, endpoint versions, raw messages, mapped events, assertions and deviations.
- Partner FAT/SAT procedures, authority assignments and acceptance records.

These are proposed deliverables, not directories or executable test infrastructure created by this documentation change. Choose the implementation repository before building them. Keep credentials and confidential partner data outside this public hub.

## Indicative Japan planning budgets

**Planning only:** the JPY allowances below are carried from the October discussion, not researched current prices, verified quotations, purchase approvals or a complete project budget. Obtain Japan supplier quotations and confirm tax treatment, compatibility and scope before procurement. No existing computer or equipment ownership is assumed.

| Proposed equipment | Quantity | Discussion allowance (JPY, line total) |
| --- | --- | ---: |
| Development computer / local server | 1 | ¥0–200,000 |
| Managed industrial Ethernet switch | 1 | ¥20,000–60,000 |
| Industrial PLC / compact controller | 1 | ¥50,000–150,000 |
| Ethernet remote I/O | 1–2 | ¥20,000–80,000 |
| 24 V DC power supply | 1 | ¥8,000–20,000 |
| Buttons, lamps and switches | 1 set | ¥10,000–30,000 |
| Photoelectric / proximity sensors | 2–4 | ¥10,000–40,000 |
| Enclosure, DIN rail, terminals and protection | 1 set | ¥20,000–60,000 |
| Wireless access point | 1 | ¥10,000–30,000 |
| **Itemized equipment envelope** | | **¥148,000–670,000** |

The ¥0 host allowance is conditional on later-confirmed reuse, not a claim of an owned host. The non-host equipment envelope is ¥148,000–470,000.

| Proposed stage | Incremental planning allowance | Assumption |
| --- | ---: | --- |
| L1 | ¥0–50,000 | Reused host; add host cost if unavailable |
| L2 | ¥200,000–350,000 | Initial constrained integration bench; scope to quotations |
| L2+ (optional) | ¥100,000–300,000 | Small development robot and associated bench additions |
| L3 | Project-specific, not estimated | Partner equipment access, site work and validation separately scoped |

The discussion also suggested a ¥250,000–350,000 physical-bench target excluding a reused computer. These stage targets and the itemized envelope are alternative scoping views with overlapping items; do not add them together as independent purchases. Neither narrow L2 target guarantees the full upper-end equipment list.

Exclude engineering time, contractors, PLC engineering software/licenses, paid SDKs, travel, transport, partner fees and site-specific safety measures from these allowances; taxes and recurring costs remain to be confirmed. Budget external controls/safety support and L3 validation separately. Defer heavy industrial robot purchase until the use case, facility and partner access justify it.

## Five proposed test gates

All gates are unpassed. Before execution, agree test cases, quantitative timing/freshness/throughput limits, repetition count, owners and review criteria; do not choose thresholds after seeing results. A gate requires its evidence and disposition of deviations, not a demonstration alone.

| Gate | Proposed acceptance condition | Proposed evidence / owner role |
| --- | --- | --- |
| G1 — Semantic integrity | Schema/reference checks and mappings preserve IDs, units, timestamps, source, quality and mapping version; unknown, unsupported and stale stay distinct; missing boolean never becomes false; state/mode/connectivity/safety remain independent; each selected value objective has an appropriate measure | Ontology validation, mapping fixtures and negative cases; semantic/model owner |
| G2 — Interoperability | Pinned VDA 5050/API and PLC/I/O interfaces exchange required supported requests/states; unsupported capabilities and unauthorized requests are rejected; mappings retain protocol identities and extensions | Version/capability matrix, raw and mapped traces, contract test records; gateway owner with interface supplier |
| G3 — Workflow execution | All three replenishment variants reach their specified outcome or controlled exception; successful completion requires destination acceptance and material readiness evidence, with no duplicate dispatch or inventory effect | Correlated task/action, station and WMS histories plus objective measures; runtime owner and process owner |
| G4 — Failure recovery | Defined outages, stale/duplicate/reordered events and restarts are detected; ambiguous outcomes remain unresolved until reconciliation; no blind redispatch, duplicate handoff or inferred restart | Fault matrix, replay/restart records, alarm and authorized recovery audit; runtime/gateway owners with execution owner |
| G5 — Partner FAT/SAT | Repeat the scoped scenario and substitution criterion on agreed real equipment, then validate the site workflow under representative warehouse conditions against agreed service and exception limits | Factory Acceptance Test (FAT), Site Acceptance Test (SAT), assigned partner/site acceptance and separate safety evidence; partner execution owner and site process/safety owners |

G1–G4 start in L1 and are repeated for affected real interfaces in L2/L3. L2+ is optional. G5 includes partner-facility FAT before site SAT; this does not require entering a factory to discover basic recovery defects. Software gates do not certify machine safety. Triage any earlier ontology/Operational Value Model review findings and record their disposition; this plan does not claim those findings are fixed or that their current count is verified.

## First proposed scenario: machining-station material replenishment

Scope one machining station, one receiving point, a material buffer / virtual warehouse, a WMS endpoint and one transport resource. Keep machining execution with the machine/CNC/PLC owner. Use simulated devices at L1, real station PLC/I/O at L2, then partner vehicles at L3.

Before testing, freeze the factory-facing workflow, material identity/quantity, source and destination, required production time, destination capacity/acceptance rules, freshness limits, timeouts and recovery owner. Retain the existing runtime task lifecycle; phase names below are test descriptions, not new canonical states.

1. Station/operator requests material; WMS confirms/reserves the required material.
2. Runtime checks fresh material availability, destination acceptance/capacity, capability support and command authority.
3. Gateway submits the authorized transport request; execution owner acknowledges and executes it.
4. Confirm pickup/load acquisition; retain material and task/order correlation.
5. Observe arrival and request the permitted receiving handshake.
6. Validate material identity, usable quantity and point-of-use acceptance from the station/operator and WMS evidence.
7. Complete the workflow only when the Material Readiness Contract is satisfied; record whether readiness preceded the required production time.

An MQTT acknowledgment, robot arrival or transport-complete report alone is insufficient. A presence sensor alone does not establish material identity or quantity; require appropriate WMS/operator evidence.

| Variant | Proposed injection | Required observable outcome |
| --- | --- | --- |
| Normal | No injected fault; material accepted before the agreed required time | Exactly one dispatch and handoff; correct material/quantity usable at the destination; correlated acceptance and completion evidence; readiness timing recorded |
| Destination unavailable | Destination stops accepting after dispatch, before delivery | Runtime blocks the receiving handoff, raises an actionable exception and retains task/material ownership; execution owner determines permitted hold behavior. Resume only after fresh acceptance and authorized recovery, or use a separately approved alternate/cancel path; never silently reroute or mark delivered |
| Post-arrival communication loss | Disconnect after vehicle arrival is observed, before receiving acceptance reaches the runtime | Mark affected observations stale/unavailable after the agreed limit; leave acceptance unresolved and workflow incomplete; alert with recovery owner. Do not infer delivery, absence or a need to resend transport. On reconnection/restart, reconcile authoritative robot, station/operator and WMS records; deduplicate delayed acceptance and apply at most one completion/inventory effect |

For the loss variant, test both physical acceptance during the outage and no physical acceptance. Recovery must distinguish them; if evidence cannot resolve the result, require an authorized operator check. Late but valid acceptance may establish delivery while still recording a missed service deadline.

Each run should retain a manifest (scenario/configuration, workflow and adapter versions, simulated/physical endpoints, capabilities, fault schedule and expected outcomes), timestamped raw/mapped evidence, assertions, alarms, recovery actor and disposition. L1 logs must be labeled synthetic rather than actual operational performance.

## Safety and control authority boundaries

Follow the [existing safety boundaries](../../ontology/safety/boundaries.json). Observation, workflow configuration, command execution and recovery require distinct permissions. Capability support and visibility in the shell do not grant authority.

The runtime coordinates authorized process requests. The gateway translates and validates mappings. Vendor FMS/robot controllers and PLCs retain their assigned navigation, motion, machine sequences and interlocks; designated safety systems and responsible engineers retain safety functions and validation. No cost, urgency, semantic label or AI suggestion overrides these boundaries.

Ordinary Ethernet remote I/O and a 24 V bench are not safety controllers. A test button or displayed safety observation does not implement an emergency stop. Unknown/stale safety information never means safe; reset is distinct from restart and communication restoration must not imply automatic motion restart. Operational route/zone permission is not safety clearance.

Perform disruptive network trials virtually first. Physical fault tests require a separately assessed test area, documented execution-owner behavior and authorized procedures. Do not assume loss of communication necessarily stops a vehicle. Partner/site owners must determine applicable standards, risk assessment and safety-function validation before physical trials; no compliance verdict or certified safety performance is claimed here.

## Proposed partner roles — no commitments

| Candidate / role | Proposed request and contribution | Boundary / acceptance focus |
| --- | --- | --- |
| Doup | Documented capabilities, mission/state/fault interfaces, API/SDK versions, simulated FMS endpoint, possible later test-vehicle access | Candidate collaboration only; no assumed VDA support, hardware access or commercial agreement; validate abstraction without needing proprietary navigation internals |
| Robot OEM / AMR or AGF supplier | Specifications, supported actions, load-handling/error definitions, interface documentation and supervised trials | Own assigned vehicle execution/control and safety responsibilities; demonstrate towing/handling and recovery on representative equipment |
| Material-handling partner | Conveyor/shutter/docking state tables, handshakes, interface test access and representative peripherals | Define process handoff evidence, interlocks and equipment ownership |
| Warehouse partner / operator | Anonymized WMS events, material flows, demand/throughput and exception records, later site access | Validate material readiness and Operational Value Model measures against real operations; own site process acceptance |
| PLC system integrator (SI) | I/O lists, sequence descriptions, controller/interface access and bench engineering | Verify brownfield mappings, signals and recovery with controls/safety owners |

Leiomano would own the semantic model, runtime, adapter framework and test evidence responsibilities under a future agreement; supplier control software and responsibilities stay separately defined. Confirm interfaces, access rights, support hours, data permissions and FAT/SAT responsibilities before relying on any partner. No partnership, equipment inventory or willingness to provide access is established by this plan.

## Proposed acceptance milestone and next decisions

**Milestone: replace the virtual robot with a partner robot without altering the factory-facing workflow.** Reuse the frozen replenishment workflow, factory objects, task outcomes, Material Readiness Contract and all three scenario variants. Endpoint configuration, capability bindings and explicit vendor/project adapters/mappings may change; factory-facing conditions, actions, exceptions and success meaning must not require supplier-specific rewrites.

Record before/after workflow versions, adapter/configuration differences and G1–G5 evidence. If the partner robot lacks a required capability, report the incompatibility and leave the milestone unmet; do not weaken the workflow to claim success. Representative physical test methods must be agreed with execution/safety owners.

This validation milestone supports the existing M0–M4 planning sequence without renumbering it: define scope/contract at M0, validate adapters at M1, execution/recovery at M2, shell diagnosis at M3, and partner/site evidence at M4. It is neither a delivered platform nor productization approval.

Next decisions: name the implementation repository and gate owners; freeze the first contract and measurable limits; choose one PLC/interface and obtain quotations; implement L1; scope limited L2 after interface tests; decide whether L2+ adds useful evidence; negotiate L3 access and FAT/SAT criteria. Procurement, real-equipment control and partner agreements require their own decisions.

## Related planning

- [Architecture baseline and existing milestones](automation-runtime.md)
- [Tier 1 semantic baseline](../../ontology/README.md)
- [Automation advisory](../../projects/automation-advisory/README.md)
- [Roadmap](../../strategy/roadmap.md)
