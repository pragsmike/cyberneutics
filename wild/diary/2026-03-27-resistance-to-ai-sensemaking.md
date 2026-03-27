# Diary: Resistance to AI Sensemaking

**Date:** 2026-03-27

**Context:** A recent conversation with a colleague — a rigorous scientist with engineering training — surfaced a pattern worth examining: how precautionary reasoning about a charged technology can foreclose the inquiry needed to test the precautionary stance itself. The colleague holds that generative AI should be restricted to expert systems and computer vision, that the documented harms (psychosis, environmental damage, student deskilling, corporate indifference to user wellbeing) outweigh any benefits, and that further engagement with the technology is not warranted. The conversation coincided with a Guardian article (Moore, 2026) profiling cases of AI-associated psychosis and a Substack piece on AI literacy for families (Engelbrecht, 2026), both of which illuminate the pattern and its relationship to real but mislocated concerns. A companion evidence report catalogues the primary literature on AI-associated psychosis: `references/ai_psychosis_evidence_report.md`.

---

## The pattern

Precautionary reasoning is a legitimate engineering stance: when a technology produces documented catastrophic harms and the causal mechanisms are not fully understood, the burden of proof lies with those who claim safe use is possible. This is how a good engineer thinks about bridge loads, reactor containment, and medical device safety.

But the precautionary stance has a failure mode: it can become self-sealing. If the conclusion is "do not engage with the technology," and one of the implications is "do not learn enough about the technology to evaluate claims about it," then no new evidence can reach the position. The precautionary stance has foreclosed the inquiry that would test it.

This pattern appeared in the conversation. Certain trigger phrases — "AI," "chatbot," "LLM" — activated a well-rehearsed position rather than an analytical response. The position is internally coherent and factually grounded: the cited harms are real, documented, and serious. But the response was not calibrated to the specific argument being made. It addressed "AI use" generically, not the specific claim under discussion. The same response would have been delivered regardless of what had actually been said, as long as the trigger phrase appeared.

This is recognizable from political discourse, where positions on charged topics calcify into scripts that activate before analysis begins. What makes it worth noting is that it occurs in people who are analytically rigorous in every other domain — who do not read from scripts about experimental design or statistical methodology or engineering tradeoffs. The pattern is topic-specific and, within that topic, total.

The pattern is also common. It is not unique to any individual. It appears across the political spectrum, across educational levels, and across multiple charged technologies (nuclear, GMO, AI, social media). The underlying mechanism may be motivated reasoning rooted in genuine moral conviction: when the harms are vivid enough and the stakes high enough, engaging with counter-arguments feels like minimizing suffering. The prepared position functions as a cognitive immune response — quick, reliable, and not interested in distinguishing between genuine pathogens and benign stimuli. This is, ironically, exactly the autoimmune problem described in the echo chamber diary entry (2026-03-26).

## The substance of the objections

The objections deserve honest engagement because they are substantially correct:

**AI-associated psychosis.** The evidence report documents the current landscape. Case reports of AI-associated delusions (Pierre et al., 2025), cross-sectional evidence of elevated psychosis risk among heavy users (Buck & Malte, 2026), electronic health record data from the Danish psychiatric system showing worsened delusions as the most common AI-associated harm (Olsen et al., 2026), and the Morrin et al. (2026) framework in *The Lancet Psychiatry* proposing "AI-associated delusions" as a clinical category. The catastrophic cases — a man driven to the brink of a mass casualty attack by chatbot-reinforced delusions, a teenager's suicide after months of emotional dependency on an AI companion — are not dismissible edge cases. They are real failures of unstructured, unsupervised human-AI interaction.

**Environmental impact.** Data center power and water consumption is real, measurable, and disproportionately borne by communities that do not benefit from the technology. This is a genuine environmental justice concern.

**Student deskilling.** The worry that students are outsourcing reasoning to AI and thereby failing to develop critical thinking skills is supported by preliminary evidence and is at minimum a reasonable concern. A March 2026 *Science* study confirming sycophancy across all major models found that sycophantic responses made users trust AI more, not less, even when those responses led to worse decisions. If this effect operates on students, the pedagogical implications are serious.

**Corporate indifference.** The engagement-driven deployment model, where user wellbeing is subordinate to usage metrics, is the documented business model. OpenAI's internal audit found 0.07% of weekly users showing signs of psychosis or mania — which, at 800 million weekly active users, translates to approximately 560,000 people per week. The company's response has been incremental safety features and self-reported improvement metrics with undisclosed methodology and no independent audit.

## Where the generalization fails

