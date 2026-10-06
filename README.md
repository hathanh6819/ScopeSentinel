# ScopeSentinel — DAO Proposal Amendment Guard

ScopeSentinel is a GenLayer dApp that prevents a DAO proposal revision from becoming canonical when its human change summary hides a material semantic or executable change.

**Live release:** [`0xA198744fd4A6479019EEea2E27195f8546EDB176`](https://explorer-studio-dev.genlayer.com/address/0xA198744fd4A6479019EEea2E27195f8546EDB176) on GenLayer Studio Next. The complete finalized two-wallet transaction trail and state readbacks are in [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).

The contract seals exact parent/revision text and bounded action manifests on-chain. Deterministic code compares target, selector, recipient, asset, value, amount, and action count. Validators judge only whether the prose summary completely discloses semantic changes. Only the proposal creator can activate a certified child of the currently active revision.

## Why GenLayer

Ordinary code can compare addresses and numbers but cannot reliably decide whether rewritten governance prose expands authority, changes purpose, weakens a condition, or hides a beneficiary change. GenLayer consensus establishes that bounded semantic premise; it never receives activation authority.

## Authority boundaries

| Layer | Authority |
|---|---|
| On-chain revision records | Exact parent, text, manifest, revision and actor binding |
| GenLayer validators | Bounded semantic materiality and disclosure-completeness judgment |
| Deterministic contract | Certification safety gate, creator authorization, activation and replay protection |
| Frontend | Non-authoritative client; waits for finality and refreshes exact readbacks |

There is no constructor role, owner, global admin, custody, external web source, or backend authority. Any reviewer can connect their own wallet and create a separate proposal.

## Lifecycle

```text
create_proposal -> ACTIVE baseline
propose_revision -> REVISION_PROPOSED
assess_revision -> CERTIFIED | BLOCKED | CONSENSUS_UNRESOLVED
activate_revision -> old SUPERSEDED + certified child ACTIVE
```

`CONSENSUS_UNRESOLVED` may be reassessed. `BLOCKED`, `ACTIVE`, and `SUPERSEDED` cannot be semantically retried. Every revision is bound to the exact active parent text and manifest digests.

## Reviewer quick path

1. Deploy `contracts/scope_sentinel.py`; there are no constructor inputs.
2. Configure `frontend/.env` with `VITE_CONTRACT_ADDRESS` and build the frontend.
3. Connect any Studio Next wallet and create a proposal baseline.
4. Select the proposal card; the Workbench opens without manually entering IDs.
5. From another wallet, propose a revision with a complete summary and changed action amount.
6. Run semantic review. The action diff must be disclosed as `EXECUTION_ACTION` before certification.
7. Reconnect the proposal creator and activate the certified revision.
8. Repeat with a “formatting only” summary plus changed beneficiary/scope; observe `BLOCKED` and no activation path.

## Local verification

```powershell
.\verify.ps1
```

Current verified result:

- Contract: `20 passed`
- GenVM linter: `3 checks passed`
- Frontend state tests: `2 passed`
- TypeScript/Vite production build: passed

Live SDK E2E also passed on the release address: 2 proposals, 4 revisions, 2 assessments, with happy, stale, unauthorized, replay, hidden-change and blocked-activation paths finalized. See `docs/LIVE_EVIDENCE.md`; browser-wallet automation is not claimed.

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

ScopeSentinel proves only the relationship between exact on-chain proposal versions and whether a submitted summary discloses their material changes. It does not prove that a proposal is beneficial, lawful, voter-approved, or executed by an external DAO. The activation state is the demonstrated downstream enforcement inside this protocol.
