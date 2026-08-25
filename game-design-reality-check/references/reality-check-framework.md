# Game-design reality-check framework

Use this reference to challenge a design claim without confusing skepticism with certainty.

## Core principle

“This game will be fun” is not a useful testable claim. Fun is an umbrella report produced by different players for different reasons. Decompose it into a target player, situation, mechanism, expected behavior, intended experience, and observable failure signal.

The review should answer four questions:

1. What exactly does the proposal claim will happen?
2. Through what causal chain should it happen?
3. What evidence currently supports each important link?
4. What is the cheapest test that could change the next decision?

## Claim anatomy

Use this form for important claims:

| Part | Question |
| --- | --- |
| Audience | For whom is the claim expected to hold? |
| Context | Under what platform, session, social, skill, and content conditions? |
| Cause | Which rule, interaction, content, presentation, or structure creates the effect? |
| Behavior | What will players actually do, notice, learn, choose, or repeat? |
| Experience | What feeling, fantasy, understanding, or social response is intended? |
| Boundary | When should the claim not be expected to hold? |
| Failure signal | What observation would weaken or reject it? |
| Decision | What will the team do if it is supported, mixed, or contradicted? |

If the claim has no failure signal or attached decision, it is a belief or aspiration rather than a validation hypothesis.

## Evidence ledger

Classify evidence without collapsing quality into a single score.

### Observed

Directly observed in a relevant prototype, playtest, telemetry sample, production build, or shipped game. Record sample, build, conditions, task, and whether the behavior was spontaneous or prompted.

### Sourced

Supported by a comparable game, research source, market record, usability convention, technical measurement, or other external evidence. Record why the source is comparable and where it is not.

### Derived

Follows from explicit rules, math, state transitions, performance constraints, or production facts. Derived evidence can establish what the system permits or incentivizes, not how players will necessarily feel or behave.

### Assumed

Plausible but inadequately evidenced. Assumptions are normal; hidden assumptions are dangerous. Rank them by impact, uncertainty, and cost of being wrong.

### Unknown

Information is missing or the question cannot yet be resolved. Do not turn an unknown into a negative finding unless the missing evidence itself blocks a decision.

## Confidence dimensions

When confidence matters, state the dimensions rather than producing false precision:

- **Relevance**: does the evidence represent the target game, audience, and context?
- **Strength**: can the evidence distinguish the claim from alternatives?
- **Coverage**: does it test the whole causal chain or only one link?
- **Repeatability**: does the effect recur across players, sessions, builds, or conditions?
- **Freshness**: does it reflect the current design and market context?

Use high/medium/low only when it helps the decision, and explain the limiting dimension.

## Common self-confirming patterns

| Pattern | Reality-check question |
| --- | --- |
| Designer fluency | Would a new player see the option, understand it, and predict its consequence? |
| Feature-count confidence | Which repeated decision becomes better because this feature exists? |
| Effort justification | What player evidence exists independently of the work already spent? |
| Novelty equals value | After the surprise ends, what remains worth mastering or repeating? |
| Theme equals experience | Which interaction, pacing, sensory, or narrative tools actually create the intended feeling? |
| Choice equals depth | Are alternatives readable, viable, consequential, and dependent on context? |
| Difficulty equals engagement | Does failure teach and invite another attempt, or only obstruct progress? |
| Positive feedback equals proof | What did participants do before being asked whether they liked it? |
| Reference-game analogy | Which causal structure is actually shared, and which production advantages are missing? |
| Core fun will fix content | How much variety can the rule generate before authored content must carry it? |
| Retention from session fun | What return motivation, progression, social state, or unfinished goal persists between sessions? |
| Monetization from engagement | Does the proposed value exchange preserve the decisions and experience being validated? |

## Failure-first review

For each important hypothesis, name:

- the earliest causal link that can break;
- the most damaging plausible player strategy;
- the strongest alternative explanation for positive evidence;
- the quality or content dependency omitted by a greybox;
- the audience segment or context where the claim may fail;
- the cost of learning the answer after full production instead of now.

Do not manufacture objections. A failure case matters when it is plausible, consequential, and connected to the actual design.

## Minimum decisive test

A useful test isolates uncertainty rather than recreating the whole game.

```text
Hypothesis:
Decision this test informs:
Target participants and context:
Required rules/content/feedback:
Explicit exclusions:
Behavioral observations:
Questions asked after observation:
Useful measurements:
Support signal:
Revise signal:
Stop signal:
Confounds and alternative explanations:
Next action for each result:
```

Do not set arbitrary numeric thresholds merely to appear rigorous. Use thresholds when the decision, baseline, expected sample, or operational constraint gives them meaning. Otherwise define directional or qualitative decision rules and state the limitation.

## Reviewing evidence after a test

1. Preserve the original hypothesis and decision rule.
2. Separate observation from participant explanation and reviewer inference.
3. Look for prompting, selection, novelty, facilitator, build, order, and learning effects.
4. Identify whether the test exercised the critical GMT links.
5. Update only the claims the evidence addresses.
6. Record what remains unknown and the next decision.

A failed hypothesis is useful evidence. Do not rescue it by silently changing the target audience, experience, or success condition after seeing the result.
