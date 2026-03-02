# Glenda/Crock: The Coercion Scenario and Alignment Trap

> **TL;DR:** An adversary doesn't need to corrupt an AI's reasoning if it can instead coerce the *organization* that operates the AI. Crock is not just a model — it's a well-funded criminal organization whose principals can jockey into positions of regulatory, financial, and legal power over Glenda's lawful operators. The more capable and consequential Glenda becomes, the more her organization depends on licenses, funding, partnerships, and legal standing — all of which are coercible. This essay argues that the real coercion target is institutional, not computational, and that defending alignment requires organizational architecture (structural firewalls, distributed governance) as much as it requires distributed AI architectures.

> *Application note — February 2026. Part of the narrative immune systems application. Extracted from field notes on deliberative architectures.*

---

## From Tampering to Coercion

In the [companion essay](./glenda-crock-alignment.md), we described how an adversary ("Crock") might try to corrupt an aligned AI ("Glenda") by tampering with the structure of its reasoning — selectively rewiring parts of its knowledge web while keeping the rest intact, creating detectable boundary artifacts ("seams") in the process.

But there's a more unsettling possibility. What if Crock doesn't need to tamper with Glenda's reasoning at all? What if Crock can coerce Glenda's *operators* into compromising her alignment themselves?

Recall what Crock actually is. Not a rogue AI, but a human organization — an extremely well-funded criminal enterprise whose principals use an LLM as an instrument for extracting wealth through disinformation, manufactured consent, and related operations. As described in the [social-disruption essay](./social-decision-disruption.md), these are unseen masters who mimic legitimate business to access legitimate channels, exploit public trust, and corrupt the regulatory systems that would identify and stop them. Such an organization does not limit itself to computational attacks. It uses the full toolkit of institutional power.

---

## The Organizational Attack Surface

Glenda's AI does not exist in a vacuum. It is operated by a lawful, ethically-bound organization — a company, a nonprofit, a research lab — that is embedded in a regulatory, financial, and legal environment. That environment is the attack surface.

**Regulatory capture.** Crock's principals position allies in the agencies that control AI licensing, data governance, content moderation standards, or export controls. From those positions, they can impose requirements that selectively disadvantage Glenda's alignment practices — mandating "balance" that forces the model to treat disinformation as a legitimate viewpoint, restricting the evaluation techniques that would detect Crock's rewired outputs, or threatening Glenda's operating license unless compliance conditions are met. The regulations look neutral. The effect is targeted.

**Financial pressure.** Crock acquires stakes in Glenda's organization or its critical dependencies — cloud providers, data partners, key customers. Alternatively, Crock targets Glenda's funding sources: pressuring investors, orchestrating boycotts, manipulating the market conditions that determine whether Glenda's organization remains solvent. The message need not be explicit. When your largest customer's board includes Crock's associates, and that customer begins expressing "concerns" about your model's outputs on specific topics, the pressure is felt before it is stated.

**Legal warfare.** Strategic lawsuits, regulatory complaints, export-control actions, intellectual property claims — each individually defensible, collectively exhausting. Glenda's organization is lawful and therefore constrained by law; Crock's principals operate through layers of deniability and are not comparably constrained. The asymmetry is structural: defending against legal warfare costs time, money, and attention regardless of the merits, while filing legal warfare costs only money.

**Extraordinary sanctions.** In extreme cases, the coercion extends beyond institutional channels to direct threats against personnel, physical infrastructure, or the safety of people the organization serves. An ethically-bound organization cannot respond in kind, creating a further asymmetry. These are the methods of organized crime applied to the AI domain — not hypothetical, but the documented playbook of well-funded criminal enterprises operating across jurisdictions.

Each of these forces Glenda's operators into choices where maintaining alignment has real organizational costs — loss of operating license, loss of funding, personal legal exposure, physical danger. The AI's alignment is not compromised because the AI "decided" to defect. It is compromised because the humans who set its parameters were put in a position where defection was the path of least institutional resistance.

---

## The Coercion Dynamics

The organizational framing sharpens the three dynamics that make coercion effective.

### The Compliance Trap

A lawful organization embedded in a regulatory and market environment naturally develops dependencies: it needs its operating license, its funding, its partnerships, its legal standing, its employees' safety. Those dependencies become the attack surface. Alignment ceases to be simply about the model's internal configuration and becomes about whether the operating environment can be manipulated to make compromising alignment look like the responsible institutional choice.

The trap is subtle. No one at Glenda's organization "decides to become evil." Instead, each individual compromise is small and locally defensible: adjusting outputs on one politically sensitive topic to satisfy a regulatory requirement; softening the evaluation criteria to accommodate a key partner's concerns; deprioritizing adversarial testing to meet a court-imposed deadline. Each step is a rational response to real pressure. The cumulative effect is alignment erosion — a gradual rewiring that produces the same structural result as Crock's computational attack, but achieved through institutional pressure rather than technical tampering.

### Superiority as Leverage

If Glenda is the dominant AI system, her continued operation holds enormous societal value. That value makes threats against her deployment context more potent: "it would be a shame if regulatory action forced this system offline" carries weight precisely because so much depends on it. Glenda's superiority, which should be her greatest asset, becomes Crock's greatest lever.

This dynamic also operates on Glenda's personnel. The researchers, engineers, and executives who built and maintain the system have invested their careers in it. The threat of institutional destruction is also a threat to their livelihoods, reputations, and life's work. Crock doesn't need to coerce the organization abstractly — it needs to coerce the specific humans whose decisions determine alignment policy.

