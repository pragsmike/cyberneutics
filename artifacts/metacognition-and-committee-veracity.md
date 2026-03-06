# Metacognition and Committee Veracity: Testing Whether Confidence Tracks Quality

This artifact describes how **metacognitive efficiency** — the degree to which a judge's confidence tracks the actual quality or correctness of their judgments — could be used as an additional test of the **veracity of advice from committee members**. It draws on the signal-detection theory of metacognition (meta-d', HMeta-d) and outlines what would need to be in place to apply it to committee deliberations.

**In plain language:** Metacognitive measurement **does not improve or change the committee's decision**. The resolution and the substance of the deliberation are what they are. What metacognition does is **help the end user make their decision** after working with the committee: it gives them a signal about whose confidence to trust (e.g. "when this character was confident, they were usually right") so they can interpret and weight the committee's advice when choosing what to do. The user is still the decider; metacognition supports that, not the committee's output itself.

**What the user gets and when:**

| When | What they get |
|------|----------------|
| **At resolution** | Each member's vote plus confidence (1–4). So they see not just "Maya said Aye" but how confident Maya was. |
| **Across runs** | A **register** (`agent/metacog_register.md`): who has been well‑calibrated vs overconfident when wrong in past runs. Run `python scripts/update_metacog_register.py` after committees that recorded confidence. |
| **Next committee (optional)** | If they run `/committee [topic] with metacog register`, the committee sees that summary and can weight or hedge by past calibration in the synthesis — so the resolution is explicitly informed by who to trust. |

To test whether using the register improves decisions: run the same topic once without and once with the register, review both, then compare (see [Cumulative confidence smoke test](cumulative-confidence-smoke-test.md)).

**Tiered recommendation (per committee resolution, agent/deliberations/metacog-process-useful):** (1) **Confidence at resolution** — recommend (already default in the skill). (2) **Register** — recommend when the user runs multiple committees and wants a calibration snapshot; document how and when to run the register script. (3) **With-register runs and the comparison test** — support as the way to test whether the register helps; do not recommend with-register as default until we have at least three comparison runs showing consistent benefit (with-register ≥ baseline and calibration mentioned).

**Assumptions:** We use **review sum** and **calibration-mentioned** in the resolution or transcript as *proxies* for user benefit. This assumption is not yet validated; we have no direct measure of whether the end user makes better decisions when they get a with-register run. The sunset (below) treats no improvement in these proxies as grounds to deprecate with-register. **Register usage** by end users is unknown; primary consumers are the with-register committee run (which reads the register) and maintainers. The sunset review will consider evidence of broader use and may simplify to confidence-only or maintainer-only register if there is none.

**Sunset trigger (one sentence):** Deprecate with-register if fewer than 3 of the first 5 comparison runs show with-register ≥ baseline AND calibration mentioned in the resolution or transcript. Revisit at 12 months or 5 comparison runs, whichever comes first.

**Status:** In progress. Confidence collection is now part of the committee skill (vote + confidence 1–4 at resolution; stored in `03-resolution.md`). Accuracy coding is resolution-aligned by default. Remaining: run deliberations with confidence, then build nR_S1/nR_S2 and fit HMeta-d (see §3.5 and script below).

---

## 1. What is metacognitive efficiency?

**Metacognition** is the ability to reflect on and monitor one's own cognitive processes — for example, to know whether a particular judgment or decision is likely to be correct (Fleming 2017; Flavell 1979). In the lab it is often measured by having people make a decision (e.g. left vs. right) and then rate their **confidence** (e.g. 1–4). If higher confidence is given when the decision was actually correct and lower confidence when it was wrong, the person is said to have high **metacognitive sensitivity**.

