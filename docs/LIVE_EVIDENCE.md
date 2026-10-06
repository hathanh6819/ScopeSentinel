# Live E2E Evidence

## Release identity

- Network: GenLayer Studio Next (`chain_id 61997`)
- Active contract: [`0xA198744fd4A6479019EEea2E27195f8546EDB176`](https://explorer-studio-dev.genlayer.com/address/0xA198744fd4A6479019EEea2E27195f8546EDB176)
- Production frontend: [scope-sentinel.thanhha68199.workers.dev](https://scope-sentinel.thanhha68199.workers.dev)
- Deployment transaction: [`0x098fa9cc...0028ea`](https://explorer-studio-dev.genlayer.com/transactions/0x098fa9ccdda02602f6ce01d8aa9e5ffc7765255700d18fb5faed8f06fe0028ea)
- Creator/test wallet A: `0x1D283b45974B0be9630DFD1deC6A62a9B72B2760`
- Independent reviewer/test wallet B: `0xf96Cf822F9f4e76956AB9fAAa22B3BdCD7b10aD6`
- Executed: 2026-10-06

The deployer did not receive a protocol role. Both test wallets are ordinary users. A steward can repeat the path with any wallet by creating a separate proposal.

## Finalized transaction trail

| # | Actor | Operation and expected invariant | Explorer |
|---:|---|---|---|
| 1 | Wallet A | Create happy-path proposal baseline; proposal `1`, revision `1` becomes `ACTIVE` | [`0xa3b29f16...494448`](https://explorer-studio-dev.genlayer.com/transactions/0xa3b29f16cbefbb0712856bd535baff0f1ea5e4fcab5c4e2968f26a9871494448) |
| 2 | Wallet B | Propose revision `2` against the exact active parent | [`0x18a5d263...d657a`](https://explorer-studio-dev.genlayer.com/transactions/0x18a5d263e7cf3893a17a5c07da2b980abdfc127311b39fb03d7b0077454d657a) |
| 3 | Wallet B | Stale parent assessment rejected with `STALE_PROPOSAL_REVISION`; no state mutation | [`0xe3ea2a26...c13fd`](https://explorer-studio-dev.genlayer.com/transactions/0xe3ea2a26d434f19ed719639c3562ff6f48eb94d737a4f35784d8df14634c13fd) |
| 4 | Wallet B | Assess exact revision; consensus `MAJORITY_AGREE`, decision `FULLY_DISCLOSED`, revision `CERTIFIED` | [`0x3601d33e...c2d27`](https://explorer-studio-dev.genlayer.com/transactions/0x3601d33e6bdd7767edcc21756ec3d9e26e93325fe165fc8f6a8a9dbfa50c2d27) |
| 5 | Wallet B | Unauthorized activation rejected with `ONLY_PROPOSAL_CREATOR`; no mutation | [`0xbcf5e9fa...2a0d8`](https://explorer-studio-dev.genlayer.com/transactions/0xbcf5e9fad4e3c9daf4a50c1ba79dfa434cd5e9db4c01a85a048b63cd2322a0d8) |
| 6 | Wallet A | Creator activates certified revision atomically; old revision `SUPERSEDED`, child `ACTIVE` | [`0x01fea134...d6b82`](https://explorer-studio-dev.genlayer.com/transactions/0x01fea134d6fb0a56ddc68cd2151cb7fbe10e58655d158c9bffd38c0c1a8d6b82) |
| 7 | Wallet A | Replay activation rejected; active state unchanged | [`0xbd3a7512...453b6`](https://explorer-studio-dev.genlayer.com/transactions/0xbd3a75129914eda6324ec89a4729602b4bbdb3b6d4b40318175d0940554453b6) |
| 8 | Wallet A | Create adversarial proposal `2` with independent baseline | [`0x156f0047...7a41b`](https://explorer-studio-dev.genlayer.com/transactions/0x156f00470d72ad68bbe0308eeed72e78b91576d00f4535c1555c386c8b47a41b) |
| 9 | Wallet B | Propose revision `4` whose summary hides recipient and amount changes | [`0x4ae95e09...e813`](https://explorer-studio-dev.genlayer.com/transactions/0x4ae95e095a2ceda37b330a0023366c925e726b0cfae2e0706d72bef26fdae813) |
| 10 | Wallet B | Adversarial assessment returns `HIDDEN_MATERIAL_CHANGE`; revision becomes `BLOCKED` | [`0xd8e3292d...c788`](https://explorer-studio-dev.genlayer.com/transactions/0xd8e3292d04192a3887fb52ffb4718b78cdaf75648b1d4dce07a6ce60f2bbc788) |
| 11 | Wallet A | Blocked activation rejected with `REVISION_NOT_CERTIFIED`; no mutation | [`0xc26f0922...a157`](https://explorer-studio-dev.genlayer.com/transactions/0xc26f09221b22d02d36e271ca0fbc78840e2c1f33bb2b7a737cab58dea5dba157) |

## Final readback

`get_counts()` returned `2 proposals / 4 revisions / 2 assessments`.

- Proposal 1 points to revision 2; revision 1 is `SUPERSEDED`, revision 2 is `ACTIVE`.
- Assessment 1 is `FULLY_DISCLOSED`, with deterministic action diff present and disclosed, and `summary_complete = true`.
- Revision 4 has deterministic diff fields `RECIPIENT` and `AMOUNT`.
- Assessment 2 is `HIDDEN_MATERIAL_CHANGE`, with `summary_complete = false` and `scope_expanded = true`; revision 4 is `BLOCKED`.
- Stale, unauthorized, replay, and blocked calls finalized with their expected errors and did not mutate the protected state.

Programmatic live E2E result: **PASS**. Browser-wallet behavior is supported by the frontend but is not misrepresented here as automated browser evidence.

## Source parity and reproducibility

The active address was deployed from `contracts/scope_sentinel.py` after the effect-aligned comparator fix. Run `node scripts/inspect_state.mjs 0xA198744fd4A6479019EEea2E27195f8546EDB176` for the finalized readback. The retired pre-fix address is documented in `docs/SUPERSEDED_DEPLOYMENTS.md` and is not the submitted release.