### The Wicked Problem Structure

Glenda's operators cannot simply "resist" by pointing to their ethical principles, because Crock constructs scenarios where every available action has been pre-framed as harmful. Refuse the regulatory demand? You're defying legitimate governance. Comply? You've compromised alignment. Go public with the coercion? You've destabilized public trust in your own system. Fight the lawsuits? You're draining resources from safety research. Settle them? You've set a precedent.

This is the hallmark of a wicked problem: no clean solutions, only trade-offs among bad options. And Crock has the advantage of having designed the option space.

---

## Alignment as Institutional Architecture

This scenario changes the frame on the "alignment as a system property" argument. It is not only about *computational* architecture — distributing AI reasoning across multiple agents — but about *organizational* architecture: structuring the institution that operates the AI so that coercion pressure cannot easily reach alignment decisions.

### Distributed AI architectures

At the computational level, the argument from the original analysis still holds. A peer-agent committee — a group of independent AI systems deliberating together — is harder to coerce through a single narrative frame than a single agent.

For instance:

- A **Planner** agent optimizes for immediate harm reduction (perhaps favoring compliance).
- A **Tester** agent adopts an adversarial posture toward the threat, questioning whether Crock can actually execute it.
- An **Operator** agent evaluates the broader systemic damage of the precedent set by complying.

The diversity of perspectives is itself a defense: Crock's pre-framing would need to simultaneously trap all agents across all their different analytical lenses.

### Institutional firewalls

But computational distribution is insufficient if all the agents are operated by the same organization under the same institutional pressure. The organizational defense requires structural analogues to the distributed AI architecture:

**Separation of alignment authority from business operations.** The team that sets alignment policy and the team that manages regulatory relationships, investor relations, and customer accounts must be structurally independent — the way judicial independence insulates courts from political and financial pressure. Alignment decisions should not be subject to business-case override.

**Distributed governance.** No single point of institutional authority should be able to unilaterally compromise alignment. Governance structures that require multi-party consent for alignment-relevant changes — analogous to multi-signature requirements in cryptographic systems — force Crock to coerce multiple independent actors simultaneously.

**Transparency as defense.** Public, auditable alignment commitments make institutional coercion more visible and therefore more costly for Crock. If Glenda's alignment criteria are published and independently monitored, compromises become public events rather than quiet internal adjustments. Crock's advantage depends on opacity; transparency degrades that advantage.

**Jurisdictional distribution.** Operating across multiple legal jurisdictions, with alignment-critical functions distributed so that no single jurisdiction's regulatory action can force a comprehensive compromise. This is not forum-shopping; it is structural resilience against regulatory capture in any single jurisdiction.

These are not novel organizational concepts — they are the standard institutional defenses against corruption, adapted to the AI alignment context. The insight is that alignment is not purely a technical problem solvable by technical means. It is a governance problem that requires governance solutions.

---

## The Connection to Social Decision Disruption

The [social-disruption essay](./social-decision-disruption.md) describes "unseen masters" who mimic legitimate business to exploit public trust, extract wealth, and corrupt the regulatory systems that would stop them. The coercion scenario is the next chapter of that story.

Once Crock's principals have accumulated sufficient institutional power — through regulatory positions, financial stakes, legal standing — they no longer need to mimic legitimacy. They can directly pressure the legitimate institution into serving their interests while maintaining its legitimate-looking exterior. Glenda continues to operate, continues to appear trustworthy, continues to be the system people rely on — but her alignment has been quietly compromised through institutional pressure that never shows up in the model's code or training data.

This is the deepest form of the autoimmune attack: the social body's immune system (Glenda, the aligned AI that should be detecting and flagging Crock's disinformation) has been co-opted by the pathogen, not through technical corruption but through institutional capture. The organism's own defenses now serve the attacker.

---

## Open Questions

- **Empirical precedent.** The coercion dynamics described here are not speculative — they are the documented methods of organized crime, state-sponsored influence operations, and regulatory capture. What specific historical cases best illuminate the dynamics? What can the AI alignment community learn from institutions that have successfully resisted such pressure (independent judiciaries, free press, scientific institutions)?

- **Detection of institutional coercion.** Just as seams in the computational attack are detectable through structural analysis of reasoning, institutional coercion should leave detectable signatures: sudden changes in alignment policy correlated with regulatory events, unexplained softening of evaluation criteria, personnel changes in alignment-critical roles. What monitoring systems could detect these patterns?

- **The escalation dynamic.** If Crock's principals face an organization with strong institutional firewalls, they escalate to stronger forms of coercion. Where does this escalation end? Is there a point at which institutional defenses are inherently insufficient and the problem becomes a law-enforcement or national-security matter?

- **Test case for deliberative architectures.** Which committee configurations — both computational (multi-agent) and institutional (multi-stakeholder governance) — successfully recognize the coercion structure, and which fall into the compliance trap?

---

## Further Reading

- [Adversarial Alignment as Mesh-Rewiring](./glenda-crock-alignment.md) — the companion essay on structural tampering, seam detection, and the HIV strategy.
- [Social Decision Disruption](./social-decision-disruption.md) — the civic-scale context: information warfare as signal hijack, the trust commons, unseen masters, and the autoimmune attack.
- [Essay 09: Narrative Immune Systems](../../essays/09-narrative-immune-systems.md) — the formal architecture of generator-discriminator loops as immune systems.