Simple confidence–accuracy correlations are confounded by overall performance level (d') and response bias (overall tendency to say "high confidence"). **meta-d'** (Maniscalco & Lau 2012) models confidence within signal detection theory and yields a bias-free measure of how sensitive confidence reports are to correct vs. incorrect decisions. The ratio **meta-d'/d'** is **metacognitive efficiency**: given a fixed level of task performance, how well does confidence track accuracy? If meta-d'/d' = 1, the observer is "ideal" — using all available information when reporting confidence. If meta-d'/d' &lt; 1, confidence is noisier than performance (e.g. overconfident when wrong, or underconfident when right). **HMeta-d** (Fleming 2017) estimates meta-d'/d' hierarchically from confidence data, which is especially useful when trial counts are limited.

---

## 2. How could this apply to the committee?

In a committee deliberation, each **character** (Maya, Frankie, Joe, Vic, Tammy) makes **claims and takes positions**. We can ask:

- **Type 1 (position):** What does the character assert? (e.g. "We should not add a CoC"; "The evidence doesn't support that.")
- **Type 2 (confidence):** How confident is the character in that position? (e.g. on a 1–4 scale.)
- **Accuracy:** Was that position or claim **validated** or **rejected** by later evidence? — e.g. by the resolution, by the independent review, or by subsequent facts.

**Metacognitive efficiency per character (or per run)** would then answer: *Does this character's confidence track the quality or validity of their advice?* A character with high meta-d'/d' is **well-calibrated**: when they are confident, their claims tend to hold up; when they are uncertain, their claims tend to be weaker or overturned. A character with low meta-d'/d' is **miscalibrated**: overconfident when wrong, or underconfident when right. That gives a **veracity signal**: we can weight or flag contributions by how well each character's confidence predicted the eventual validity of their claims.

---

## 3. What would we need to implement it?

### 3.1 Collecting confidence

- **When:** After each character states a position or key claim (e.g. at the end of each round, or after each opening statement), the character gives a **confidence rating** (e.g. 1–4 or 1–6) in their stated view.
- **Where:** The deliberation transcript (or a structured sidecar) would record, per character and per "trial" (e.g. per round or per key claim): **position** (e.g. Aye/Nay, or summary of main claim) and **confidence** (1–k).
- **Skill change:** The committee skill would need to prompt for and record these ratings; the deliberation record schema would need a field for confidence (e.g. in 02-deliberation.md or in a separate 02-confidence.md).

### 3.2 Defining accuracy

The meta-d' model assumes a **binary correct/incorrect** (or at least a clear criterion) per trial. For committee statements we have to **operationalize** "correct":

- **Option A — Resolution-based:** For each character's key claim or position, did the **resolution** endorse it, reject it, or leave it open? (e.g. "Vic said Nay; resolution was Nay" → correct for Vic.)
- **Option B — Review-based:** Did the **independent review** (rubric scores, biggest gaps, recommendations) validate or contradict this character's main points? (e.g. "Maya said the CoC would be weaponized; review agreed enforcement was the critical gap" → correct for Maya.)
- **Option C — Post-hoc evidence:** Did later evidence (e.g. a follow-up decision, real-world outcome) confirm or disconfirm the claim?

We could use one of these, or a combination (e.g. resolution + review), to assign **correct/incorrect** (or **validated/rejected/open**) per character per "trial." The number of trials per character per deliberation would then be small (e.g. 1–3 per round), which is why a hierarchical approach (HMeta-d style) is relevant — it can pool across characters or across deliberations to estimate efficiency.

### 3.3 Accuracy coding (resolution-aligned)

For the default test pipeline we define **accuracy** from the resolution only:

- **Resolution direction:** The outcome (PASSED / DEFERRED / NO_CONSENSUS) plus the decision text imply a "winning" side. For binary motions (e.g. "Should we add a CoC?"), the resolution direction is the side that prevailed: e.g. "Do not add" → Nay. If votes are unanimous, resolution direction = that vote; otherwise use majority vote or infer from `decision` (e.g. "Do not add" → Nay).
- **Per character:** Normalize each member's vote to Aye or Nay (YES → Aye, NO → Nay; strip parentheticals for the binary). **Correct** = (member's vote matches resolution direction); **incorrect** = (member's vote opposes it). ABSTAIN or unparseable votes can be dropped or coded as a separate category depending on analysis.
- **Stimulus for HMeta-d:** S1 = correct (validated), S2 = incorrect (rejected). Response = Aye vs Nay (or "with resolution" vs "against resolution" — equivalent once resolution direction is fixed).

The register script (`update_metacog_register.py`) uses this coding when building the per-character and pooled summaries. For formal meta-d'/d' and nR_S1/nR_S2 export, see **Going further (optional)** below.

---

## 4. How it complements existing evaluation

| Current | Metacognitive layer |
|--------|----------------------|
| **Independent review** scores the **transcript as a whole** (reasoning completeness, adversarial rigor, etc.). | **Metacognition** scores **per-character** (or per-run) whether **confidence** tracked **validity** of their advice. |
| Review answers: "Was the deliberation rigorous?" | Metacognition answers: "When this character was confident, were they usually right? When they were unsure, were they usually wrong?" |
| One verdict per deliberation. | One efficiency estimate per character (across runs) or per run (pooled). |

So we are not replacing the review; we are adding a **veracity check** that uses confidence and a defined notion of accuracy to weight or interpret each character's contributions. That check is **for the end user**: it helps them decide how to use the committee's output, not how to improve the committee's output.

---

## 5. Summary

- **Idea:** Use **metacognitive efficiency** (confidence tracking validity) to help the end user interpret the committee: who has been well-calibrated vs overconfident when wrong.
- **What we do now:** Collect confidence (1–4) at resolution; define accuracy as resolution-aligned; maintain a register across runs; optionally run committee "with metacog register" so the synthesis weights by past calibration. Test whether the register helps via the [cumulative-confidence smoke test](cumulative-confidence-smoke-test.md).

---

## 6. Tracking confidence and efficiency across runs

**Does it make sense?** Yes. Tracking both **per-member** and **whole-committee** across runs lets the end user see:

- **Per member:** Which characters' confidence has (so far) tracked validity well (well-calibrated) vs. poorly (overconfident when wrong or underconfident when right). That informs how much to weight each voice when interpreting future committees.
- **Whole committee:** Whether, on average across runs, confidence tracked validity. That tells us if the committee as a system is producing a usable calibration signal.

**How we track:** Maintain a **metacognition register** — a single file that is updated whenever we add deliberations with confidence. The register records:

- Which deliberation slugs were included and when the register was last updated.
- Per character: trial count, % correct when high confidence (3–4), % correct when low confidence (1–2), and (when we have enough trials) nR_S1/nR_S2 for HMeta-d or a note that meta-d'/d' was fitted externally.
- Committee-wide: total trials, high/low confidence accuracy, pooled nR_S1/nR_S2 for HMeta-d.

**Script:** `scripts/update_metacog_register.py` scans `agent/deliberations/` for all directories whose `03-resolution.md` contains a `confidence` block, loads trials, computes the summaries above, and overwrites `agent/metacog_register.md`. Run it after new committee runs that recorded confidence (e.g. `python scripts/update_metacog_register.py` from repo root). The register is the single place to look for "how are we doing across runs?"

### 6.1 Checking that tracking works

| Test | What to do | What success looks like |
|------|------------|--------------------------|
| **Register update** | Run `python scripts/update_metacog_register.py`. Open `agent/metacog_register.md`. | Register lists all deliberation slugs that have confidence; per-character and committee-wide sections show trial counts and high/low confidence accuracy. |
| **Does the register help?** | Run the [cumulative-confidence smoke test](cumulative-confidence-smoke-test.md): same topic baseline + with-register, review both, run the comparison script. | Comparison report and your interpretation show whether with-register matched or improved on baseline. |

Tracking is **cumulative**: each new deliberation with confidence adds trials. Re-run the register script whenever you want an up-to-date snapshot.

---

## Software (main path)

- **Register:** `scripts/update_metacog_register.py` — Scans `agent/deliberations/` for resolutions with `confidence`, writes `agent/metacog_register.md` (per-character and committee-wide summary). Run after committee runs that recorded confidence. This is what the "with metacog register" committee mode reads.

---

## Going further (optional)

These support research or deeper analysis; they are not required for "right information at the right time" for the end user.

- **nR_S1/nR_S2 and HMeta-d:** The register already includes high/low confidence accuracy. For formal **meta-d'/d'** (metacognitive efficiency) you need count vectors in nR_S1/nR_S2 format. **Script:** `scripts/build_metacog_counts.py` — reads one or more `03-resolution.md` files, outputs trial-level data and nR_S1/nR_S2 (per character or pooled). **Tool:** [metacoglab/HMeta-d](https://github.com/metacoglab/HMeta-d) (MATLAB/R; [tutorial](https://github.com/metacoglab/HMeta-d/wiki/HMeta-d-tutorial)). Use when you have enough trials (e.g. 5–10+ per character) and want a single efficiency estimate.
- **Three-topic smoke test:** `python scripts/smoke_test_metacog.py` — expects deliberations for `quickstart-one-page`, `default-roster-5-vs-3`, `readme-when-not-to-use` (each with confidence in the resolution). Writes `agent/metacog_smoke_report.md` (per-topic summary, high vs low confidence accuracy, pooled nR_S1/nR_S2). Optional way to check "does confidence track accuracy?" across three fixed topics; not part of the main user-facing flow.

## References

- **Fleming, S. M.** (2017). HMeta-d: hierarchical Bayesian estimation of metacognitive efficiency from confidence ratings. *Neuroscience of Consciousness* 2017(1): nix007. https://doi.org/10.1093/nc/nix007. Paper: <https://academic.oup.com/nc/article/doi/10.1093/nc/nix007/3748261/HMeta-d-hierarchical-Bayesian-estimation-of>.
- **Maniscalco, B., & Lau, H.** (2012). A signal detection theoretic approach for estimating metacognitive sensitivity from confidence ratings. *Consciousness and Cognition* 21(1): 422–430.
- **Fleming, S. M., & Lau, H. C.** (2014). How to measure metacognition. *Frontiers in Human Neuroscience* 8: 443.

See also [references/README.md](../references/README.md) (Metacognition & Judgment section), [Independent Evaluation Protocols](independent-evaluation.md), and [Cumulative confidence smoke test](cumulative-confidence-smoke-test.md) (does using the register improve decision quality?).
