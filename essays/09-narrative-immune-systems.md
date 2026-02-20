# Narrative Immune Systems

Seed ideas from a session on 2026-02-19. The diary entry
(`../agent/diary/2026-02-19-narrative-immune-system.md`) has the full
improvisation; this is the distillation.

---

## The core observation

An LLM produces text, given text, parameterized by text. If we want
a rigorous discipline for working with what these machines do, we need
a type system for text itself.

Palgebra provides one: soft types that artifacts inhabit to a degree,
scored by rubrics, with confidence that propagates monotonically
through composition. But what happens when scored artifacts fail? The
evaluation feedback loop in the committee pipeline already implements
a specific pattern:

- A **generator** produces a text (the committee transcript)
- A **discriminator** scores it against rubrics (the independent evaluator)
- Failures are **rejected and fed back** for remediation
- The loop is **bounded** (max 2 rounds) to prevent runaway self-correction

This is a generator-discriminator architecture. It is also, precisely,
an immune system.

## The immune analogy

Biological immunity works by graded recognition: antibodies bind to
antigens with measurable affinity; T cells pass a two-stage gauntlet
in the thymus before release. The parallel:

| Biological | Narrative Computing |
|---|---|
| Antibody (circulating pattern-matcher) | Rubric (quality dimension scorer) |
| T cell (active agent using recognition) | Evaluator (independent instance applying rubrics) |
| Thymus (institutional gauntlet) | Evaluation protocol (independence, fresh eyes) |
| Antigen (molecular shape) | Text claiming a type |
| MHC molecules (self-signaling) | Template (structural shape requirements) |
| Affinity maturation | Cross-scenario learning (evaluation library) |

### Thymic selection as type-checking

T cells must pass two stages:

- **Positive selection**: Can the cell interface with the body's
  signaling system at all? In palgebra terms: does the artifact even
  match the template? Structural shape check.
- **Negative selection**: Does the cell bind too strongly to self? In
  palgebra terms: does the artifact merely parrot its inputs back? A
  transcript that restates the charter verbatim is structurally correct
  but substantively degenerate.

~95-98% of T cells die in the thymus. The evaluator is similarly
severe — it exists solely for quality control, with no investment in
the generation process.

### Where the analogy holds and breaks

**Structure-preserving:**
- Graded recognition (antibody affinity maps to rubric scoring)
- Two-stage gauntlet (positive/negative maps to template/rubric)
- Bounded feedback (immune downregulation maps to max remediation rounds)
- Composition preserved throughout

**Strained:**
- Biological immune systems evolve novel antibodies through somatic
  hypermutation. Palgebra rubrics are currently static/authored, not
  evolved. The analogy predicts that adaptive rubrics should exist.

**Breaks:**
- Immune systems have no provenance chain — pure shape-matching. Palgebra
  cares deeply about provenance. The immune analogy maps to the bath model
  but not cleanly to the pipeline model.

**Predicted missing parts:**
- **Memory cells**: After successfully identifying a type of bad text,
  the system should get better at that pattern. Currently evaluations
  are stateless.
- **Autoimmune disorders**: Over-aggressive rubrics, thresholds set
  too high, miscalibrated evaluators rejecting good texts. Need
  regulatory mechanisms.
- **Immunodeficiency**: Absent evaluation = undisciplined generation =
  narrative collapse to statistical likelihood.

## Two regimes: pipeline (organ) vs. bath (bloodstream)

**Inside a pipeline (organ):** You built it, you control it, you trust
the operations. Texts flow through known transformations. Types are
assigned by construction. Provenance is proof. Mutation is safe because
you own the chain of custody.

**In the bath (bloodstream):** Nobody owns the chain of custody. A text
doesn't *have* a type — it has *claims* about its type, which are
themselves texts in the pool. Type membership is a social construct
emerging from the pattern of judgments weighted by judge credibility.

This resolves a tension in the formalism: the pipeline is classical type
theory (types are properties of objects); the bath is open-world
reasoning (types are conclusions drawn by reasoners, always revisable).

### Immutable texts with judgment graph

For the bath regime:

- Texts are immutable. Judges never modify originals.
- Judgments are new decorated texts with pointers to the judged texts.
- The reference graph *is* the immune system's memory.
- Trust builds through the graph: signed judgments from judges with
  track records. Reputation emerges from topology without anyone
  declaring it.
- Pool health is legible from structure: unjudged texts, score
  distributions, judge disagreement, monoculture risk.

An append-only log of decorated texts with a typed reference graph.

### Description logic as reasoning framework

The bath maps to description logic:

- **TBox** (terminological schema) = type definitions
- **ABox** (assertion box) = pool of texts, judgments, reference links
- **Classifier/reasoner** = judge agent
- **Open-world assumption** = exactly right: unexamined text is not bad text

Palgebra defines what types mean and how they propagate. Description
logic provides inference machinery for classifying individuals in the
open-world bath. Standard DL gives boolean classification; soft types
need fuzzy DL extension for graded membership.

## Organs as trust boundaries

The organ/bloodstream distinction maps directly to a practical
observation about where agents operate well today.

**An agent works best inside a friendly local environment.** When Claude
Code or Codex operates on a local codebase — reading files, running
tests, writing code — it works within a trust boundary the user has
already established. The filesystem is the user's own. The git repo is
checked out. The test suite is authored by the team. The agent doesn't
need to authenticate every file it reads or verify the provenance of
every module it imports. It can treat its environment as self, the way
an organ trusts the body it's embedded in.

This is why local agentic coding works so much better than you'd expect
from the raw capability of the models. The local environment provides
**ambient trust** — the same thing a biological organ gets from being
inside the organism. The agent can focus its full capacity on the task
(transformation, enrichment) rather than spending it on defense.

