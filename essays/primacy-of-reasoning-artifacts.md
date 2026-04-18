# The Primacy of Reasoning Artifacts

**How three unrelated traditions converge on the same structural claim: the models matter more than what they produce**

---

## The Claim

Code is not the most important artifact of software development.

This sounds like something a manager would say. It is also true, and has been true since before there were managers of software developers. It was true when Naur wrote it down in 1985, true when NASA's systems engineers rediscovered it in the 2010s, and true when we stumbled into it again while building adversarial committee pipelines for LLM-assisted deliberation.

The claim generalizes beyond software. Code, hardware, recommendations — these are downstream products. They are the residue of a process. The process leaves behind something else, something less tangible and more important: the reasoning that produced the product. The theory. The model stack. The deliberation record. The story of why this solution and not some other.

Lose the product but keep the reasoning, and you can rebuild. You can also decide the product was wrong and build something better, because the reasoning tells you where the choices were made and what the alternatives looked like.

Keep the product but lose the reasoning, and you are maintaining a mystery. The code runs, but you don't know why it's shaped the way it is. The system works, but you can't tell whether it's solving the right problem. The recommendation sits in front of you, but you have no basis for evaluating whether to follow it.

Three traditions arrived at this claim independently. They come from different domains, different decades, different intellectual lineages. None cites the others. The convergence is the argument.

---

## I. Naur: The Theory Is the Program

In 1985, Peter Naur — one of the designers of ALGOL 60, editor of the report that coined the term "Backus-Naur Form" — published a twelve-page paper called "Programming as Theory Building." It is one of those papers that sounds almost trivially true on first reading and becomes more radical the longer you sit with it.

Naur's central claim: programming is not the production of program text. It is the construction, in the programmers' minds, of a *theory* of how certain real-world affairs can be supported by a computer. The program text is evidence of the theory, but it is not the theory itself.

By "theory" Naur means something specific, borrowed from Gilbert Ryle's distinction between knowing-that and knowing-how. A programmer who holds the theory of a program can explain why the code is structured the way it is, what would need to change to accommodate a new requirement, and why particular alternatives were rejected. Someone who merely reads the code — even with perfect documentation — cannot do these things. They can tell you *what* the code does. They cannot tell you *why it does it that way*, what it was chosen over, or how the domain maps to the implementation.

This has a sharp consequence for maintenance. Code whose theory has been lost cannot be reliably modified. Not because the code is opaque — it might be perfectly readable — but because readability and understanding are different things. The maintainer can see what each function does. What they cannot see is the web of constraints, trade-offs, rejected alternatives, and domain assumptions that shaped the design. Every modification is a guess against this invisible web. Sometimes the guess is right. Sometimes it introduces a subtle bug that won't surface for months, because the maintainer unknowingly violated a constraint they didn't know existed.

Documentation doesn't save you. This is Naur's sharpest edge. Documents describe the program text — they explain what it does, how to use it, sometimes how to extend it. But they do not transmit the theory. The theory includes things that are extraordinarily hard to write down: *why* one approach was chosen over another, *what* the real constraints were (as opposed to what the requirements document said they were), *how* the developer understood the domain at the time, *which* simplifying assumptions were made and what would break if they turned out to be wrong. These things live in heads. They are transmitted through conversation — through working alongside someone who holds the theory, asking questions, hearing the war stories, absorbing the context. When the people leave, the theory goes with them. The code remains, but it becomes an archaeological site rather than a living system.

Naur couldn't have anticipated agents. But the pathology he describes is exactly what happens when an LLM generates code without a human having built a theory first.

A colleague recently told me that his codebase had grown past his understanding of it. His coding agent was writing code faster than he could comprehend. He was maintaining an archaeological site that had been excavated by a machine — layer upon layer of plausible-looking program text, each locally correct, the ensemble opaque. There was no theory to lose because none had ever been constructed. The agent doesn't hold theories. It holds weights. It produces text that has the statistical form of code written by someone who held a theory, without the theory itself. The residue without the reasoning.

My response was: slow down. Write prose before code. Articulate the constraints, the invariants, the types, the domain assumptions — in natural language, for humans. Converse with the agent to explore the problem space. Work out candidate solutions and reason about which one best fits the constraints. *Then* generate executable code, against tests that encode the invariants you've identified. The prose is the theory's external representation. The code is its compilation target.