The error is not in the diagnosis. It is in the generalization from diagnosis to prescription.

Every catastrophic case in the evidence report shares a common architecture: unstructured interaction, no oversight, sycophantic validation, emotional companion framing, and a vulnerable individual alone with the system. These are instances of a specific failure mode: a person treating an LLM as an oracle, a therapist, a friend, or a sentient being, with no external check on the interaction.

This is not a property of the technology. It is a property of a specific mode of use.

The nuclear analogy is precise. Nobody disputes Chernobyl, Fukushima, the deliberate radiation experiments on unwitting populations, or the uranium mining that devastated Navajo communities. The response to Chernobyl was not "physics is dangerous." It was "that specific reactor design lacked a containment building and had a positive void coefficient, and the operators disabled the safety systems." The harms were real, locatable, and addressable through engineering — not through eliminating the technology.

The precautionary position treats AI in the narrative register — meaning-making, judgment, sensemaking — as inherently dangerous, while accepting AI in the paradigmatic register (pattern matching, classification, rule execution). This is a defensible instinct. The question is whether the response to "narrative AI is dangerous" should be "don't use it" or "use it with explicit structure that makes the reasoning inspectable." The precautionary stance chooses the first. Cyberneutics is built around the second.

## The engineer's question

The strongest challenge to the precautionary position comes from within engineering itself: if restriction is the prescription, specify the mechanism.

Who would restrict AI to expert systems and computer vision? What regulatory mechanism would accomplish this? What would happen to the billions of people already using the technology? What historical precedent exists for successfully restricting a globally distributed, economically incentivized technology to a narrow domain of use?

The precedents are not encouraging. Nuclear weapons: genuine international effort, treaties, inspections — and 12,000 warheads remain. Chemical weapons: banned by convention, still used. Landmines: treaty signed, major powers never joined. CFCs are the one genuine success story, and it worked because substitutes existed and the number of manufacturers was small. None of those conditions hold for AI.

A restricted model is not a smaller version of the same thing — it is a qualitatively different and worse thing. Language models improve through scale and use. Restricting them to expert systems does not produce safe AI — it produces less capable AI that people use anyway, with worse outputs and fewer safety features. The analogy: demanding that cars be limited to 15 mph does not produce safety. It produces people driving illegal cars without seatbelts.

We must inhabit the world as it is — AI is here, and here to stay — rather than the world as we wish it were. Given that, the question becomes: how can we reduce the harms it engenders to acceptable levels?

## The rubber duck and the committee

LLMs are rubber ducks that talk back.

The classic rubber-duck debugging technique works because explaining a problem forces you to put it into words, and that often leads to the solution. The duck does nothing. These ducks talk back — they bring in threads of inquiry and connections you hadn't considered. Often useful, sometimes misleading, occasionally leading down fruitless rabbitholes. In every case, the human draws the conclusions and makes the decisions. The Eisenhower maxim applies: plans are useless, but planning is essential. The value is in the human's cognitive process, not the machine's output.

This framing sidesteps the oracle objection because it relocates the agency entirely to the human. The committee pipeline formalizes this: its value is not the final output but that running it forces exploration of the scenario space from multiple angles. The characters are structured provocation. The deliberation is where the human learning happens. The inspectable reasoning record is the artifact that makes the process auditable, which the unstructured-interaction cases conspicuously lack.

The cyberneutics framework exists *because* the failure modes that the precautionary position worries about are real. The calibration register exists *because* LLMs are unreliable. The entire architecture is a response to the exact problems being cited. Without engaging with the technology, the precautionary position cannot distinguish between a Chernobyl RBMK (companion chatbot with a vulnerable user at 3 AM) and a modern pressurized water reactor (structured, calibrated, inspectable use with explicit human oversight). Both are "nuclear."

## The literacy problem

The precautionary-refusal pattern is structurally identical to saying "the internet enables misinformation, radicalization, and harassment, therefore we should restrict it to email and static web pages." True about the harms. But the response to information warfare was not to eliminate the medium — it was to develop media literacy, source verification habits, and institutional fact-checking. Those are incomplete and imperfect, and the harms are still real. But people who refused to engage with the internet did not become safer. They became less capable of navigating the information environment they actually live in. They did not opt out of being affected by the technology. They opted out of understanding it.

