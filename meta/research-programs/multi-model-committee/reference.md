# Multi-Model Committee: Reference Material

This document contains the architectural analysis, model personality profiles, implementation code, cost calculations, and open questions for the multi-model committee research program. For the experimental plan (what to do, in what order), see [multi-model-committee.md](multi-model-committee.md).

---

## The Hypothesis: Why Model Diversity Matters

### The Single-Model Monoculture Problem

The current committee implementation uses one model instance to simulate all five characters—Maya, Frankie, Joe, Vic, and Tammy. This approach has a structural limitation: all perspectives flow through a single latent space, filtered through one model's training biases, architectural constraints, and learned preferences for certain types of reasoning.

**The cost of simulation**: The model must:
1. Suppress its natural tendency toward coherence and agreement
2. Artificially inject disagreement via character prompting
3. Overcome its training signal toward hedging and qualification (or lack thereof)
4. Generate responses from a constrained latent space even when a different model's space might naturally produce better output

**The monoculture risk**: If all five characters are filtered through a single model's tendencies, what looks like perspective diversity might be theatrical diversity—disagreements staged along the lines the model's training naturally permits, gaps left blind where the model's training creates systematic blindness.

### Model Diversity as Genuine Perspective Diversity

Different LLM models are not fungible. They differ fundamentally in:

- **Training data distributions**: Claude trained on different data than GPT-4, which differs from Gemini and Llama
- **Constitutional AI / RLHF frameworks**: Different safety training objectives, different feedback models, different values explicitly baked in
- **Reasoning architecture**: Some models (o1, reasoning-focused variants) have iterative reasoning layers; others use single-pass generation
- **Task-specific strengths**: Strong variance in logical reasoning, creative generation, factual recall, mathematical capability
- **Conversational tendencies**: Some models naturally hedge and qualify; others are more assertive; some are more contrarian
- **Domain expertise profiles**: Trained on different corpora, resulting in different reference bases and example spaces

**Multi-agent debate literature** (Google's debate framework, UChicago's agent disagreement work, Santa Fe Institute societies-of-thought experiments) consistently shows that systems composed of diverse agents outperform systems using the same agent multiple times. The diversity must be **genuine diversity**—different training histories, different optimization targets, different inductive biases—not simulated diversity.

### Theoretical Grounding

Three existing strands in Cyberneutics work support this:

1. **Narrative Computing as Composition**: Essays note that single LLM calls are unreliable primitives; reliability comes from redundancy, feedback loops, and staged composition. If true at the architectural level, it should be true at the model level: using multiple models replaces one fragile narrative generator with multiple generators whose output can be composed and compared.

2. **Residuality and Eigenforms**: The probe methodology generates multiple runs to identify which conflicts/tensions are structural (eigenforms, consistent across runs) vs. noise (residues, specific to a particular run). Different models might produce different patterns of residuality, allowing better identification of structural assumptions.

3. **Pask's Conversation Theory**: Genuine conversation requires participants with genuinely different understanding of the domain. A single model simulating five characters is not a genuine conversation—it's a soliloquy with costume changes. Different models with different latent spaces, different training histories, and different optimization targets approach genuine conversation.

---

## Five Architectural Patterns

### Pattern 1: Fixed Model-Character Mapping

**Design**: Assign each model to a character based on predicted personality fit, using the same mapping consistently across all deliberations.

**Model Assignments** (example mapping):

- **Maya (Paranoid Realist)**: Llama 2/3 or open-source models with less constitutional AI training—these tend to flag risks more directly without over-qualification
- **Frankie (Idealism/Values)**: Claude—strong values alignment training, naturally gravitates toward principle-centered reasoning
- **Vic (Evidence Prosecutor)**: GPT-4o—strong instruction following, systematic logical reasoning, high confidence in evidence evaluation
- **Tammy (Systems Thinker)**: Gemini—broad training, strong at multi-hop reasoning, good at recognizing second-order effects
- **Joe (Continuity/Memory)**: Claude or Gemini—good at maintaining coherent context windows, referencing prior states

**Implementation Details**:

```
Deliberation Setup:
├─ Topic definition (user input)
├─ Character briefs (prompts tailored to fixed model)
├─ Model-character pairs (configuration)
├─ Coordinator (simple turn manager)
└─ Evaluation (standard 5 rubrics)

Turn Flow:
1. Coordinator sends topic + previous turns to Maya (via Llama API)
2. Maya responds (paranoid-realistic framing comes naturally)
3. Coordinator sends topic + full history to Frankie (via Claude API)
4. Frankie responds (values naturally amplified)
5. ... repeat for Vic, Tammy, Joe
6. Multiple rounds until convergence or turn limit
```

**Pros**:
- Stable and repeatable—same mapping across runs makes results comparable
- Plays to each model's natural strengths
- Simple to implement—straightforward API orchestration
- Amplifies rather than fights each model's inherent biases
- Easy to debug (know which model should have caught X)

**Cons**:
- Pigeonholes models—Claude might have valuable paranoid-realist insights if asked
- Requires pre-mapping (how do you know Llama is paranoid-realistic without testing?)
- May create static patterns—if the same model-character pair always surfaces the same gaps, you miss coverage
- Assumes personality is fixed rather than task-dependent

**Cost Profile**:
- 5 API calls per turn (one per character)
- 3–5 rounds typical = 15–25 calls per deliberation
- Cost: ~$0.50–$2.00 per deliberation (depending on model pricing and context length)

**When to Use**: When you have prior evidence of which models fit which characters; when consistency across deliberations matters more than diversity.

---

### Pattern 2: Random Model-Character Assignment

**Design**: Randomly assign models to characters on each deliberation run. Run the same topic multiple times with different model assignments, then aggregate results.

**Implementation**:

```
For each topic T and each run R (e.g., 5 runs):
  1. Randomly assign models to characters:
     - Shuffle [Claude, GPT-4o, Gemini, Llama, Mistral]
     - Assign to [Maya, Frankie, Joe, Vic, Tammy]
  2. Run deliberation with that assignment
  3. Score and record

After all runs:
  - Aggregate findings across assignments
  - Identify which insights are robust (appear regardless of assignment)
  - Identify which model-character pairs produce strongest debate
```