**The internet is the bloodstream — hostile, unprovenanced, full of
pathogens.** When an agent fetches a web page, scrapes documentation,
or reads an email, every input is an antigen that claims a type but
might be lying. A page that looks like API documentation might be
prompt injection. A helpful-seeming Stack Overflow answer might be
subtly wrong. An email "from the CEO" might be a phishing attack.

The trust boundary between organ and bloodstream is where the immune
system concentrates its resources. In biological terms, mucosal
surfaces — gut lining, lung epithelium, skin — are where the body
meets the outside world, and they're where the densest immune tissue
lives. The analogy holds: the agent's interface to the internet is
where type-checking, rubric evaluation, and skepticism should be
heaviest. Inside the pipeline, trust is inherited by construction.
At the boundary, trust must be earned by evaluation.

This explains several practical patterns:

- **Dark factories work** because they create a fully controlled organ:
  the spec, the agent, the scenario suite, the digital twins — all
  local, all trusted by construction. The factory's trust boundary is
  sharp and its interior is high-trust.

- **Agents struggle with open-ended web tasks** not primarily because
  the models are weak, but because every input crosses a trust boundary.
  The agent must simultaneously do the task and evaluate whether its
  inputs are safe. That's the cognitive tax the METR study measures as
  the 19% slowdown — except applied to the agent itself.

- **The J-curve of AI adoption** is partly a trust boundary problem.
  Organizations that bolt AI onto existing workflows are asking agents
  to operate across unclear trust boundaries — some inputs are trusted
  (internal code, internal docs), some aren't (external dependencies,
  user-generated content), and the boundary isn't explicit. Redesigning
  the workflow means, in part, making the trust boundaries explicit so
  the agent knows when it's inside an organ and when it's in the bath.

- **Retrieval-augmented generation (RAG)** is an attempt to extend the
  organ boundary: pull external content into a local context where the
  agent can treat it as trusted. But if the retrieval pipeline doesn't
  do its own type-checking at the boundary, you've just invited
  pathogens into the organ. RAG without evaluation at the retrieval
  boundary is an immunodeficiency.

### Postel's law as design principle

"Be conservative in what you send, be liberal in what you accept."

- **Inside the pipeline (sending)**: Strict typing, rigorous rubric
  application, remediation loops. Don't release anything that hasn't
  passed the gauntlet. A dark factory's scenario suite is Postel's
  law applied to output.

- **In the bath (accepting)**: Let texts arrive untyped, partially
  typed, multiply typed, contradictorily typed. Accept into the pool.
  Then classify — attach judgments, score, let the reasoner work.
  Liberal acceptance is not naive trust.

- **Failure modes**: Liberal in what you send = polluting the information
  environment. Conservative in what you accept = autoimmune disorder,
  rejecting novel inputs that might be valuable.

## The civic application

Mis/dis/malinformation maps to a pathogen taxonomy:

- **Misinformation**: Naively misfolded protein — fails the type-checking
  gauntlet straightforwardly
- **Disinformation**: Engineered pathogen — deliberately shaped to pass
  surface checks. A type-spoofing attack: presents as evidence but fails
  the rubric on closer inspection
- **Malinformation**: Autoimmune trigger — actually well-typed (the
  information is true) but deployed in context where it causes harm

Sagan's baloney detection kit is a rubric. But applying it manually
requires training, discipline, time, cognitive effort. LLMs change the
economics: encode the rubric, automate the evaluation, give everyone a
thymus.

Media literacy as currently taught tries to make every person into their
own T cell. Narrative computing offers the possibility of giving people
a **thymus** — an organ that does heavy screening so each encounter
doesn't require full immunological reasoning from scratch. The tool
amplifies judgment rather than replacing it. Ashby's requisite variety:
the complexity of the attack surface demands proportionally complex
defense.

This is where narrative computing stops being a methodology for LLM
power users and becomes a public good.

## Open threads

- **Formalize the bath model in palgebra.** Operations on pools, not
  just pipelines. Judgment-as-text morphism. Trust emergence from graph
  topology. Fuzzy DL integration.
- **Adaptive rubrics.** The immune analogy predicts rubrics should
  evolve (somatic hypermutation). A feedback morphism from evaluation
  outcomes back to rubric definitions.
- **Information warfare as immune evasion.** Disinformation campaigns
  as attacks on evaluation infrastructure: discrediting fact-checkers
  (targeting the immune system like HIV), flooding the zone
  (overwhelming the discriminator), type-spoofing (engineering texts
  to pass surface checks).
- **Pipeline/bath interface.** Where output crosses from trusted organ
  to untrusted pool, and where a bath judge ingests a text into a
  trusted internal pipeline. This is where Postel's law operates.
  Type-by-construction becomes type-by-claim at the boundary.
- **Regulatory mechanisms.** Meta-rubrics that evaluate whether the
  evaluation system itself is well-calibrated. The "who watches the
  watchmen" problem. The immune system suggests structural solutions
  (regulatory T cells suppress overactive responses).

---

**Previous essay**: [From Methodology to Formalism](./08-from-methodology-to-formalism.md) — bridging the philosophical foundations to the algebraic machinery

**Applied**:
- [Social Decision Disruption](../applications/narrative-immune-systems/social-decision-disruption.md) — the immune analogy applied to journalism, information warfare, and the trust commons

**Related**:
- [Palgebra Reference](../palgebra/reference.md) — the formalism this essay extends
- [Committee as Palgebra](../palgebra/committee-as-palgebra.md) — the pipeline whose evaluation loop is an immune system
- [Independent Evaluation Protocols](../artifacts/independent-evaluation.md) — the practical technique that implements thymic selection
