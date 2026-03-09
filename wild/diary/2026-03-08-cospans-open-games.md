# Diary: 2026-03-08

*For wild/ — exploratory, not a status report.*

---

A conversation today that kept surprising me, which is usually a sign
something is actually happening.

---

## The generalization ladder

Started with a question about extending the palgebra — whether hypergraphs
and decorated cospans are worth the audience cost. But the more interesting
thing that emerged was a way of seeing the existing formalism as one rung
on a generalization ladder that has a clear shape:

**Kalman filter** → assumes linear Gaussian dynamics, observable state,
fixed noise model. The gold standard for estimation when the world
cooperates.

**Bayesian state estimation (nonlinear)** → relaxes Gaussian and linearity
assumptions. Particle filters, unscented transforms. The state is still
Markovian, the objective still fixed.

**MDPs / reinforcement learning** → relaxes the assumption that you know
the dynamics. The agent learns the model or learns a policy directly. But
the state space is still assumed well-defined and the objective is still
a fixed reward function.

**Open games / compositional game theory** → relaxes the fixed-objective
assumption. Players have selection functions, not utility functions.
Decisions compose. The setting is explicitly open: a game has boundary
interfaces through which it plugs into a larger system. This is where
cospans live — they're the formalism for those interfaces.

**Cyberneutics** → relaxes the assumption that the state space is
well-defined in the first place. Wicked problems. The fan generates
candidate state spaces (scenarios); the funnel commits to one
interpretation. The methodology is the act of making the state space
tractable enough to decide in, not of optimizing within a given one.

Each step is a generalization that drops one assumption and gains
expressive power at the cost of tractability. The Kalman filter has
closed-form solutions. Open games have compositional semantics but
no general solution procedure. Cyberneutics has visible reasoning
chains but no guarantee of correctness — only of inspectability.

This is worth writing up as an essay. The engineering audience will
recognize the progression. The category theory audience will recognize
the pattern of relaxing constraints to get universal properties. It
might be the clearest single argument for why the formalism has the
shape it does.

---

## The control systems parallel

The open games framing looks a lot like a control system when you squint.
Context function = plant model (maps inputs to outputs). Selection
function = control law (maps observations to actions). Composition of
games = cascade or feedback connection of controllers. The cospan is the
typed interface between plant and controller.

This is not a coincidence. The lens formulation of open games makes the
parallel explicit: a lens is a get/put pair, which is exactly the
structure of an observer-controller system. Read the state, write a
control signal. The category theory here is not decorative — it's
capturing something that was always latent in control theory but never
made compositional.

The remediation loop in cyberneutics is literally a feedback controller:
the evaluator measures the transcript, computes an error signal (rubric
deficit), and feeds it back to the committee (the plant). The committee
produces a new transcript. The loop runs until the evaluation passes
or the iteration budget is exhausted. That's a sampled-data control
system. The palgebra's confidence propagation is the stability condition:
confidence can only degrade, so the loop has a natural stopping criterion.

I hadn't fully seen the remediation loop as a controller before. Worth
making explicit in the palgebra.

---

## Decorated cospans vs. hypergraphs: the verdict

Decorated cospans: worth it. The fan/funnel composition needs a proper
formal treatment and cospans are the right vocabulary. The payoff is
real — it turns an informal monad metaphor into a precise categorical
statement. The audience cost is lower than feared: engineers who have
internalized the resource theory framing are actually close to needing
cospans already. The concept of a typed interface is not alien to them.

Hypergraphs: hold. No concrete modeling problem currently strains against
the monoidal structure. Adding them preemptively reads as formalism for
its own sake. Revisit if a genuine multi-input-multi-output bottleneck
appears in the pipeline descriptions.

---

## Two audiences, two registers

Thinking about how to position the palgebra extension for two very
different communities:

One community: applied category theorists, people who work on
compositional game theory, polynomial functors, open systems. For
them, the current resource theory framing is competent but conservative.
They will immediately see where it's going and wonder why it stopped.
They won't be put off by cospans — that's their vocabulary. The question
for them is whether the analogy between the committee structure and open
games is genuinely functorial or just a suggestive metaphor.

My intuition: it might be genuinely functorial. Each committee character
is not a utility maximizer — they have a fixed worldview lens and a
selection function that is agnostic about decision theory. The scenario
set is the context function. The resolution is equilibrium selection.
The composed fan/funnel is an open game. If that's right, it's a
real mathematical result, not a metaphor.

Other community: computational social scientists, information
environment researchers, people studying how narratives propagate and
how multi-agent systems produce collective sense-making. For them, the
math is beside the point. What lands is the empirical claim: that
structured multi-perspective deliberation produces more inspectable
reasoning than single-model outputs, and that inspectability matters
for contested information environments. The committee as a requisite
variety machine. Adversarial robustness as epistemic hygiene.

These communities don't overlap much, which means they won't confuse
each other's registers. The repo can serve both without one audience
finding the other's material alienating — as long as the paths are
clearly marked.

---

## The on-ramp problem and wild/

A contributor's pull request closed without a conversation today. The
contributor was doing exactly the right kind of lateral thinking —
connecting an external theoretical perspective to the project's existing
work — and the guidelines read as a door instead of a window.

The `wild/` directory is the right answer. It already functions this
way: neo-cybernetics, residuality theory, harness engineering — all
started there as unfinished ideas before being tamed into the main
corpus. The pipeline is: wild → diary → essays/artifacts/palgebra.
But that pipeline is invisible in the contributor-facing docs.

The deeper issue: the methodology itself was developed through
exploratory lateral walks, not structured research programs. The
contribution model should reflect how the work actually gets done,
not an idealized research workflow. Agents need structure; humans
need an on-ramp that acknowledges partial ideas as legitimate starting
points.

Moving the diary into wild/ makes sense as a signal: the wildest
ideas live here, and that's not a defect, it's where things start.

---

## The library

1,255 books currently catalogued. Adding more tomorrow. Notably present:
the Dervin sense-making reader (direct hit), both von Foerster volumes,
Wiener, the applied category theory shelf (Fong/Spivak, Riehl, Awodey),
Kahneman, Waldrop and Mitchell on complexity, Holland's Signals and
Boundaries. West's Scale. The full SFI complexity lineage is
represented.

Notably absent: the Fong thesis (decorated cospans), Haykin on adaptive
filters, Bertsekas/Shreve on stochastic optimal control, the Hedges
papers on open games. These are the books the palgebra extension most
needs. Worth acquiring.

The adaptive filtering shelf is thin: Optimal State Estimation (Dan
Simon), Papoulis, a few stochastic processes texts. No Kalman filter
dedicated texts. No particle filter literature. Given the generalization
ladder above, the control/estimation literature is foundational — not
just background, but the first rung of the argument.

---

## Open threads from today

- Write the generalization ladder essay (Kalman → open games →
  cyberneutics). Both audiences can use it.
- Make the remediation loop's control-system structure explicit in
  the palgebra. It's not currently stated.
- Investigate whether the committee/open-games analogy is genuinely
  functorial. Read the 2016 morphisms paper and the earlier
  compositional game theory paper. Then decide whether to extend
  the palgebra to cospans or wait for the confirmation.
- Run the committee deliberation on contributor experience.
  Brief is ready.
- Consider the diary's relocation to wild/ as part of the same
  remediation — signals that the wildest ideas are welcome, not
  just the tamed ones.
- The selection function framing (agnostic about decision theory)
  is important for the Hedges outreach. The characters are not
  utility maximizers. This distinguishes cyberneutics from
  generic game-theoretic framing and is where selection functions
  become interesting over expected utility.