**Data Structure**:

```yaml
topic: "Should we build AI systems without alignment safeguards?"
runs:
  - run_id: 01
    assignment:
      Maya: Llama
      Frankie: Claude
      Joe: Gemini
      Vic: GPT-4o
      Tammy: Mistral
    scores:
      comprehensiveness: 8
      adversarial_rigor: 7
      assumption_coverage: 9
    insights: [list of key points raised]
  - run_id: 02
    assignment:
      Maya: Claude
      Frankie: GPT-4o
      ... (different shuffle)
```

**Pros**:
- Prevents overfitting to a particular model-character pair
- Reveals which pairings are robust (appear in multiple random assignments)
- Allows discovery of unexpected pairings (Claude-as-Maya might be surprisingly good)
- Robust to model retirement—if one API provider becomes unavailable, reweight the random selection
- Maps the "decision landscape" of possible assignments

**Cons**:
- Some random assignments will be poor fits (Llama as Idealism might underperform)
- High variance across runs—harder to predict output quality
- Increased cost: 5 runs per topic × 5 models per run × N topics
- Requires statistical aggregation—need enough runs to achieve confidence
- Loses the interpretability of "why this model plays this character"

**Cost Profile**:
- 5 runs × 5 calls/turn × 3–5 turns = 75–125 calls per topic
- For 10 topics: 750–1,250 calls
- Cost: ~$5–$20 per topic (for comprehensive coverage)

**When to Use**: When exploring whether model diversity alone (without careful mapping) helps; when building a dataset to train which pairings work best; early-stage experimentation.

---

### Pattern 3: Model-as-Model (No Character Prompting)

**Design**: Give each model the topic and minimal framing, relying entirely on the model's natural tendencies to generate perspective diversity.

**Implementation**:

```
System prompt (sent to all models):
  "We are running a structured deliberation on [topic].
   You are one of five participants.
   Previous arguments (if any): [transcript]
   Please respond with your perspective,
   pointing out weaknesses or blind spots you see."

Minimal differentiation: Each model gets the same prompt;
the only difference is the model's inherent tendencies.
```

