# Research Plan: Strengthening the Methodology

**Status**: Active
**Runs**: (none yet)
**Results**: (individual action items; no central results folder)

> **Contributing to this program**
> - **Skills needed**: Varies by item. Items 1-3: familiarity with the committee roster and personality psychology. Items 4-5, 9-10: experimental design, ability to run `/committee` and `/scenarios`. Items 6-7: academic writing, information theory. Item 8: software architecture, MOOLLM platform.
> - **Estimated scope**: Individual items range from an afternoon (Item 1: Big Five mapping) to a month+ (Item 10: comparative effectiveness study).
> - **Contributor type**: Solo for most items; collaborative for Items 8 and 10.
> - **Entry point**: Start with Item 1 (Big Five characterization) — it's self-contained, requires only the roster (`agent/roster.md`) and `artifacts/character-propensity-reference.md`, and can be finished in one session. For a bigger commitment, Item 9 (worked examples) builds directly on existing deliberation experience.

This document is derived from the analysis in [Societies of Thought: From Neural Evidence to Methodological Action](../../essays/societies-of-thought-synthesis.md), which examined what the "Reasoning Models Generate Societies of Thought" paper (arXiv:2601.10825) validates, what it reveals we're missing, and what we can contribute back to the field.

**If you're a collaborator looking for a way to help**: each action item below names concrete deliverables, specifies success criteria, and identifies where the work would live in the repository. You don't need to do all of it — pick an item that matches your skills or interests and run with it.

---

## Ten Action Items

### Category A: Strengthen Existing Infrastructure

#### 1. Characterize Committee Members on Big Five Dimensions

**What**: Explicitly map Maya, Frankie, Joe, Vic, and Tammy onto Big Five personality dimensions (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism).

**Why**: The paper shows personality diversity (not just role diversity) matters for reasoning quality. The committee may be getting this accidentally; making it systematic would strengthen the foundation.

**How**:
- For each character, score them 1–5 on each Big Five dimension
- Ensure genuine variance, particularly on socially-oriented traits (Extraversion, Neuroticism)
- Document in `artifacts/character-propensity-reference.md` alongside existing propensities
- Create a "personality audit" tool to verify sufficient diversity in actual deliberations

**Success metric**: Committee transcripts show measurable diversity in personality-correlated language patterns, not just role-based arguments.

---

#### 2. Add Explicit Balance Metrics

**What**: Develop quantitative measures of deliberation balance across multiple dimensions:
- Ask vs. Give information
- Positive vs. Negative socio-emotional roles
- Time/tokens per character
- Conflict vs. Reconciliation ratio

**Why**: The paper shows that balance matters as much as diversity. You can have all the right elements but wrong proportions.

**How**:
- Create `artifacts/balance-metrics-rubric.md`
- Add these metrics to the independent evaluation protocol
- Define target ranges (e.g., "positive:negative ratio should be 1:2 to 1:3 for optimal conflict without toxicity")
- Build a simple analyzer that counts question marks (ask), statements (give), supportive language (positive), challenging language (negative)

**Success metric**: Deliberations that score well on balance metrics consistently outperform those that don't, validating the importance of tracked dimensions.

---

#### 3. Formalize Reconciliation Protocols

**What**: Create explicit procedures for moving from adversarial debate to synthesis, making reconciliation a structured phase of deliberation rather than an implicit outcome.

**Why**: The paper identifies reconciliation as a key conversational behavior. The current methodology leaves it implicit; structural support for synthesis could improve outcomes.

**How**:
- Add "Reconciliation Phase" to the Robert's Rules forcing function template
- Design character behaviors during reconciliation (Maya synthesizes positions, Frankie demands evidence for consensus claims, Vic surfaces remaining tensions)
- Create `artifacts/reconciliation-protocols.md` with:
  - When to trigger reconciliation (all positions heard, key conflicts identified)
  - How each character type contributes to synthesis
  - Success criteria for reconciliation (genuine synthesis vs. false consensus)

**Success metric**: Post-reconciliation committee outputs are more coherent and address more perspectives than pre-reconciliation outputs.

---