This is not a workflow tip. It is Naur's thesis, operationalized for the agent era. The theory must exist before the code, because the code without the theory is unmaintainable by definition. The agent can help you build the theory — it's a useful conversational partner for exploring problem spaces, surfacing assumptions, generating alternatives. But it cannot hold the theory for you. That's your job. Process over product. Planning over plan.

---

## II. NASA: The System Is the Models

Between 2010 and 2020, Michael Watson, Bryan Mesmer, and Phillip Farrington — working through the NASA Systems Engineering Research Consortium at Marshall Space Flight Center — published a series of technical papers and a comprehensive NASA Technical Publication on what they called "Engineering Elegant Systems."

They arrived at a claim that is structurally identical to Naur's, from a completely different starting point. Where Naur was reflecting on the practice of programming, Watson and colleagues were reflecting on the practice of building rockets. The stakes are different. The cost of losing the reasoning is measured in lives and billions of dollars rather than in maintenance headaches. But the structure is the same.

Their framework identifies four aspects of systems engineering: mission context, system-integrating physics, organizational structure and culture, and policy and law. A system — a rocket, a satellite, a launch complex — sits at the intersection of all four. No single engineering discipline covers all of them. The physicist understands the thermodynamics but not the procurement regulations. The project manager understands the organizational constraints but not the structural dynamics. The lawyer understands the policy environment but not the physics.

Systems engineering, in Watson's framework, is the discipline of maintaining all four models simultaneously and ensuring they remain coherent with each other as design evolves. The models are not the hardware. The models are the understanding of how the hardware relates to the mission, the physics, the organization, and the regulatory environment. The hardware is downstream of the models, not the other way around.

This produces a sharp distinction between verification and validation. You *verify* that the product matches the specification: did we build it right? You *validate* that the specification matches the mission need: did we build the right thing? Both are necessary. Both require models that are prior to and independent of the product. But here's the key: you can verify without models — you just check the product against the spec. You cannot validate without models, because validation requires understanding what the spec was supposed to achieve, what trade-offs were made in writing it, what mission requirements it was meant to satisfy.

A system you can verify but not validate is a system that works but that you cannot evaluate. It does what it says on the box, but you have no way to determine whether what's on the box is what you actually needed. This is the systems engineering version of Naur's archaeological site: the artifact is intact, but the reasoning that produced it is gone.

Elegance, in Watson's vocabulary, is a set of system characteristics — efficacy, efficiency, robustness — that are properties of the *design reasoning*, not just the hardware. A system can work without being elegant. An elegant system is one whose design models are coherent, parsimonious, and transparent. The elegance is in the models, not the metal.

---

## III. Cyberneutics: Stories Over Verdicts

The committee pipeline produces two kinds of output. One is a recommendation — the committee's collective assessment of the situation, the convergent product of the funnel. The other is a deliberation record — the transcript of who argued what, where they agreed, where they disagreed, what evidence was cited, what assumptions were challenged, what remained unresolved.

The recommendation is not the most important output.

This took us a while to understand. Early in the development of the methodology, we evaluated the committee by the quality of its recommendations. Did the committee reach a better decision than a single prompt would have? Sometimes yes, sometimes no. A black swan evaluation showed that the committee did not demonstrably outperform solo evaluation on outcome quality. If you judged the pipeline by the quality of its products — its recommendations — it was not clearly superior to simpler approaches.

But the deliberation record was consistently, structurally different from anything a solo prompt produced. It contained the reasoning. It showed which considerations were weighed, how they were weighed, where the characters disagreed and why. It surfaced assumptions that a single prompt would leave implicit. It made visible the tensions and trade-offs that a solo answer would either resolve silently or ignore entirely.

The fan stage produces stories — four narrators generating divergent scenarios, each revealing different aspects of the situation from different worldview lenses. These are not candidate answers. They are models of the problem from different vantage points, the way charts on a manifold are different maps of the same territory, each valid in its own region, each distorting in different ways.

The funnel stage produces a deliberation record. Five characters — Maya the paranoid realist, Frankie the idealist, Joe the continuity guardian, Vic the evidence prosecutor, Tammy the systems observer — argue under procedural rules. The output is not a consensus verdict. It is a trace of reasoning: who challenged what, what evidence was demanded, where the characters found common ground and where they didn't, what remained genuinely unresolved. The trace is the primary artifact. The recommendation, if one emerges, is secondary.