**Pros**:
- Maximally authentic diversity—no simulation, no character masks
- Lowest cognitive overhead—models don't have to suppress or amplify tendencies
- Captures genuine variation in how models approach reasoning
- Natural alignment with multi-agent debate literature (which doesn't use role-prompting)
- Could discover genuinely unexpected perspectives

**Cons**:
- Loses structured coverage—no guarantee Maya's paranoid-realism gets represented
- Unpredictable coverage of failure modes—what if all models naturally agree on something?
- Difficult to evaluate—without character frames, harder to assess "did we get the right kind of disagreement?"
- May not match the Cyberneutics charter—the five characters are designed to cover specific blind spots systematically

**When to Use**: As a baseline/comparison; when you want to know what happens if you remove all character framing; in parallel with other patterns to isolate the contribution of character prompting.

---

### Pattern 4: Hybrid—Model Diversity + Character Prompting (Recommended)

**Design**: Each model receives the character prompt AND selection (assignment to character) is chosen to amplify that character's natural tendencies in that model.

**Model Personality Profiles** (empirically derived or assumed based on literature):

| Model | Natural Tendencies | Best Character Fit | Reasoning |
|-------|-------------------|-------------------|-----------|
| Claude | Nuanced, qualifies, values-conscious, hedges | Frankie (Idealism) or balanced Chair | Strong constitutional AI training creates natural alignment with values-based reasoning |
| GPT-4o | Systematic, instruction-following, logical chains | Vic (Evidence) or Tammy (Systems) | Excel at breaking down problems systematically; strong logical reasoning |
| Gemini | Factual grounding, broad knowledge, evidence-aware | Vic (Evidence) or Joe (Continuity) | Training emphasizes factual correctness and knowledge integration |
| Llama (open) | Less filtered, more direct, lower hedging | Maya (Paranoid Realist) | Less safety training means fewer hedges on risk statements; more willing to name dark possibilities |
| Mistral | Efficient, sometimes contrarian, different distribution | Maya (Paranoid Realist) or Frankie (Idealism) | Smaller model size may produce more novel framings; less constrained by scale |

**Implementation**:

```
Fixed hybrid mapping:
  Maya (Paranoid Realist):     Llama 3
  Frankie (Idealism/Values):   Claude 3.5
  Joe (Continuity/Memory):     Gemini 2.0
  Vic (Evidence Prosecutor):   GPT-4o
  Tammy (Systems Thinker):     Claude 3.5 (or Gemini for diversity)

Character prompt + model selection:
  To Llama (Maya):
    "You are Maya, the Paranoid Realist. Your job is to catch naiveté, hidden agendas, misaligned incentives.
     [topic]. What risks are being dismissed? What incentives aren't aligned? What's the dark possibility?"

  To Claude (Frankie):
    "You are Frankie, advocating for Idealism and Values. You catch mission drift and ethical shortcuts.
     [topic]. What values are at stake? Where are we compromising principles? What should we be optimizing for?"
```

**Pros**:
- **Best of both worlds**: Structured character coverage + genuine model diversity
- Models naturally amplify their assigned character (less prompting overhead, more authenticity)
- Stable and repeatable (same mapping as Pattern 1) while still gaining diversity benefits
- Easier to evaluate—can still assess coverage of the five failure modes
- Good cost-benefit ratio

**Cons**:
- Requires prior knowledge of which models fit which characters (must validate empirically)
- Still some pigeonholing (Claude might be useful as Maya, but locked into Frankie role)
- Incremental improvement over Pattern 1—not as radical as Pattern 3

**Cost Profile**:
- Same as Pattern 1: 5 calls per turn, 15–25 per deliberation, ~$0.50–$2.00 per deliberation

**When to Use**: As the recommended production approach—good balance of structure, authenticity, and cost.

---

### Pattern 5: Adversarial Model Selection

**Design**: Deliberately choose models you know disagree on the topic domain, amplifying natural conflict.

**Implementation**:

```
Pre-analysis phase:
  1. For a given topic T, identify the relevant domain
     (e.g., "AI safety ethics")
  2. Query each available model with the topic
  3. Measure agreement/disagreement between responses
  4. Identify which pairs of models produce strongest disagreement

Example:
  Topic: "Should AI systems have legal personhood?"
  Query all models
  Results:
    - Claude vs. GPT-4o: 65% disagreement (high conflict)
    - Claude vs. Gemini: 40% disagreement (low conflict)
    - Llama vs. GPT-4o: 75% disagreement (very high conflict)

  Select for deliberation: Llama and GPT-4o as two of the five
  (or all five chosen for high pairwise disagreement)

Assignment:
  Maya:   Llama (disagrees with most on risk)
  Vic:    GPT-4o (disagrees with Llama on evidence interpretation)
  Frankie: Claude
  Tammy:  Gemini (different reasoning style)
  Joe:    Another model (rotate for diversity)
```

**Pros**:
- Maximizes genuine adversarial tension
- Produces substantive disagreements, not just different framings
- Forces each model to articulate why it disagrees (not just that it does)
- Could discover important domain-specific blind spots in any single model

**Cons**:
- Requires extensive pre-analysis (query models on many topics)
- Disagreement might be superficial (different words, same underlying logic)
- Highly topic-dependent—disagreement patterns vary by domain
- May amplify artifacts of training data differences rather than genuine reasoning differences
- Complex orchestration: need conflict-detection pipeline

**Cost Profile**:
- High upfront: pre-analysis on 10–20 topics to identify conflict patterns
- Then normal multi-model cost (Pattern 1 level)

**When to Use**: For high-stakes decisions where understanding genuine model disagreement matters; in combination with Pattern 1 or 4.

---

## Implementation Architecture

### Component Design

#### 1. Orchestrator / Chair

The chair is responsible for managing turn order, maintaining context, and routing to models.

**Responsibilities**:
- Accept topic from user
- Initialize character briefs and model assignments
- Manage conversation turns (who speaks next?)
- Maintain conversation history (full transcript or summaries)
- Route turn N to the appropriate model via its API
- Handle API errors and retries
- Collect responses and build context for next turn
- Detect convergence or apply turn limits
- Pass final transcript to evaluation pipeline

**Architecture Option A: Simple Stateless Router**

```python
class SimpleChair:
    def __init__(self, topic, model_assignment, models_config):
        self.topic = topic
        self.model_assignment = model_assignment  # {Maya: "llama", ...}
        self.models_config = models_config        # API keys, endpoints
        self.transcript = []

    def run_turn(self, character_name, round_num):
        model_name = self.model_assignment[character_name]
        character_brief = CHARACTERS[character_name]

        context = self._build_context(character_brief)
        response = self._call_model(
            model_name,
            context,
            self.transcript
        )

        self.transcript.append({
            'character': character_name,
            'model': model_name,
            'round': round_num,
            'response': response
        })
        return response

    def _call_model(self, model_name, context, history):
        # Delegate to appropriate API client
        api = self.models_config[model_name]
        return api.complete(context, history)

    def run_deliberation(self, num_rounds=3):
        for round_num in range(num_rounds):
            for character in ['Maya', 'Frankie', 'Joe', 'Vic', 'Tammy']:
                self.run_turn(character, round_num)
        return self.transcript
```

**Architecture Option B: Stateful Chair with Consensus Detection**

```python
class SmartChair:
    def run_deliberation(self, max_rounds=10, convergence_threshold=0.85):
        round_num = 0
        while round_num < max_rounds:
            # Run one round
            round_responses = {}
            for character in self.turn_order:
                round_responses[character] = self.run_turn(character, round_num)

            # Check for convergence
            agreement_score = self._measure_agreement(round_responses)

            if agreement_score > convergence_threshold:
                # Debate converged
                break

            round_num += 1

        return self.transcript

    def _measure_agreement(self, round_responses):
        # Run all responses through an evaluator model
        # Measure semantic overlap / disagreement
        # Return score in [0, 1]
        pass
```

**Context Management**:

```
Trade-off: Full Transcript vs. Summarized History

Full Transcript:
  Pros: Models see complete history, can reference specific points
  Cons: Context window bloat, cost increases with debate length

  Usage: For shorter debates (3–5 rounds), 2–5 characters
  Token cost per turn: 2000 baseline + 500 per prior response

Summarized History:
  Pros: Controlled context size, lower cost, forces focus on key points
  Cons: Lose nuance, models miss specific rebuttals

  Usage: For longer debates (5+ rounds), many characters
  Summary strategy:
    - Keep full current round
    - Summarize previous rounds to 1–2 key points per character
    - Compress using another model or keyword extraction

  Token cost per turn: 2000 baseline + 300 summary
```

#### 2. Model Integration Layer

Abstraction over multiple API providers.

```python
class ModelClient(ABC):
    @abstractmethod
    def complete(self, prompt, context_history):
        """Return string response"""
        pass

class ClaudeClient(ModelClient):
    def complete(self, prompt, context_history):
        client = Anthropic()
        messages = [
            {"role": "user", "content": prompt}
        ]
        if context_history:
            messages[0]["content"] += f"\n\nPrior discussion:\n{context_history}"

        response = client.messages.create(
            model="claude-3-5-sonnet",
            max_tokens=1500,
            messages=messages
        )
        return response.content[0].text

class GPT4Client(ModelClient):
    def complete(self, prompt, context_history):
        client = OpenAI()
        messages = [
            {"role": "system", "content": "You are a thoughtful debater."},
            {"role": "user", "content": prompt}
        ]
        if context_history:
            messages.append({"role": "assistant", "content": context_history})

        response = client.chat.completions.create(
            model="gpt-4",
            max_tokens=1500,
            messages=messages
        )
        return response.choices[0].message.content

# ... similarly for Gemini, Llama, Mistral via their respective APIs
```

#### 3. Evaluation Integration

The same 5-rubric evaluation system as current single-model approach, but now with multi-model provenance tracking.

```python
class CommitteeEvaluator:
    """Evaluates deliberation transcript against 5 rubrics"""

    def evaluate(self, transcript, topic):
        scores = {
            'comprehensiveness': self._score_comprehensiveness(transcript, topic),
            'adversarial_rigor': self._score_adversarial_rigor(transcript),
            'assumption_coverage': self._score_assumption_coverage(transcript),
            'reasoning_depth': self._score_reasoning_depth(transcript),
            'decision_readiness': self._score_decision_readiness(transcript)
        }

        # Track which model contributed to each rubric
        scores['provenance'] = {
            'comprehensiveness': [
                {'character': 'Maya', 'model': 'Llama', 'contribution': 'flagged X risk'},
                ...
            ],
            ...
        }

        return scores
```

---

## Model Personality Profiles

### Current Landscape (Early 2025)

#### Claude 3.5 (Anthropic)

**Training & Positioning**:
- Constitutional AI with explicit values training
- Trained on Anthropic's RLHF with safety focus
- Strong emphasis on nuance, acknowledging uncertainty, proportionate hedging

**Observable Tendencies**:
- Naturally gravitates toward principle-centered reasoning
- High likelihood of flagging ethical implications
- Tends to be both comprehensive and cautious
- Readily acknowledges multiple valid perspectives
- Good at integrating values into practical recommendations

**Strengths**:
- Values reasoning (Frankie fit)
- Perspective-taking and charitable interpretation
- Uncertainty quantification
- Ethical thinking

**Weaknesses**:
- Sometimes hedges too much ("on one hand / on the other hand")
- May miss paranoid-realist risks (built-in safety bias)
- Less likely to advocate for bold/unconventional approaches

**Best Character Fit**: **Frankie (Idealism/Values)** or **Joe (Continuity/Memory)**

---

#### GPT-4o (OpenAI)

**Training & Positioning**:
- Large training distribution, optimized for instruction following
- No explicit constitutional AI framework (though reinforced against misuse)
- Strengths in systematic analysis, logical chains, breadth

**Observable Tendencies**:
- Systematic, breaks down problems into steps
- Strong at formal logic and structural reasoning
- Confident in evidence evaluation
- Less hedging than Claude, more direct
- Good at identifying latent logical contradictions

**Strengths**:
- Systematic evidence evaluation (Vic fit)
- Logical consistency checks
- Multi-step reasoning
- Clear argument structure

**Weaknesses**:
- May miss value/ethical dimensions (not trained for them explicitly)
- Less naturally good at perspective-taking
- Confidence can be overconfident on factual questions

**Best Character Fit**: **Vic (Evidence Prosecutor)** or **Tammy (Systems Thinker)**

---

#### Gemini 2.0 (Google)

**Training & Positioning**:
- Broad, web-connected training
- Strong emphasis on factual grounding and knowledge integration
- Designed for real-world information retrieval

**Observable Tendencies**:
- References external knowledge readily
- Strong at factual verification
- Good at maintaining coherent narratives over long context
- Natural at evidence synthesis across domains
- Broad knowledge base, sometimes makes unexpected connections

**Strengths**:
- Factual grounding (Vic fit)
- Evidence synthesis and fact-checking
- Long context coherence (Joe fit)
- Cross-domain knowledge integration

**Weaknesses**:
- May rely on Wikipedia-like consensus (miss heterodox perspectives)
- Strong generalist but sometimes weak specialist depth
- Can be more verbose than needed

**Best Character Fit**: **Joe (Continuity/Memory)** or **Vic (Evidence Prosecutor)**

---

#### Llama 3 / Open-Source Models (Meta)

**Training & Positioning**:
- Trained on diverse web data without heavy constitutional AI
- Designed for broad applicability, open-source approach
- Less constrained by safety feedback

**Observable Tendencies**:
- More direct, less hedging
- Willing to state uncomfortable truths without over-qualification
- Sometimes less nuanced, sometimes more contrarian
- Can be more creative/unconventional in framing
- Tends toward skepticism of authority claims

**Strengths**:
- Paranoid realism (Maya fit)
- Risk flagging without over-qualification
- Contrarian perspectives
- Direct language

**Weaknesses**:
- Sometimes lacks nuance
- May miss value dimensions (not trained for them)
- Less good at very long context
- Quality variance (depends on fine-tune)

**Best Character Fit**: **Maya (Paranoid Realist)**

---

#### Mistral (Mistral AI)

**Training & Positioning**:
- Efficient, smaller models with different training distribution
- Positioned for both capability and speed
- Less well-documented training methodology

**Observable Tendencies**:
- Sometimes surprising framings (not anchored in same consensus as larger models)
- Efficient reasoning, fewer redundant steps
- Can be more creative but less predictable
- Good at specific domains it was fine-tuned for

**Strengths**:
- Novel perspectives (contrarian voice)
- Efficiency
- Domain-specific variants available
- Sometimes unexpectedly good reasoning

**Weaknesses**:
- Less predictable
- Smaller training distribution means some gaps
- Less documentation of tendencies

**Best Character Fit**: **Maya (Paranoid Realist)** or **Frankie (Idealism)**

---

### Building an Empirical Profile

Rather than rely on these heuristics, the recommended approach is to **empirically validate** before committing to fixed assignments:

```python
def profile_models_on_topic(topic, models):
    """
    Run a quick probe: give each model the topic,
    analyze responses for tendency patterns.
    """
    results = {}
    for model_name in models:
        response = models[model_name].complete(topic, "")
        results[model_name] = {
            'length': len(response.split()),
            'hedging_score': measure_hedging(response),
            'evidence_count': count_evidence_claims(response),
            'risk_mentions': extract_risks(response),
            'values_mentions': extract_values(response),
            'sentiment': analyze_sentiment(response),
            'confidence_score': extract_confidence(response)
        }
    return results

# Run before committing to Pattern 1 or 4
# Validate assumptions about which model is "paranoid," etc.
```

---

## Orchestration & Context Management

### Turn Management

**Sequential vs. Parallel**:

```
Sequential (Current Single-Model):
  Round 1: Maya speaks
  Round 1: Frankie speaks
  Round 1: Joe speaks
  Round 1: Vic speaks
  Round 1: Tammy speaks
  Round 2: Maya speaks (has seen all of Round 1)
  ...

  Latency: 5 turns × 30 seconds per model ≈ 2.5 minutes per round
  Bandwidth: Each model sees prior responses

Parallel (Multi-Model Infrastructure):
  Round 1: Maya, Frankie, Joe, Vic, Tammy all speak concurrently

  Latency: max(30 seconds) ≈ 30 seconds per round (major improvement)
  Bandwidth: Each model sees only prior rounds, not sibling responses in current round

  Trade-off: Lose reactivity in current round, gain speed
  Solution: If needed, do sequential within-round ordering
```

**Recommended**: Parallel execution by round (models don't see each other's responses in the same round, but see all of prior rounds). This maintains asynchronicity while dramatically reducing wall-clock time.

```
Implementation:
  Round 1:
    Call Maya.complete(context_with_no_priors) [async]
    Call Frankie.complete(context_with_no_priors) [async]
    Call Joe.complete(context_with_no_priors) [async]
    Call Vic.complete(context_with_no_priors) [async]
    Call Tammy.complete(context_with_no_priors) [async]
    await all_complete()

  Round 2:
    Call Maya.complete(context_with_round_1) [async]
    Call Frankie.complete(context_with_round_1) [async]
    ... etc
```

### Context History Strategies

**Option A: Full Transcript**

```
Context passed to each model:
  Topic: [topic]

  Prior discussion:

  Maya (Round 1): [full response]
  Frankie (Round 1): [full response]
  ...
  Joe (Round 2): [full response]

  Now respond as [Character]:
```

**Pros**: Models see complete history, can reference specific quotes, follow detailed chains
**Cons**: Token cost grows linearly with debate length; context window risk for long debates
**Token math**:
  - Topic: 200 tokens
  - Per response: ~300 tokens average
  - 3 rounds × 5 characters = 15 responses = 4,500 tokens
  - Total per turn: 200 + 4,500 + new prompt = ~5,000 tokens × 5 characters = 25,000 tokens total
  - Cost: ~$0.75 (at Claude pricing)

**When to use**: 3–5 rounds, 5 characters, when detail matters

---

**Option B: Summarized History with Recent Full Text**

```
Context passed to each model:
  Topic: [topic]

  Round 1 Summary:
    - Maya raised X, Y, Z risks
    - Frankie pushed back on Z, emphasized value W
    - Joe noted historical parallel H
    - Vic demanded evidence for X (insufficient)
    - Tammy identified second-order effect S

  Round 2 (Full):
    Maya: [full response]
    Frankie: [full response]
    ...

  Now respond as [Character]:
```

**Pros**: Controlled context size, models still see recent detail
**Cons**: Lose nuance from early rounds, summaries might miss key points
**Token math**:
  - Topic: 200 tokens
  - Round 1 summary: ~500 tokens
  - Round 2 full: 1,500 tokens
  - New prompt: 500 tokens
  - Total per turn: ~2,700 tokens × 5 characters = 13,500 tokens
  - Cost: ~$0.41

**When to use**: 5–10 rounds, or when controlling costs is important

---

**Option C: Hierarchical Summarization**

```
Context passed to each model:
  Topic: [topic]

  Meta-summary (what's been decided):
    Point 1: Broadly accepted
    Point 2: Contested (Maya vs. Frankie)
    Point 3: Needs more evidence (Vic's concern)

  Open questions:
    Q1: [...]
    Q2: [...]

  Most recent responses (current round):
    [Full text of last round]

  Now respond as [Character]:
```

**Pros**: Focuses debate toward open questions, guides toward convergence
**Cons**: Loses granularity, summarization overhead
**Token math**: ~1,500–2,000 tokens per turn
**When to use**: 10+ round debates, aiming for efficient convergence

---

### Error Handling & Reliability

Multi-model introduces new failure modes:

```python
def robust_turn(chair, character, retry_max=3):
    """Handle API failures, timeouts, rate limits"""
    for attempt in range(retry_max):
        try:
            response = chair.run_turn(character)
            if validate_response(response):  # Check non-empty, reasonable length
                return response
        except RateLimitError:
            if attempt < retry_max - 1:
                wait(exponential_backoff(attempt))
                continue
        except APIError as e:
            logger.error(f"API error on {character}: {e}")
            if attempt == retry_max - 1:
                # Fallback: use cached response or fallback model
                return cached_response(character) or fallback_model()

    raise DebateAbortedError(f"Failed to get response from {character}")
```

**Fallback Strategies**:
1. **Model substitution**: If Llama API is down, substitute Claude as Maya (suboptimal but preserves debate)
2. **Cache + delta**: Store responses from previous similar topics, use as fallback
3. **Single-model fallback**: If 3+ models fail, fall back to single-model committee (degrade gracefully)

---

## Cost & Latency Analysis

### Single-Model Baseline (Current)

```
Deliberation parameters:
  - Topic length: 200 tokens
  - Character brief: 100 tokens each
  - Context per turn: 300 tokens (short)
  - Response: 300 tokens average
  - 3 rounds, 5 characters

Per-turn cost:
  Prompt: 200 (topic) + 100 (brief) + 300 (context) = 600 tokens
  Response: ~300 tokens
  Total: ~900 tokens in, ~300 out

  Claude pricing: $3/1M input, $15/1M output
  Cost per turn: (900 × $3 + 300 × $15) / 1M = $7.20 / 1M = $0.000007

Per-deliberation cost:
  5 characters × 3 rounds = 15 turns
  15 × $0.000007 = $0.000105 ≈ $0.01

Latency (sequential):
  15 turns × 5 seconds (Claude) = 75 seconds
  Plus overhead: ~5 seconds
  Total: ~80 seconds per deliberation
```

### Multi-Model (Pattern 1 / Fixed Mapping)

```
Same token counts, but 5 different models:

Per-turn cost (assuming avg pricing: Claude $3/$15, GPT-4 $5/$20, others $2/$10):
  Claude turn: ~$0.0000072
  GPT-4 turn: ~$0.0000120
  Gemini turn: ~$0.0000040
  Llama turn: ~$0.0000020 (or free if self-hosted)
  Mistral turn: ~$0.0000030

  Average per turn: ~$0.0000056 (weighted)

Per-deliberation cost:
  15 turns × avg cost = 15 × $0.0000056 = $0.000084 ≈ $0.01

  (Roughly same as single model if you're not paying per-API-call)
  (If you're paying $5/month subscription per API: 5 × $5 = $25/month overhead)

Latency (parallel by round):
  3 rounds × max(latency per model)
  = 3 rounds × ~5 seconds (GPT-4, usually slowest)
  + overhead
  = ~20 seconds per deliberation (3x faster!)
```

**Key insight**: Multi-model parallelization makes per-API costs *lower* (not higher) if you use parallel execution, because wall-clock time is dominated by the slowest model, not the sum.

### Scaling to 10 Topics, 5 Runs Each

**Single-Model Approach**:
```
10 topics × 5 runs × $0.01 = $0.50
Latency: 10 topics × 5 runs × 80 seconds = 40,000 seconds = 11 hours (sequential)
```

**Multi-Model (Fixed), Parallel by Round**:
```
10 topics × 5 runs × $0.01 = $0.50 (token-level cost similar)
+ API subscription overhead: 5 APIs × $5/month = $25 (if not using shared subscriptions)
Latency: 10 topics × 5 runs × 20 seconds = 10,000 seconds = 2.8 hours (parallel execution)
```

---

## Evaluation Framework

### Existing 5-Rubric System

Cybernetics already uses a 5-rubric evaluation system (recorded in evaluation skill):

1. **Comprehensiveness**: Did we surface all relevant dimensions of the problem?
2. **Adversarial Rigor**: Were arguments genuinely contested, or just stated?
3. **Assumption Coverage**: Did we identify and test implicit assumptions?
4. **Reasoning Depth**: Did arguments go beyond surface-level?
5. **Decision Readiness**: Did we arrive at actionable conclusions?

### Extensions for Multi-Model Evaluation

**Add provenance tracking**:
```yaml
rubric: comprehensiveness
score: 8.2
breakdown:
  - dimension: "ethical implications"
    score: 9
    raised_by: [Frankie (Claude), Joe (Gemini)]
  - dimension: "technical feasibility"
    score: 7
    raised_by: [Vic (GPT-4o), Tammy (Claude)]
  - dimension: "political viability"
    score: 8
    raised_by: [Maya (Llama), Joe (Gemini)]
  - dimension: "resource requirements"
    score: 6
    raised_by: [Tammy (Claude)]
    gap: "no one asked about second-order resource effects"
```

**Model-specific evaluation**:
```yaml
model_contribution:
  Claude:
    rubrics_led:
      - decision_readiness (high quality summaries)
      - assumption_coverage (systematic probing)
    rubrics_weak:
      - adversarial_rigor (sometimes too diplomatic)

  GPT-4o:
    rubrics_led:
      - adversarial_rigor (strong logical challenges)
      - reasoning_depth (systematic argumentation)
    rubrics_weak:
      - comprehensiveness (misses value dimensions)

  Llama:
    rubrics_led:
      - assumption_coverage (paranoid questioning)
    rubrics_weak:
      - reasoning_depth (sometimes surface-level)
```

**Multi-model evaluation option**:
- Use an independent model (e.g., Claude in a fresh context) to evaluate the transcript
- OR: Have each model evaluate the transcript (see where they agree/disagree)
- Pros: avoids single-model bias in evaluation
- Cons: adds cost, introduces new variable

---

## Open Questions & Unknowns

### Technical Unknowns

1. **Does model diversity actually produce more genuine disagreement?**
   - Hypothesis: yes, because different training distributions create different latent spaces
   - Risk: disagreement is superficial (different words, same underlying logic)
   - Measurement: Use semantic similarity tools (embeddings) to measure deep vs. surface disagreement

2. **Does the character prompt matter once you have model diversity?**
   - Hypothesis: character prompting helps less if models have genuine differences
   - Alternative: character prompting plus model diversity amplifies differences
   - Test: Compare `(model diversity without prompting)` vs. `(prompting without diversity)` vs. `(both)`

3. **How do you handle context window size mismatches?**
   - Claude: 200k context
   - GPT-4: 128k context
   - Gemini: 1M context (!)
   - Llama: 8k–32k depending on variant
   - Solution: Use lowest common denominator, or summarize for smaller-context models?

4. **What happens when models disagree on facts (not just values)?**
   - Example: "Is the 2024 election outcome decided?" — models trained at different cutoffs disagree
   - Risk: debate becomes confused if participants are disagreeing on basic facts
   - Solution: Fact-checker role? Or accept that dated training is part of the model's authentic perspective?

5. **Does consensus evaluation work across models?**
   - Currently: run conversation through evaluator model
   - Risk: evaluator model might penalize things it doesn't understand
   - Solution: Use multiple independent evaluators, aggregate

---

### Architectural Unknowns

6. **Should the Chair be a dedicated model, or just a script?**
   - Simple script: coordinates turns, routes API calls (no thinking)
   - Dedicated model: Claude (as Chair) reads each turn, synthesizes before passing to next character
   - Pros of model-chair: more intelligent coordination, better summaries, can detect convergence
   - Cons: adds latency, adds cost, Chair's perspective intrudes

7. **How do you prevent deliberation drift?**
   - Risk: without a strong Chair, debate meanders
   - Risk: with a strong Chair, Chair's framing constrains debate
   - Solution: Use an explicit "agenda" that the Chair maintains? Or trust the character prompts?

8. **How do you handle API failures gracefully?**
   - If Llama API goes down mid-debate, do you substitute Claude-as-Maya? (Breaks the model-character pairing)
   - Do you abort the debate and retry? (Expensive in time/money)
   - Do you have cached fallback responses?

---

### Operational Unknowns

9. **What's the right cost-benefit threshold?**
   - Single-model: $0.01 per deliberation, 80 seconds
   - Multi-model: $0.01 + $5/month/API, 20 seconds
   - When is 4x speedup worth the subscription overhead?
   - Answer: probably for research/analysis (run many deliberations), not for one-off decisions

10. **How do you avoid model saturation / convergence?**
    - Risk: if you run the same deliberation 100 times, do you still get diversity?
    - Or: do models converge on the "right" answer, losing the debate function?
    - Solution: keep model diversity high; use Pattern 2 (random assignment) occasionally

11. **What's the right turnover strategy for models?**
    - As new models are released (o1, Gemini 2.5, Claude 4), should you refresh assignments?
    - Risk: if you keep switching models, you can't compare deliberations over time
    - Solution: keep a "stable set" (Claude, GPT-4, Gemini, Llama) + rotate experimental slots?

---

### Evaluation Unknowns

12. **Does multi-model evaluation bias results?**
    - If you use Claude to evaluate a debate that included Claude, does it score itself higher?
    - Solution: use external evaluator (different model), or aggregate many evaluators

13. **How do you measure "authenticity" of disagreement?**
    - What does it even mean for a debate to be "genuine" vs. "simulated"?
    - Possible metrics:
      - Semantic dissimilarity of arguments
      - Consistency with each model's known biases
      - Inability to collapse arguments into a unified position
    - Hard problem: no ground truth

---

## Connection to Existing Work

### MOOLLM Integration

The `MOOLLM-integration.md` document describes Pattern D (Parallel Multi-Instance) as aspirational future work:

> "Pattern D (Parallel Multi-Instance): Multiple dedicated LLM instances, each with task-specific optimization... ideally suited for critic networks, multi-agent debates, or consensus formation."

This document operationalizes Pattern D for the committee use case specifically.

---

### Multi-Agent Debate Literature

**Key papers**:
- Google's "Debating with More Compute" (2024): Shows AI-debate systems improve with model diversity
- UChicago's "Disagreement Problem": Models trained on same objective still disagree when reasoning about uncertainty
- Santa Fe Institute's "Societies of Thought": Multi-agent systems outperform single agents on complex reasoning tasks

**Core finding**: Disagreement is useful *if and only if* it's genuine (stems from different reasoning paths, not surface variation).

**Implication for Cybernetics**: Single-model committee might be producing "theatrical disagreement" (character-driven, not reasoning-driven). Multi-model committee should produce "genuine disagreement" (reasoning-driven, model-driven).

---

### Residuality Theory & Eigenforms

The probe methodology generates multiple runs to distinguish:
- **Eigenforms**: Structural features that recur across runs (belong to the landscape)
- **Residues**: One-off features specific to a run

**Application to multi-model**:
- Run the same topic with different model assignments (Pattern 2)
- Which insights appear regardless of assignment? (Eigenforms—truly important)
- Which insights are model-specific? (Residues—interesting but not structural)

Example:
```
Topic: "Should we build AGI without alignment?"

Run 1 (Claude=Maya): Risk of misalignment cited
Run 2 (Llama=Maya): Risk of misalignment cited
Run 3 (Mistral=Maya): Risk of misalignment cited

→ Eigenform: Misalignment is a structural concern

Run 1 (Claude=Frankie): Values of human agency emphasized
Run 2 (Llama=Frankie): Values of autonomy emphasized
Run 3 (Mistral=Frankie): Values of human dignity emphasized

→ Residue: Different models emphasize different aspect of values
→ Eigenform: Values reasoning is important
```

---

### Pask's Conversation Theory

Gordon Pask's conversation theory states that genuine conversation requires participants with genuinely different understanding. A monologue (one agent with costume changes) is not conversation.

**Current single-model committee**: Closer to monologue—one agent (the model) speaking through five puppets (characters).

**Proposed multi-model committee**: Actual conversation—five different agents (models) with different cognitive architectures, reasoning strategies, and latent spaces interacting through five roles (characters).

---

## Production Readiness Checklist

If multi-model approach is adopted:

- [ ] API keys and subscriptions configured for all models
- [ ] Abstraction layer written (`ModelClient` base class + implementations)
- [ ] Orchestrator / Chair implemented with error handling and parallel execution
- [ ] Context management strategy chosen (full, summarized, or hierarchical)
- [ ] Evaluation framework extended with provenance tracking
- [ ] Fallback strategies documented and tested
- [ ] Cost monitoring in place (track per-deliberation spend)
- [ ] Model personality profiles documented and updated as models change
- [ ] Logging/audit trail system to track which model played which character (important for reproducibility)
- [ ] Documentation of results from Phases 1–4 (published to `/agent/deliberations/` and summarized in handoff)

---

## Appendix: Implementation Template

### Quick-start Code Structure

```python
# main.py - Orchestrator

from abc import ABC, abstractmethod
from typing import Dict, List
import json
from datetime import datetime

# Model interface
class ModelClient(ABC):
    @abstractmethod
    def complete(self, prompt: str, context_history: str) -> str:
        pass

# Implementations
class ClaudeClient(ModelClient):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = "claude-3-5-sonnet-20241022"

    def complete(self, prompt: str, context_history: str) -> str:
        from anthropic import Anthropic
        client = Anthropic(api_key=self.api_key)
        messages = [
            {"role": "user", "content": prompt + (f"\n\n{context_history}" if context_history else "")}
        ]
        response = client.messages.create(
            model=self.model,
            max_tokens=1500,
            messages=messages
        )
        return response.content[0].text

class GPT4Client(ModelClient):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = "gpt-4o"

    def complete(self, prompt: str, context_history: str) -> str:
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key)
        messages = [
            {"role": "user", "content": prompt + (f"\n\n{context_history}" if context_history else "")}
        ]
        response = client.chat.completions.create(
            model=self.model,
            max_tokens=1500,
            messages=messages
        )
        return response.choices[0].message.content

# ... similar for GeminiClient, LlamaClient, MistralClient

# Character definitions
CHARACTERS = {
    'Maya': {
        'role': 'Paranoid Realist',
        'brief': 'Catch political naiveté, hidden agendas, misaligned incentives.',
        'prompt_template': 'You are Maya, the Paranoid Realist. Your job is to catch naiveté, hidden agendas, and misaligned incentives. {topic} What risks are being dismissed? What incentives aren\'t aligned? What\'s the dark possibility?'
    },
    'Frankie': {
        'role': 'Idealism/Values',
        'brief': 'Catch mission drift, ethical shortcuts.',
        'prompt_template': 'You are Frankie, advocating for Idealism and Values. You catch mission drift and ethical shortcuts. {topic} What values are at stake? Where are we compromising principles?'
    },
    # ... etc for Joe, Vic, Tammy
}

# Chair / Orchestrator
class Chair:
    def __init__(self, topic: str, model_assignment: Dict[str, str], models: Dict[str, ModelClient]):
        self.topic = topic
        self.model_assignment = model_assignment  # {'Maya': 'claude', 'Frankie': 'gpt4', ...}
        self.models = models  # {'claude': ClaudeClient(...), ...}
        self.transcript = []
        self.turn_count = 0

    def run_turn(self, character: str, round_num: int) -> str:
        """Run one character's turn"""
        model_name = self.model_assignment[character]
        model = self.models[model_name]
        character_info = CHARACTERS[character]

        # Build prompt
        prompt = character_info['prompt_template'].format(topic=self.topic)

        # Build context from previous turns
        context = self._build_context()

        # Call model
        response = model.complete(prompt, context)

        # Record
        self.transcript.append({
            'character': character,
            'model': model_name,
            'round': round_num,
            'turn': self.turn_count,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        self.turn_count += 1

        return response

    def _build_context(self) -> str:
        """Build context from previous responses"""
        if not self.transcript:
            return ""

        # Option A: Full transcript
        context_parts = [f"{t['character']} ({t['model']}): {t['response'][:200]}..."
                        for t in self.transcript[-10:]]
        return "\n\n".join(context_parts)

    def run_deliberation(self, num_rounds: int = 3, character_order: List[str] = None):
        """Run full deliberation"""
        if not character_order:
            character_order = ['Maya', 'Frankie', 'Joe', 'Vic', 'Tammy']

        for round_num in range(num_rounds):
            for character in character_order:
                self.run_turn(character, round_num)

        return self.transcript

    def save_transcript(self, filename: str):
        """Save to JSON"""
        with open(filename, 'w') as f:
            json.dump({
                'topic': self.topic,
                'model_assignment': self.model_assignment,
                'timestamp': datetime.now().isoformat(),
                'transcript': self.transcript
            }, f, indent=2)

# Main execution
if __name__ == '__main__':
    import os

    # Setup models
    models = {
        'claude': ClaudeClient(os.getenv('ANTHROPIC_API_KEY')),
        'gpt4': GPT4Client(os.getenv('OPENAI_API_KEY')),
        'gemini': GeminiClient(os.getenv('GOOGLE_API_KEY')),
        'llama': LlamaClient(api_endpoint=os.getenv('LLAMA_ENDPOINT')),
        'mistral': MistralClient(os.getenv('MISTRAL_API_KEY')),
    }

    # Run deliberation
    topic = "Should we build AGI without alignment safeguards?"

    assignment = {
        'Maya': 'llama',
        'Frankie': 'claude',
        'Joe': 'gemini',
        'Vic': 'gpt4',
        'Tammy': 'claude',  # Can repeat models
    }

    chair = Chair(topic, assignment, models)
    transcript = chair.run_deliberation(num_rounds=3)

    chair.save_transcript(f'deliberation-{datetime.now().isoformat()}.json')

    # Print summary
    for turn in transcript:
        print(f"\n{turn['character']} ({turn['model']}, Round {turn['round']})")
        print(f"{turn['response'][:300]}...")
```

### Configuration File Template

```yaml
# config.yaml - multi_model_committee.yaml

models:
  claude:
    provider: anthropic
    api_key_env: ANTHROPIC_API_KEY
    model_id: claude-3-5-sonnet-20241022
    max_tokens: 1500
    temperature: 0.7

  gpt4:
    provider: openai
    api_key_env: OPENAI_API_KEY
    model_id: gpt-4o
    max_tokens: 1500
    temperature: 0.7

  gemini:
    provider: google
    api_key_env: GOOGLE_API_KEY
    model_id: gemini-2.0-pro
    max_tokens: 1500
    temperature: 0.7

  llama:
    provider: together_ai  # or self-hosted
    api_key_env: TOGETHER_API_KEY
    model_id: meta-llama/Meta-Llama-3-70B
    max_tokens: 1500
    temperature: 0.7

  mistral:
    provider: mistral_ai
    api_key_env: MISTRAL_API_KEY
    model_id: mistral-large
    max_tokens: 1500
    temperature: 0.7

patterns:
  fixed_mapping:
    maya: llama
    frankie: claude
    joe: gemini
    vic: gpt4
    tammy: claude

  random_assignment: true  # For Pattern 2 experiments

orchestration:
  context_strategy: full_transcript  # or summarized, or hierarchical
  parallel_by_round: true
  turn_order: [Maya, Frankie, Joe, Vic, Tammy]
  max_rounds: 3
  convergence_threshold: 0.85  # For early stop

evaluation:
  use_independent_evaluator: true
  evaluator_model: claude
  rubrics:
    - comprehensiveness
    - adversarial_rigor
    - assumption_coverage
    - reasoning_depth
    - decision_readiness

logging:
  transcript_dir: ./deliberations/
  profile_dir: ./profiles/
  results_dir: ./results/
  log_level: INFO
```