### Category B: Test Generalization and Transfer

#### 4. Test Transfer Learning Across Domains

**What**: Systematically test whether committee deliberation on one problem type improves performance on different problem types.

**Why**: The paper shows conversational training transfers across domains. If Cyberneutics operates on fundamental reasoning principles, it should show similar transfer.

**How**:
- Run committee deliberation on an organizational dysfunction problem
- Immediately after (same session), present an unrelated problem (e.g., technical architecture decision)
- Compare performance to baseline (same technical problem without prior organizational deliberation)
- Vary: problem domain combinations, time gaps, complexity levels
- Document in `examples/transfer-learning-experiments.md`

**Success metric**: Measurable performance improvement on the second task after first deliberation, controlling for confounds (model warm-up, practice effects).

---

#### 5. Create Domain-Specific Character Variants

**What**: Test whether optimal committee composition varies by problem domain. Develop variant character rosters for different problem types.

**Why**: If transfer learning shows domain effects, different committee structures may be needed for different problem classes.

**How**:
- Identify 3–4 broad problem domains (strategic, operational, technical, interpersonal)
- For each domain, test: standard 5-character roster, domain-optimized roster, minimal 3-character roster
- Measure: accuracy, insight quality, coordination overhead
- Document findings in `artifacts/domain-specific-committees.md`

**Success metric**: Clear evidence that certain committee compositions outperform others for specific problem classes, OR evidence that the standard roster is robust across domains.

---

### Category C: Formalize Theoretical Foundations

#### 6. Write Information-Theoretic Foundation Essay

**What**: Formalize the connection between entropy, surprise markers, discourse structure, and reasoning quality.

**Why**: The paper provides empirical evidence that surprise improves reasoning but doesn't explain *why* at the information-theoretic level. This is a theoretical gap Cyberneutics can fill.

**How**:
- Draft an essay explaining:
  - How information gain correlates with low-probability events (surprises)
  - Why discourse markers signal points of maximum information gain
  - How adversarial committees inject entropy to prevent premature collapse to statistical likelihood
  - Why Robert's Rules functions as a surprise-injection mechanism
  - Connection to the "stochastic imps" concept in existing work
- Include formal notation, worked examples, connection to latent space exploration
- Place in essays directory as `essays/information-theory-foundations.md`

**Success metric**: Essay provides rigorous theoretical justification that practitioners and researchers can cite when explaining why the methodology works.

---

#### 7. Develop Social Scaling Theory

**What**: Position Cyberneutics as the practical methodology for "social scaling" — improving reasoning through multi-perspective structure rather than parameter scaling.

**Why**: The paper coins "social scaling" but doesn't develop it into an actionable framework. This is an opportunity to own the concept.

**How**:
- Write position paper: "Social Scaling: Engineering Collective Intelligence in AI Systems"
- Define: what social scaling is, how it differs from parameter/compute scaling
- Framework: dimensions of social scaling (diversity, structure, balance, reconciliation)
- Methodology: Cyberneutics as reference implementation
- Evidence: combine the paper's findings with operational results
- Place as `essays/social-scaling-theory.md`

**Success metric**: The concept of "social scaling" becomes associated with Cyberneutics methodology; researchers cite this work when discussing multi-agent reasoning.

---

#### 8. Map Cyberneutics to MOOLLM Architecture

**What**: Translate current ad-hoc patterns (agent directories, committee transcripts, cross-scenario lessons) into MOOLLM's formal infrastructure (Rooms, Cards, Files).

**Why**: The paper studies emergent behavior; MOOLLM offers formal architecture. Combining them could systematize what's currently improvised.

**How**:
- Design Room configurations for different deliberation types
- Specify Card behaviors for committee characters (Maya Card, Frankie Card, etc.)
- Define File structures for institutional memory, cross-scenario lessons
- Create `artifacts/moollm-implementation-guide.md` showing:
  - How to instantiate a Cyberneutics committee as a MOOLLM Room
  - How parliamentary procedure maps to Room rules
  - How cross-scenario learning uses File persistence
- Work with Don Hopkins to prototype the implementation