The human decision-maker reads stories, not verdicts. Their job is not to accept or reject a recommendation. It is to engage with the models — the stories, the tensions, the assumptions made explicit — and make a judgment informed by considerations they might not have generated alone. The committee doesn't decide for you. It tells you what a decision in this space looks like from five incompatible directions, so that when you decide, you do so knowing what you're trading off.

This is Naur's theory building in a different domain. The reasoning record is the theory; the recommendation is the program text. Lose the record but keep the recommendation, and you have a verdict you can follow but cannot evaluate. You don't know what was considered, what was dismissed, what wasn't raised at all. Keep the record but lose the recommendation, and you can re-derive it — or decide it was wrong and arrive somewhere better, because the record shows you where the pivotal judgments were made.

The committee pipeline's value proposition is not accuracy. It is auditability. You can examine what was considered. You can spot what was missed. You can trace why the recommendation has the shape it has. This is independently valuable even when the recommendation is wrong — *especially* when it's wrong, because the reasoning record tells you where the error entered and what assumptions to revisit.

---

## IV. The Convergence

Three traditions. Three domains. Three independent arrivals at the same structural claim.

| | Primary artifact | Reasoning artifact | What's lost when reasoning is lost |
|---|---|---|---|
| **Naur** (software, 1985) | Program text | Theory in heads | Code becomes an archaeological site — modifiable only by guesswork |
| **NASA Elegant** (systems, 2010–2020) | Hardware / system | Model stack (mission, physics, org, policy) | System you can verify but cannot validate |
| **Cyberneutics** (decisions, 2024–) | Recommendation | Deliberation stories | Verdict you can follow but cannot evaluate |

No one told Naur about NASA's model stack. No one told Watson about adversarial committees. Naur was a Danish computer scientist reflecting on the practice of ALGOL programming. Watson was a NASA engineer reflecting on the practice of rocket design. We were practitioners trying to make LLM outputs trustworthy enough to be useful for real decisions. Different decades, different problems, different intellectual traditions. Same claim.

This kind of convergence is what we call a *narrative proof* — not a formal theorem, but epistemically compelling evidence constituted by independent arrival from unrelated starting points. No single chain of citation produces the conclusion. Instead, unrelated traditions, working on different problems with different tools, keep landing in the same place. The claim keeps being rediscovered because it keeps being true.

The routes to the claim are worth noting because they're so different:

Naur arrived through philosophical reflection on the practice of programming, grounded in Ryle's distinction between knowing-that and knowing-how. His method was introspection informed by decades of practice. His evidence was the accumulated observation that programs whose developers had left could not be reliably maintained, regardless of documentation quality.

Watson and colleagues arrived through the practice of building rockets, where the cost of poor systems engineering is measured in lives and billions of dollars. Their method was empirical analysis of NASA programs — what distinguished successful missions from failed ones. Their evidence was institutional: the programs that maintained their model stacks produced elegant systems; the programs that let the models decay produced systems that worked (when they worked) by accident rather than design.

We arrived through the practice of structured LLM deliberation, where the cost of losing the reasoning is measured in decisions made without understanding why. Our method was iterative engineering — building pipelines, evaluating their outputs, noticing that the deliberation records were consistently more valuable than the recommendations themselves. Our evidence was the black swan evaluation: the committee didn't beat solo evaluation on outcome quality, but it always produced something solo evaluation didn't — an inspectable record of the reasoning.

Different stakes. Different methods. Different evidence. Same structure. Same claim.

---

## V. The Agent Era Makes This Urgent

Everything described above was true before LLMs. Naur's paper is from 1985. NASA's framework was developed through the 2010s. The claim about reasoning artifacts didn't need agents to be correct.

But the agent era makes the claim urgent rather than academic, because agents industrialize the exact failure mode all three traditions warn against: producing artifacts without reasoning.

An LLM coding agent generates program text without ever holding a theory. It produces code that compiles, passes the tests it can see, and reads like something a competent engineer might have written. Every surface cue for quality is present. The only thing missing is the theory — the understanding of why the code is shaped the way it is, what constraints it respects, what alternatives were considered and rejected, how the domain maps to the implementation. The agent doesn't hold theories. It doesn't reject alternatives. It doesn't reason about constraints. It completes patterns. The output has the *form* of code written by someone with a theory, without the theory itself.

