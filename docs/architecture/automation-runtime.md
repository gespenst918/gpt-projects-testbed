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