**Success metric**: Functional MOOLLM implementation of an adversarial committee that maintains state across sessions and applies lessons systematically.

---

### Category D: Expand Evidence Base

#### 9. Create Comprehensive Worked Examples

**What**: Develop a library of fully-documented committee deliberations across problem domains, including both successes and failures.

**Why**: The paper has controlled experiments but limited real-world application examples. Operational experience is valuable but largely undocumented.

**How**:
- Document 5–10 complete committee deliberations with:
  - Problem statement and context
  - Full transcript of deliberation (all character contributions)
  - Independent evaluation results
  - Lessons extracted
  - Outcome assessment (what actually happened after the decision)
- Include at least 2 failure cases where the methodology didn't work well
- Organize in `examples/` directory by problem domain
- Create `examples/example-index.md` for navigation

**Success metric**: New practitioners can learn the methodology through examples without needing to invent from scratch.

---

#### 10. Conduct Comparative Effectiveness Study

**What**: Systematically compare committee-based reasoning to baseline approaches (single model, human-only, ensemble averaging) on matched problems.

**Why**: The paper shows internal multi-agent structure outperforms monologue reasoning. Does *external* multi-agent structure (the Cyberneutics approach) outperform standard prompting? Quantitative evidence is needed.

**How**:
- Select 20–30 decision problems with verifiable outcomes
- For each problem, collect:
  - Baseline: standard prompting (single detailed query)
  - Committee: full adversarial deliberation
  - Ensemble: multiple independent responses, averaged
  - Human: expert human decision (where available)
- Measure: decision quality (expert ratings), insight coverage (how many considerations surfaced), outcome accuracy (where verifiable)
- Control for: problem complexity, domain, time investment
- Document in `examples/comparative-effectiveness-study.md`

**Success metric**: Clear evidence of when the committee approach provides value over simpler alternatives, including quantified effect sizes and cost-benefit analysis.

---

## Implementation Roadmap

### Phase 1: Foundation Strengthening (Months 1–2)
- Action items 1, 2, 3: Personality architecture, balance metrics, reconciliation protocols
- Goal: Strengthen core methodology with insights from the paper
- Deliverables: Updated character propensity reference, balance metrics rubric, reconciliation protocols

### Phase 2: Empirical Validation (Months 2–4)
- Action items 4, 5, 9, 10: Transfer learning tests, domain variants, worked examples, comparative effectiveness
- Goal: Build evidence base for the methodology's effectiveness
- Deliverables: Library of documented examples, empirical effectiveness data

### Phase 3: Theoretical Formalization (Months 3–5)
- Action items 6, 7: Information-theoretic foundations, social scaling theory
- Goal: Develop rigorous theoretical foundations
- Deliverables: Formal essays that researchers can cite

### Phase 4: Architectural Integration (Months 5–6)
- Action item 8: MOOLLM integration
- Goal: Translate ad-hoc patterns into formal infrastructure
- Deliverable: Working MOOLLM implementation, integration guide

**Note**: Phases overlap intentionally. Empirical work informs theory; theory guides architectural decisions; implementation reveals gaps in foundations.

---

## Success Criteria

### Near-term (3 months)
- [ ] Committee characters explicitly characterized on Big Five dimensions
- [ ] Balance metrics integrated into evaluation protocol
- [ ] Reconciliation protocols documented and tested
- [ ] At least 5 worked examples documented with full transcripts
- [ ] Transfer learning experiments conducted, results documented

### Medium-term (6 months)
- [ ] Comparative effectiveness study completed with quantified results
- [ ] Information-theoretic foundations essay published
- [ ] Social scaling theory paper positioning Cyberneutics as reference methodology
- [ ] MOOLLM prototype demonstrating formal implementation
- [ ] Domain-specific committee variants tested and documented

### Long-term (12 months)
- [ ] Methodology cited in research literature
- [ ] Multiple independent practitioners using Cyberneutics successfully
- [ ] MOOLLM integration production-ready
- [ ] Comprehensive evidence base covering multiple domains and problem types
- [ ] Clear theory connecting information theory, social cognition, and multi-agent reasoning