This is Naur's maintenance nightmare, industrialized. Not one archaeological site, but thousands — generated at the speed of token completion, each one plausible, each one theory-less. The developer who lets the agent run without building the theory first will, within weeks, have a codebase they cannot maintain. Not because the code is bad. Because the reasoning is absent.

A recommendation engine does the same thing to decisions. It generates a verdict — "you should do X" — without a deliberation record. It tells you what to do without telling you why, what was considered, what was traded off, what assumptions were made. The verdict might be right. It might be wrong. You have no basis for evaluating which, because the reasoning isn't there. It was never there. The engine doesn't reason. It completes.

The response, in both cases, is the same: build the reasoning *before* generating the artifact.

In software, this means prose before code. Write the constraints, the invariants, the types, the domain assumptions, the rejected alternatives — in natural language, for humans — before the agent writes a line. Converse with the agent to explore the problem space. Generate candidate solutions and reason about their fit. Then, and only then, generate executable code, against tests that encode the constraints you've identified.

The tests deserve particular attention. A test suite that encodes invariants and exemplary behavior is a piece of the theory in executable form. It says: *this must be true regardless of implementation.* Code generated against such tests is code that respects the constraints the human articulated. The test is a theory fragment; the code is its evidence. If the code passes, the evidence supports the theory. If it fails, either the theory has a gap or the implementation does — and the test tells you which question to ask.

In decision support, the committee pipeline is the mechanism. It doesn't just produce recommendations. It produces theories of the situation — multiple, competing, stress-tested. The fan generates divergent models. The funnel generates a deliberation record. The human reads the theories and makes the decision. The agent era's contribution is to make the theory-building step faster and richer, not to skip it.

The common error is to treat the agent as a faster version of the human. It is not. It is a fast generator of theory-less artifacts. The human's job — now more than ever — is to be the theory-builder, the model-maintainer, the keeper of the reasoning.

Process over product. Planning over plan. Stories over verdicts.

---

## VI. Further Witnesses

The three-tradition convergence is the essay's core argument, but the claim has additional independent witnesses worth noting briefly. Each arrived at the same insight from a different direction, and none of them was talking to the others.

**Brooks.** Fred Brooks, in *The Mythical Man-Month* (1975, revised 1995) and "No Silver Bullet" (1986), argued that the hard part of software is the conceptual structure — the design, the specification, the understanding of the problem — not the representation. The representation is just the encoding. In the 20th anniversary edition, Brooks cites Naur's paper approvingly. Two of the most influential figures in the history of software engineering, working a decade apart, converging on the same claim.

**Dijkstra.** Edsger Dijkstra, in "On the Cruelty of Really Teaching Computer Science" (1988), argued that programming is a thinking activity, not a typing activity, and that computer science education should be radically formal — focused on the mathematical reasoning that produces programs rather than on the programs themselves. Dijkstra arrived from a very different direction than Naur (radical formalism vs. philosophical pragmatism), but the destination is the same: the reasoning is primary; the code is secondary.

**Coles.** Robert Coles, in *The Call of Stories* (1989), documented what happened when medical students read literature as part of their training. They became better clinicians — not because the novels contained medical knowledge, but because the *process of engaging with stories* developed capacities for judgment, empathy, and interpretive skill that transferred to clinical practice. The students who read Tolstoy and George Eliot learned to sit with ambiguity, to consider multiple interpretations, to notice what the patient was not saying. The stories were the reasoning artifact; clinical competence was the product. Coles was not writing about software or systems engineering. He was writing about how young doctors learn to think. Same claim, different domain.

**Pask.** Gordon Pask's Conversation Theory provides the micro-mechanics. Understanding, for Pask, is demonstrated through *teachback* — the ability to reconstruct another's position from a different starting point. Agreement is a surface indicator that may or may not reflect understanding. Teachback is the test. If you can explain the reasoning in your own terms, you hold the theory. If you can only repeat the conclusion, you hold the artifact. The teachback is the reasoning; agreement is the residue.

**The shared canon.** There is a cultural instance of the same claim that predates all of these. The canonical literary references that once pervaded educated discourse — Sisyphus, Midas, Persephone, Icarus — functioned as compressed reasoning artifacts. They were not mere allusions. They were shared models, compressed into a word or a phrase, that enabled high-bandwidth communication about complex situations. To invoke "Sisyphean" was to activate, in the listener's mind, a complete model of futile but compelled effort — with its emotional topology, its moral ambiguity, its recognition of the absurd. The word was a pointer to a shared theory.