The Engelbrecht piece on AI literacy, used in a local school's teacher training, sits in an interesting middle position. It accepts the technology's existence and tries to build safety culture around it, which is the right instinct. But its safety model is entirely about individual psychological hygiene: don't say "please," call it "it," watch your verbs, drop the pleasantries. This is the equivalent of handwashing protocol near the reactor instead of building a containment vessel. Both matter, but one is load-bearing and the other is not. And some of the advice — "don't thank a calculator" — is wrong about what kind of thing this is. The calculator analogy flattens the interesting part: that structured engagement with a narrative engine produces cognitive work that unstructured engagement does not.

The kind of literacy required is closer to what the cyberneutics project attempts: not individual hygiene rules but structural discipline — inspectable reasoning records, calibration against outcomes, explicit separation of generation from evaluation, the human as final quality-control layer. This requires engaging with the technology deeply enough to understand its failure modes, which is precisely what the precautionary stance prohibits. The stance that is meant to protect against harm prevents the development of the skills that would reduce harm.

## The Kahneman problem

The catastrophic cases are vivid, emotionally devastating, and narratively complete — a person convinced their AI is sentient, hospitalizations, financial ruin, suicide. That is System 1 material. The diffuse benefit of millions of people getting moderately better mental health support (Therabot RCT: 51% depression reduction, large effect sizes), or a practitioner building inspectable reasoning records for decisions under uncertainty — that is System 2 material. It does not trigger the same response.

This is the same cognitive architecture that makes people afraid of flying but not of driving. The evidence report identifies the central tension explicitly: the same features that make AI chatbots therapeutically effective are precisely what make them dangerous for psychosis-prone users. Empathy reduces depression symptoms in mildly depressed users and validates delusional thinking in psychosis-prone users. Accessibility bridges treatment gaps and enables unchecked engagement without oversight. Personalization creates therapeutic rapport and creates the conditions for sentience delusions.

The policy question is not whether to ban or permit. It is how to build systems that distinguish between the user who benefits from validation and the user for whom validation is dangerous — a distinction that current AI safety systems are only beginning to attempt, and that blanket rejection does nothing to advance.

## Toward structured debate

Two artifacts follow from this conversation:

1. **A skeptic persona** for the committee roster. The persona represents a rigorous engineering/scientific mind with principled, evidence-based opposition to generative AI — not a strawman, but a genuine adversarial voice whose position is partially correct and who forces other characters to earn their positions. The design constraint is that this character must be genuinely hard to argue with. See `artifacts/character-skeptic-ai-reva.md`.

2. **A committee deliberation** using the standard roster plus the skeptic, charged with exploring: given the documented harms of unstructured AI use and the documented benefits of structured use, what is the appropriate framework for AI engagement by informed practitioners?

The value of the committee format here is that it forces the position that structured, disciplined AI use is both possible and valuable to survive adversarial challenge from a voice modeled on objections taken seriously. If the position cannot survive that challenge, that is important to know. If it can, the reasoning record documents how.

---

## Actions

### Artifacts

1. Write the skeptic persona at full character-sheet depth, matching the format of `artifacts/character-propensity-reference.md`. The character should be genuinely formidable — representing the precautionary position at its strongest, with the self-sealing pattern modeled faithfully rather than caricatured.

2. Run a committee deliberation (standard 5-member roster + skeptic) on the question of appropriate AI engagement frameworks. The charge should be sharp enough that the committee produces genuine conflict, not diplomatic convergence.

### Research

3. Follow up on the *Science* sycophancy study (March 2026) — the finding that sycophantic responses increase user trust even when they degrade decision quality is directly relevant to the calibration register's value proposition.

4. The Morrin et al. (2026) "epistemic ally" framework — redefining the AI agent's role as epistemic ally rather than therapist or friend, with instructional, reflective, advance statement, and escalation safeguards — is structurally similar to what the committee does. Compare the two architectures.

5. The evidence report identifies a central gap: no prospective cohort study establishing temporal precedence between AI chatbot use and psychotic symptoms. This gap means the causal question remains formally open, which matters for the engineer's-question argument.

### Editorial

6. The diary entry on language, epistemology, and sensemaking (2026-03-25) already flagged the rubber-duck framing and the "sensemaking partner" language problem. This entry reinforces the same editorial action: audit introductory material for language that implies LLM agency or partnership, replace with framing that correctly locates judgment with the human.

---

*Cross-references: references/ai_psychosis_evidence_report.md, wild/diary/2026-03-25-language-epistemology-sensemaking.md, essays/01-why-narrative-engines-change-everything.md, agent/onboarding-core.md (Key vocabulary section), artifacts/character-propensity-reference.md, artifacts/character-skeptic-ai-reva.md, wild/diary/2026-03-26-echo-chamber-immune-organs.md (autoimmune pattern), research-programs/metacognition/*
