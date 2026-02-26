# Evaluating Deliberative Architectures: The Black Swan Hindsight Framework

**Contributing to this program**
*   **Skills needed:** LLM prompt automation, historical research, qualitative evaluation.
*   **Scope:** 1-2 weeks for dataset construction and initial trials.
*   **Entry point:** Design the historical situation dataset and run initial baseline responses against a committee.

---

## 1. Problem Statement

Testing deliberative architectures (such as adversarial committees and peer-agent networks) is inherently difficult because they are applied to "wicked problems" — situations where there is no definitively "correct" answer at the time of the decision. Without ground truth, evaluating whether an architecture performed well often devolves into evaluating whether we simply liked its output.

## 2. Experimental Design: The Hindsight Framework

The evaluation framework uses historical hindsight to solve the ground-truth problem. While black swans and complex systemic shocks are unpredictable in the moment, they are often obvious in retrospect. A decision point that was genuinely uncertain at the time becomes legible after the fact. 

This suggests a robust three-stage experimental design:

### Stage 1: Select Historical Wicked Situations
Identify historical scenarios where the "black swan" or complex outcome is now visible. The decision point must be clear, the ramifications must have played out, and a rich, reconstructable causal record must exist. 
*Note: Granular organizational or localized strategic decisions are preferred over iconic historical events, to prevent the LLM from simply pattern-matching to known historical outcomes.*

### Stage 2: Run the Fan (Deliberation)
Present the historical situation, bounded strictly to the knowledge available at the time, to different committee configurations and execution architectures (e.g., single Claude response vs. Hub-and-Spoke Committee vs. Peer-Agent Committee). Collect their recommended actions and the reasoning paths that led to them.

### Stage 3: Play Out the Ramifications
Feed each chosen action to an impartial evaluator model. This model should be blind to which architecture produced the action. Instruct it to simulate the forward consequences of that action, using the actual historical record as its knowledge base. 

## 3. Evaluation Metrics

This design evaluates not just whether the "right" action was chosen, but the quality of the reasoning trail. We evaluate:

*   **Anticipation:** Which committee configurations saw the black swan coming?
*   **Epistemic Humility:** Which architectures were confidently wrong, and which were appropriately uncertain about the unknowns?
*   **Decision Landscape Topology:** By running the identical situation through multiple committee variations, we observe variance. High variance indicates a decision hovering near a critical boundary where small assumptions flip outcomes. Consistent convergence indicates a robustly settled basin.

## 4. Specific Test Cases

*   **The Glenda/Crock Coercion Scenario:** Use the [coercion scenario](../../applications/narrative-immune-systems/glenda-crock-coercion.md) to test which alignment structures (single agent vs. committee roles) successfully identify adversarial narrative framing.
*   **The Blast Radius Problem:** Use infrastructure deployment scenarios (e.g., the declarative NixOS fleet management problem) to test whether undifferentiated "developer" agents can anticipate asymmetric failure modes compared to a committee containing a dedicated "Operator/Tester" role.

---

## Status
*   **Status:** Not started.
*   **Runs:** None yet.
*   **Findings:** N/A.
