# Operational Value Model

Status: draft design and proposal guide · 2026-09-28

Material handling generally does not add customer value directly, but material availability is a prerequisite for production. Some transport is necessary under the current layout and process constraints. The management objective is to eliminate unnecessary movement, minimize necessary movement, then automate the irreducible remainder where practical. JIT and Kanban help coordinate replenishment; physical movement still needs an execution method.

Assess work as **ValueCreating**, **NecessaryNonValueAdding**, or **AvoidableWaste**. Assess the activity, not the person or robot. Revisit necessity when the layout, demand or process changes. Automating an unnecessary trip preserves waste; automating a necessary trip can release people for work that requires their skills without making the trip itself value-creating.

## Build an AMR/AGV/AGF proposal
Start with one material flow and its existing process segment, equipment role, owner and constraints. Compare removal or layout changes, simpler handling methods and automation of the residual need. Select technology against the actual load, route, interfaces, exceptions and required service. A completed robot mission is evidence of transport, not proof that production had the right material on time.

| Objective | Technical evidence | Operational measure | Business connection |
| --- | --- | --- | --- |
| MaterialAvailability | Delivery, quantity and point-of-use acceptance timestamps | Requests ready in full by required time / eligible requests (%) | Less material starvation; validate production impact |
| FlowContinuity | Starvation and blocking events with reason codes | Material-related interrupted minutes per production hour | More usable production time at the constrained process |
| LaborRelease | Manual touch, supervision and recovery time | Net human hours released per comparable shift | Redeployed capacity; cash savings only with an explicit realization plan |
| WaitingReduction | Request, ready, pickup and arrival times | Median and p95 wait minutes by cause | Shorter lead time where transport waiting constrains flow |
| ExcessTransportReduction | Loaded/empty distance and transfer counts | Avoidable meters and handling steps per comparable unit | Lower handling effort and travel cost |
| WIPReduction | Lot quantities and process entry/exit records | Average WIP units and dwell time at comparable output | Less tied-up working capital; separate one-time release from recurring benefit |
| ErgonomicRiskReduction | Manual lift, push and pull exposure records | Change in exposure and site-assessed risk | Reduced physical burden; evaluate with the responsible safety owner |

For every measure record scope, unit, baseline, target, actual, period, evidence quality, assumptions and owner. Compare equivalent product mix, throughput and shifts; include downtime and exception work. Unknown data remains unknown. Robot utilization and mission counts are supporting technical measures, not standalone business success criteria.

## Decision and benefit realization
A concise approval case contains the current flow and avoidable work removed, residual service requirement, proposed equipment and integration scope, baseline and pilot targets, costs, and a named benefit owner. Include commissioning, infrastructure, support, energy, maintenance and recovery labor alongside equipment costs. Test demand and availability assumptions rather than promising a fixed payback from robot speed alone.

Report released hours separately from realized cost reduction. Report additional output only where demand and production constraints support it. Avoid counting the same released time as both labor savings and additional-output benefit. Do not add one-time WIP release to recurring annual savings. Ergonomic improvement is an objective requiring assessment, not a safety certification or authorization to bypass interlocks.

A pilot should demonstrate material readiness and sustained flow, net human effort, and reliable exception recovery against agreed targets. A favorable business case does not transfer motion or safety responsibility to the semantic model.

## Architecture and provenance
This guide extends the [architecture baseline](../architecture/automation-runtime.md) and [Tier 1 semantics](../../ontology/README.md). Definitions use existing factory IDs and process segments; relationships and the ordered improvement policy live in the existing hierarchy. Runtime, integration and safety remain separate responsibilities.

Provenance: owner-requested extension from AMR Weekly Brief, conversation `6a6bd8f5-0a70-83ee-b967-81af43d7280d`, carried into the 28 September 2026 repository update. The classifications, policy and metric suggestions are local design definitions, not normative standard requirements or demonstrated project results.
