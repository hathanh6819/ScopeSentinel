# Verification

## Local results — 2026-10-06

| Layer | Command | Result |
|---|---|---|
| Contract direct/adversarial | `python -m pytest tests -q` | 20 passed |
| GenVM compatibility | `python -X utf8 -m genvm_linter.cli contracts/scope_sentinel.py` | passed, 3 checks |
| Frontend state rules | `npm test` | 2 passed |
| Production frontend | `npm run build` | passed |

## Behavioral coverage

- permissionless proposal creation and no constructor roles;
- input and manifest schema/bounds;
- active parent, digest and revision binding;
- deterministic manifest diff;
- fully disclosed and editorial certification;
- positive-model bypass killed when action change is not disclosed;
- hidden material change blocked;
- malformed/unknown consensus fail-closed and retryable;
- prompt injection handled as inert evidence;
- creator-only activation;
- blocked activation, stale activation, replay and cross-object rejection;
- failure paths assert no relevant mutation.

## Live release gate

Complete for programmatic SDK E2E on `0xA198744fd4A6479019EEea2E27195f8546EDB176`.

- Exact address and deployment transaction recorded.
- Two ordinary test wallets exercised independent creator/reviewer roles; deployer has no protocol authority.
- All 11 lifecycle, failure and adversarial calls finalized.
- Happy assessment reached `MAJORITY_AGREE` and `FULLY_DISCLOSED`; activation updated the exact active parent/child atomically.
- Hidden recipient/amount change reached `HIDDEN_MATERIAL_CHANGE` and `BLOCKED`.
- Stale, unauthorized, replay and blocked-activation attempts preserved protected state.
- Final readback: 2 proposals, 4 revisions, 2 assessments.

Explorer links and readbacks: [`LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md). Browser-wallet automation is not claimed.
