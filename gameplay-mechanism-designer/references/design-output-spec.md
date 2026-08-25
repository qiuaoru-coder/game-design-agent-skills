# Full design and prototype output specification

Use sections only when they materially apply. Preserve user-specified structure if one is provided.

## Full Design

1. **Gameplay promise**: player fantasy, main action, and distinctive tension in one sentence.
2. **Goals**: player, experience, and design/product goals; name assumptions.
3. **Audience and format**: target player, platform, camera, controls, player count, session.
4. **Core decision**: repeated non-obvious choice, alternatives, information, cost, and tradeoff.
5. **Design coordinates**: primary and supporting `WHAT state domain × HOW mechanism element × WHERE placement/carrier`.
6. **Mechanism-chain map**: source IDs/formulas, adaptations, conditions, branches, and state passed between chains.
7. **Core loop**: selected loop pattern, explicit carrier on each arrow, reset, persistence, escalation, interruption, and exit.
8. **System network**: nodes and labeled relations when multiple systems exist; include carriers, receiver rules, polarity, caps/delays, and observability.
9. **Rules and states**: actors, objects, resources, relationships, permissions, triggers, timing, success/failure, cleanup.
10. **Content structure**: encounters, levels, enemy roles, items, challenges, variation and authoring burden.
11. **Progression and economy**: sources, sinks, pacing, caps, resets, unlocks, abuse and dominant-strategy risks.
12. **Feedback and usability**: controls, camera, UI, audio/visual feedback, readability, onboarding, accessibility.
13. **Difficulty and balance levers**: tunable parameters and expected behavioral effects.
14. **Production scope**: disciplines, costly dependencies, content load, technical uncertainty, and cut candidates.
15. **Risks and open decisions**: goal/logic risks first, network and balance risks second, production risks third.

## Prototype Pack

Start with:

```text
We believe [target player] will experience [target experience]
because [core decision and mechanism/loop].
We will know this is plausible when [observable behavior or metric].
```

### Design trace

Name the prototype's primary `WHAT × HOW × WHERE`, source/adapted chains, loop pattern, and any system relation being tested. Exclude framework layers irrelevant to the hypothesis.

### Build scope

- one playable scenario and target playtime;
- required actors, objects, environments, rules, and UI;
- required mechanics in implementation order;
- placeholder content allowed;
- explicit exclusions and post-validation backlog.

### State model

For every important entity:

```text
Entity:
States:
Variables:
Inputs/events:
Transitions and guards:
Outputs/side effects:
Reset/persistence behavior:
```

### Rule table

For each rule, provide trigger, precondition, action, result, feedback, priority, cancellation, and edge cases. State authority ownership for networked designs.

### Loop and network trace

List the state returned into the next round. For multi-system tests, list every carrier crossing a system boundary and the receiving rule. Define feedback limits, delays, and reset points.

### Parameter table

Provide initial value, safe test range, expected behavioral effect, and reason. Include only relevant timing windows, movement values, costs, rewards, probabilities, capacities, and thresholds.

### Test plan

Include:

- onboarding comprehension;
- core decision frequency and diversity;
- whether players perceive the intended state change and placement;
- whether the loop changes the next decision;
- whether system effects and causality are visible;
- success/failure distribution;
- dominant or degenerate strategies;
- pacing and downtime;
- player explanation after play;
- telemetry events and properties;
- stop, revise, or expand criteria.

### Handoff

End with implementation order, responsible discipline when known, biggest unknown, cut list, and the decision to make after the first playtest.
