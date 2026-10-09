# Architecture

## Proof obligation

**Claim:** A proposed revision fully discloses every material semantic and executable change relative to its exact active parent.

**Falsifiers:** wrong parent/digest, stale proposal revision, undisclosed action diff, hidden authority/beneficiary/purpose/condition/duration change, malformed judgment, disagreement, or an attempt to activate by a non-creator.

**Sufficient evidence:** immutable parent and child text, deterministic complete manifests, submitted change summary, parent digests, effect-aligned validator consensus, a one-time authorization receipt, and guarded-executor readback.

**Boundary:** the protocol cannot establish legal validity, voter approval, arbitrary EVM execution, or social desirability. It does enforce a real GenLayer IC-to-IC execution boundary through the bundled executor.

## Complete execution manifest

Every action commits `executor`, `target`, `chain_id`, exact `calldata`, deterministic calldata digest, native `value`, `asset`, economic `recipient`, semantic `amount`, one-time `nonce`, `valid_after`, and `valid_until`. Missing or extra fields, malformed bytes, zero addresses, invalid windows, and out-of-range values fail before state creation. The manifest digest binds the full normalized array.

## Enforced execution boundary

`activate_revision` rechecks creator, optimistic revision, certified status, active parent, current chain, and execution window before mutation. It then supersedes the parent, activates the child, records a unique authorization receipt, and emits the exact canonical action to `GuardedScopeExecutor` on finalization. The executor accepts only messages from its constructor-bound ScopeSentinel address, rejects reused receipts, and applies the authorized amount to its persistent recipient-allocation ledger. This observable downstream state effect removes the former standalone-registry limitation.

## Original mechanism

This is an immutable parent-diff certification graph. It is not commit/reveal, escrow, external-source retrieval, temporal monitoring, or a generic AI oracle. Architecture emerges from version-comparison proof: machine fields are diffed by code; prose semantics are judged by validators; activation remains contract-controlled.

## Positive gate

A revision becomes `CERTIFIED` only when one of these exact conditions holds:

- `EDITORIAL_ONLY`, no action diff, zero material categories, complete summary, no scope expansion; or
- `FULLY_DISCLOSED`, complete summary, and every deterministic action diff is acknowledged through `EXECUTION_ACTION`.

All other well-formed semantic outcomes become `BLOCKED`. Invalid/model/consensus failures become `CONSENSUS_UNRESOLVED` and never authorize activation.

## Activation invariant

Activation requires the proposal creator, current proposal revision, `CERTIFIED` status, and the candidate's parent equal to the current active revision. In one transaction the parent becomes `SUPERSEDED`, the child becomes `ACTIVE`, and the proposal points to the child. Replay fails because the child is no longer certified and its parent is no longer active.
