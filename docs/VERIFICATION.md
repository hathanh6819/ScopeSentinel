# Verification

## Local V2 results — 2026-10-09

| Layer | Command | Result |
|---|---|---|
| Contract direct/adversarial | `python -m pytest tests -q` | 24 passed |
| GenVM compatibility | lint `contracts/scope_sentinel.py` and `contracts/guarded_executor.py` | passed, 3 checks each |
| Frontend state rules | `npm test` | 3 passed |
| Production frontend | `npm run build` | passed |

## Behavioral coverage

- permissionless proposal creation and no constructor roles;
- input and manifest schema/bounds;
- active parent, digest and revision binding;
- deterministic manifest diff;
- complete manifest schema, calldata commitment, chain/window validation;
- atomic queued authorization and finalized cross-contract message;
- executor sender authentication, allocation effect, and receipt replay rejection;
- fully disclosed and editorial certification;
- positive-model bypass killed when action change is not disclosed;
- hidden material change blocked;
- malformed/unknown consensus fail-closed and retryable;
- prompt injection handled as inert evidence;
- creator-only activation;
- blocked activation, stale activation, replay and cross-object rejection;
- failure paths assert no relevant mutation.

## Historical V1 live release gate

Complete for historical V1 programmatic SDK E2E on `0xA198744fd4A6479019EEea2E27195f8546EDB176`. This does not evidence the V2 execution-boundary fix and must not be used for resubmission.

- Exact address and deployment transaction recorded.
- Two ordinary test wallets exercised independent creator/reviewer roles; deployer has no protocol authority.
- All 11 lifecycle, failure and adversarial calls finalized.
- Happy assessment reached `MAJORITY_AGREE` and `FULLY_DISCLOSED`; activation updated the exact active parent/child atomically.
- Hidden recipient/amount change reached `HIDDEN_MATERIAL_CHANGE` and `BLOCKED`.
- Stale, unauthorized, replay and blocked-activation attempts preserved protected state.
- Final readback: 2 proposals, 4 revisions, 2 assessments.

Explorer links and readbacks: [`LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md). Browser-wallet automation is not claimed.

## V2 live release gate

Pending new ScopeSentinel and GuardedScopeExecutor deployment, two-wallet E2E, downstream allocation readback, frontend address update, and Cloudflare publication.
