# Threat model

| Threat | Control |
|---|---|
| “Formatting only” hides recipient/amount/target change | Deterministic manifest diff plus mandatory `EXECUTION_ACTION` disclosure |
| True evidence from proposal A reused for proposal B | Revision and assessment bind proposal ID, parent ID and exact digests |
| Revision built on stale parent | Active-parent and expected-revision gates |
| AI says positive despite action mismatch | Contract-level positive gate overrides model output |
| Prompt injection in proposal text | Text marked inert; exact schema, bounded enums and deterministic enforcement |
| Validator malformed output/disagreement | Audited `CONSENSUS_UNRESOLVED`; no privilege |
| Reviewer activates someone else's proposal | Only per-proposal creator may activate |
| Certified revision replay | Atomic status transition and active-parent update |
| Partial manifest hides actual bytes or execution context | Exact calldata, chain, executor, destination, value, nonce and validity window are mandatory and digest-bound |
| Registry certificate ignored by execution layer | Activation emits a finalized message to a guard-bound executor |
| Direct or replayed executor call | Executor authenticates ScopeSentinel sender and rejects used authorization receipts |
| Wrong chain or expired authorization | Activation checks current chain and validity window before any state mutation |
| Frontend uses aggregate counter as selected object | IDs are returned/read from proposal records and selected through cards |
| UI reports submission as success | Client waits `FINALIZED`, checks execution/consensus, then refreshes state |

Residual risk: semantic consensus may misclassify subtle prose. A proposer can write misleading baseline text, but cannot claim this protocol validates external facts—the only proved relation is between exact on-chain versions.
