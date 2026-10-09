# More information for resubmission

## Steward request

> The app is limited by its standalone registry boundary and incomplete execution manifest.

## Changes made

1. Replaced the partial six-field action record with a strict complete manifest containing the guarded executor, effect target, chain ID, exact raw calldata, contract-computed calldata SHA-256 commitment, native value, asset, economic recipient, semantic amount, one-time nonce, and `valid_after`/`valid_until` window.
2. Added fail-closed schema validation. Missing/extra fields, malformed calldata, zero executor/target, invalid asset/address, negative or excessive values, invalid nonce, and invalid windows cannot create a proposal or revision.
3. Added deterministic diff categories for executor, target, chain, calldata, value, asset, recipient, amount, nonce, and both validity bounds. A model cannot conceal any of these changes.
4. Removed the standalone-registry boundary. Certified activation now creates an immutable execution record and sends the exact canonical action plus authorization receipt to a downstream Intelligent Contract on finalization.
5. Added `GuardedScopeExecutor`, whose constructor binds the ScopeSentinel address. It rejects direct callers and duplicate authorization receipts, persists an `EXECUTED` readback tied to proposal, revision, manifest digest, and exact action, and applies the approved amount to its persistent recipient-allocation ledger as an observable downstream effect.
6. Added pre-mutation chain and execution-window checks, atomic parent supersession/child activation, and one-time receipt generation.
7. Updated the frontend to collect the complete manifest and show queued-execution counts instead of presenting the app as a passive registry.
8. Expanded tests for incomplete manifests, wrong-chain activation, zero mutation on failure, downstream message emission, execution-record creation, and replay protections. Current local result: 22 contract/adversarial tests, both GenVM lint targets, 3 frontend tests, and production build pass.

## Evidence still required before resubmission

Deploy the updated ScopeSentinel contract, deploy `GuardedScopeExecutor` with the new ScopeSentinel address, run the two-wallet happy/failure/adversarial/replay lifecycle, confirm the executor readback, update production to both active addresses, and replace the prior V1 transaction evidence. The older live address remains documented honestly and must not be presented as evidence for these V2 changes.
