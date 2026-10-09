# ScopeSentinel — DAO Proposal Amendment Guard

ScopeSentinel is a GenLayer dApp that prevents a DAO proposal revision from becoming canonical when its human change summary hides a material semantic or executable change.

**Live app:** [scope-sentinel-frontend.thanhha68199.workers.dev](https://scope-sentinel-frontend.thanhha68199.workers.dev)

**Live V2 guard:** [`0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885`](https://explorer-studio-dev.genlayer.com/address/0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885)  
**Bound executor:** [`0xF6c1Df76C59244268af9D5608486740DBe50D109`](https://explorer-studio-dev.genlayer.com/address/0xF6c1Df76C59244268af9D5608486740DBe50D109)

The complete V2 two-wallet trail and downstream execution readback are in [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).

The contract seals exact parent/revision text and complete execution manifests on-chain. Deterministic code compares executor, destination, chain, raw calldata digest, recipient, asset, value, amount, nonce, and execution window. Validators judge only whether the prose summary completely discloses semantic changes. Activation atomically consumes the certified revision and emits a finalized, one-time authorization to a guarded executor contract.

## Why GenLayer

Ordinary code can compare addresses and numbers but cannot reliably decide whether rewritten governance prose expands authority, changes purpose, weakens a condition, or hides a beneficiary change. GenLayer consensus establishes that bounded semantic premise; it never receives activation authority.

## Authority boundaries

| Layer | Authority |
|---|---|
| On-chain revision records | Exact parent, text, manifest, revision and actor binding |
| GenLayer validators | Bounded semantic materiality and disclosure-completeness judgment |
| Deterministic contract | Certification safety gate, creator authorization, activation, expiry/chain checks and replay protection |
| Guarded executor | Accepts only finalized messages from ScopeSentinel and records the exact authorized effect |
| Frontend | Non-authoritative client; waits for finality and refreshes exact readbacks |

There is no constructor role, owner, global admin, custody, external web source, or backend authority. Any reviewer can connect their own wallet and create a separate proposal.

## Lifecycle

```text
create_proposal -> ACTIVE baseline with complete manifest
propose_revision -> REVISION_PROPOSED
assess_revision -> CERTIFIED | BLOCKED | CONSENSUS_UNRESOLVED
activate_revision -> old SUPERSEDED + child ACTIVE + EXECUTION_QUEUED
finalized IC message -> guarded executor EXECUTED
```

`CONSENSUS_UNRESOLVED` may be reassessed. `BLOCKED`, `ACTIVE`, and `SUPERSEDED` cannot be semantically retried. Every revision is bound to the exact active parent text and manifest digests.

## Reviewer quick path

1. Deploy `contracts/scope_sentinel.py`; there are no constructor inputs.
2. Deploy `contracts/guarded_executor.py` with the new ScopeSentinel address as its `guard` constructor input.
3. Configure `frontend/.env` with `VITE_CONTRACT_ADDRESS` and build the frontend.
4. Connect any Studio Next wallet and create a proposal baseline whose executor field is the guarded executor address.
5. Select the proposal card; the Workbench opens without manually entering IDs.
6. From another wallet, propose a revision with a complete summary and changed action amount.
7. Run semantic review. The action diff must be disclosed as `EXECUTION_ACTION` before certification.
8. Reconnect the proposal creator and activate the certified revision; verify guard queue and executor allocation readback.
9. Repeat with a “formatting only” summary plus changed beneficiary/scope; observe `BLOCKED` and no execution message.

## Local verification

```powershell
.\verify.ps1
```

Current V2 verification result:

- Contract: `25 passed`
- GenVM linter: both contracts, `3 checks passed` each
- Frontend state tests: `3 passed`
- TypeScript/Vite production build: passed

Live SDK E2E passed on both V2 release contracts: 2 proposals, 4 revisions, 2 assessments, 1 queued authorization, 1 downstream execution and allocation `1200`. Happy, stale, unauthorized, replay, hidden-change and blocked-activation paths finalized. See `docs/LIVE_EVIDENCE.md`; browser-wallet automation is not claimed.

## Repository map

- `contracts/scope_sentinel.py` — deployable Intelligent Contract
- `tests/` — direct lifecycle and adversarial contract tests
- `frontend/` — responsive multi-page React client using `genlayer-js`
- `docs/ARCHITECTURE.md` — proof obligation and state model
- `docs/THREAT_MODEL.md` — attacks, controls and residual risk
- `docs/TEST_RESOURCE_MANIFEST.md` — exact synthetic fixtures and source policy
- `docs/VERIFICATION.md` — requirement-to-evidence matrix
- `docs/LIVE_EVIDENCE.md` — finalized deployment, transaction trail and state readbacks
- `deployment.json` — honest deployment status

## Scope / not claimed

ScopeSentinel proves the relationship between exact on-chain proposal versions, disclosure completeness, and a one-time guarded execution message. The bundled executor demonstrates the enforced Intelligent Contract boundary; it does not claim arbitrary EVM execution, legal validity, voter approval, or that an external DAO adopted the proposal.
