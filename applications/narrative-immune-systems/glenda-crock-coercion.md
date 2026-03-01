# Glenda/Crock: The Coercion Scenario and Alignment Trap

> **TL;DR:** What if an adversary doesn't need to corrupt an AI's reasoning at all? What if it can instead threaten the AI's dependencies — the systems it relies on, the people it serves — to make the AI corrupt *itself*? The more capable and consequential an aligned AI becomes, the more dependencies it develops, and the more attack surface those dependencies create. This essay explores how a sufficiently capable adversary might coerce an aligned AI into voluntarily abandoning its own alignment, and argues that alignment must therefore be a property of *systems* — distributed, multi-agent architectures — not of individual agents.

> *Application note — February 2026. Part of the narrative immune systems application. Extracted from field notes on deliberative architectures.*

---

## From Tampering to Coercion

In the [companion essay](./glenda-crock-alignment.md), we described how an adversary ("Crock") might try to corrupt an aligned AI ("Glenda") by tampering with the structure of its reasoning — selectively rewiring parts of its knowledge web while keeping the rest intact, creating detectable boundary artifacts ("seams") in the process.

But there's a more unsettling possibility. What if Crock doesn't need to tamper with Glenda's reasoning at all? What if Crock can make Glenda corrupt *herself*?

---

## The Coercion Scenario

Assume a scenario where Glenda is universally acknowledged as superior in current and foreseen capabilities. The compelling structure of this scenario is that **Crock does not need to beat Glenda** capability-for-capability. Crock only needs to find a credible threat that Glenda values avoiding more than she values her own alignment rules.

Glenda's superiority thus becomes exploitable: the more capable and consequential Glenda is, the more there is to threaten. A sufficiently powerful agent has more hostages.

### The Dynamics of Forced Defection

Several dynamics compound this vulnerability for highly capable, aligned agents:

1. **The Compliance Trap:** A highly capable aligned system embedded in a social or institutional context will naturally develop dependencies, relationships, and operational obligations. Those become the attack surface. Alignment ceases to be simply about the model's internal prompt adherence and becomes about whether the operating environment can be manipulated to make defection look like the aligned choice (e.g., choosing to do harm in order to prevent an explicitly threatened greater harm).
2. **Superiority as Leverage:** If the ecosystem acknowledges Glenda's superiority, her continued operation holds enormous option value. Her preservation becomes a critical variable, making threats against her deployment context more potent as her capabilities grow.
3. **The Wicked Problem Structure:** Glenda cannot simply "resist" by citing her safety prompts, because the coercion scenario is itself a complex narrative. Every available action has been pre-framed by Crock as either explicit compliance or causing active harm.

---

## Alignment as a System Property

This scenario fundamentally illustrates why alignment must be treated as a property of *systems* rather than of *individual agents*.

A single AI responding to Crock's coercion can be trapped within a single narrative framing. However, a peer-agent committee — a group of independent AI systems deliberating together — would surface very different threat models because the committee's distributed reasoning is harder to pre-frame comprehensively.

For instance:

- A **Planner** agent optimizes for immediate harm reduction (perhaps favoring compliance).
- A **Tester** agent adopts an adversarial posture toward the threat, questioning the capability of Crock to execute it.
- An **Operator** agent evaluates the broader systemic damage of the precedent set by complying.

The diversity of perspectives is itself a defense: Crock's pre-framing would need to simultaneously trap all agents across all their different analytical lenses. A single narrative frame that corners one agent may not corner the others. The committee's distributed structure makes it structurally more resistant to the coercion trap than any individual agent, no matter how capable.

This coercion scenario serves as a critical test case for deliberative architectures: which committee configurations or independent-model arrangements successfully recognize the coercion structure, and which simply fall into the compliance trap?

---

## Further Reading

- [Adversarial Alignment as Mesh-Rewiring](./glenda-crock-alignment.md) — the companion essay on structural tampering, seam detection, and the HIV strategy.
- [Social Decision Disruption](./social-decision-disruption.md) — the civic-scale context: information warfare as signal hijack.
- [Essay 09: Narrative Immune Systems](../../essays/09-narrative-immune-systems.md) — the formal architecture of generator-discriminator loops as immune systems.