When the canon fragments — when the compression dictionary is no longer shared — you don't just lose the references. You lose the capacity for certain kinds of collective reasoning, because the shared models that enabled it are gone. The references were the reasoning artifacts. The cultural conversations they enabled were the products. We kept some of the products (the insights, the values, the habits of thought) but lost the artifacts that produced them, and now we struggle to produce new ones of the same kind. This is Naur's maintenance nightmare applied to a civilization.

---

## The Inversion

The most important artifact is never the final product. It is always the reasoning that produced it.

Code, hardware, recommendations, verdicts, clinical diagnoses, legal decisions, strategic plans — these are residue. Valuable residue, necessary residue, but residue. The theory, the model stack, the deliberation record, the story of why this and not that — these are what carry understanding forward. They are what make the product maintainable, evaluable, and improvable. Without them, the product is a mystery in working order — useful until the first time you need to change it or explain it or decide whether it's still the right product for a changed world.

Every tradition that has taken this problem seriously has arrived at the same conclusion. Naur said it about programs. Watson said it about systems. We found it in committee pipelines. Brooks said it about conceptual structures. Dijkstra said it about mathematical reasoning. Coles found it in literature courses that produced better doctors. Pask built it into the definition of understanding itself. The canonical literary traditions encoded it in shared myths that compressed entire models into a word.

The agent era brings one new thing to this old insight: speed. Agents generate artifacts faster than any previous tool. Code, reports, analyses, recommendations — all flowing at the speed of token completion, all plausible, all theory-less. The temptation is to let the speed carry you. To accept the residue and skip the reasoning. To treat the agent as a faster engineer rather than as a fast generator of theory-less artifacts that need a human theory-builder to be useful.

The claim these three traditions converge on is also a warning: *the faster you can produce artifacts, the more important it becomes to produce reasoning first.* The reasoning doesn't slow you down. It's the only thing that keeps you from going fast in the wrong direction.

Eisenhower said plans are useless, but planning is essential. He was right, and the principle generalizes. The plan is the artifact; the planning is the reasoning. The code is the artifact; the theory is the reasoning. The recommendation is the artifact; the deliberation is the reasoning. In every case, the thing you're tempted to optimize for is the less important thing. The thing you're tempted to skip is the thing that matters.

The agent can help you build the reasoning. It is a genuinely useful conversational partner for exploring problem spaces, surfacing assumptions, generating alternatives, stress-testing positions. But it cannot hold the reasoning for you. That's yours to build, yours to maintain, yours to carry forward when the artifacts need to change.

The handle must be in your hand before the blade arrives.

---

**Related essays:**
- [Why Narrative Engines Change Everything](./01-why-narrative-engines-change-everything.md) — the paradigm shift that makes reasoning artifacts necessary
- [From Practice to Theory](./02-from-practice-to-theory.md) — how operational failures led to the methodology
- [Stories All the Way Down](./stories-all-the-way-down.md) — stories as the models that carry understanding
- [The Blade Without a Handle](./blade-without-a-handle.md) — the vicious circle of outsourcing the theory-building step
- [Decisions Under Uncertainty](./10-decisions-under-uncertainty.md) — the fan/funnel architecture that produces deliberation records

**References:**
- Naur, P. (1985). "Programming as Theory Building." *Microprocessing and Microprogramming* 15: 253–261.
- Watson, M.D., Mesmer, B.L., Farrington, P.A. (2020). *Engineering Elegant Systems: Theory of Systems Engineering.* NASA/TP–20205003644.
- Brooks, F. (1975/1995). *The Mythical Man-Month.* Addison-Wesley.
- Brooks, F. (1986). "No Silver Bullet: Essence and Accidents of Software Engineering."
- Dijkstra, E.W. (1988). "On the Cruelty of Really Teaching Computer Science." EWD-1036.
- Coles, R. (1989). *The Call of Stories: Teaching and the Moral Imagination.* Houghton Mifflin.
- Pask, G. (1976). *Conversation Theory: Applications in Education and Epistemology.* Elsevier.

---

*For everyone who ever inherited a codebase and wished someone had written down why.*
