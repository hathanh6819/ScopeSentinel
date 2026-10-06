# Architecture

## Proof obligation

**Claim:** A proposed revision fully discloses every material semantic and executable change relative to its exact active parent.

**Falsifiers:** wrong parent/digest, stale proposal revision, undisclosed action diff, hidden authority/beneficiary/purpose/condition/duration change, malformed judgment, disagreement, or an attempt to activate by a non-creator.

**Sufficient evidence:** immutable parent and child text, deterministic bounded manifests, submitted change summary, parent digests, and effect-aligned validator consensus.

**Boundary:** the protocol cannot establish legal validity, voter approval, external execution, or social desirability.

## Original mechanism

This is an immutable parent-diff certification graph. It is not commit/reveal, escrow, external-source retrieval, temporal monitoring, or a generic AI oracle. Architecture emerges from version-comparison proof: machine fields are diffed by code; prose semantics are judged by validators; activation remains contract-controlled.

## Positive gate

A revision becomes `CERTIFIED` only when one of these exact conditions holds:

- `EDITORIAL_ONLY`, no action diff, zero material categories, complete summary, no scope expansion; or
- `FULLY_DISCLOSED`, complete summary, and every deterministic action diff is acknowledged through `EXECUTION_ACTION`.

All other well-formed semantic outcomes become `BLOCKED`. Invalid/model/consensus failures become `CONSENSUS_UNRESOLVED` and never authorize activation.

## Activation invariant

Activation requires the proposal creator, current proposal revision, `CERTIFIED` status, and the candidate's parent equal to the current active revision. In one transaction the parent becomes `SUPERSEDED`, the child becomes `ACTIVE`, and the proposal points to the child. Replay fails because the child is no longer certified and its parent is no longer active.
