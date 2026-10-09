# Live V2 E2E evidence

## Release identity

- Network: GenLayer Studio Next (`chain_id 61997`)
- ScopeSentinel V2: [`0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885`](https://explorer-studio-dev.genlayer.com/address/0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885)
- GuardedScopeExecutor: [`0xF6c1Df76C59244268af9D5608486740DBe50D109`](https://explorer-studio-dev.genlayer.com/address/0xF6c1Df76C59244268af9D5608486740DBe50D109)
- Production frontend: [scope-sentinel-frontend.thanhha68199.workers.dev](https://scope-sentinel-frontend.thanhha68199.workers.dev)
- Cloudflare version: `e84503f0-2856-46bd-9aa8-261cf7619933`
- Creator wallet A: `0x1D283b45974B0be9630DFD1deC6A62a9B72B2760`
- Independent reviewer wallet B: `0xf96Cf822F9f4e76956AB9fAAa22B3BdCD7b10aD6`
- Executed: 2026-10-09

The deployer has no proposal role. Executor constructor state confirms its guard is the exact ScopeSentinel V2 address. Both contracts began with zero records.

## Finalized transaction trail

| # | Actor | Operation and verified invariant | Explorer |
|---:|---|---|---|
| 1 | Wallet A | Create proposal 1 and complete execution manifest; baseline revision 1 `ACTIVE` | [`0x425f78d2…d293fb`](https://explorer-studio-dev.genlayer.com/transactions/0x425f78d2735b24b7b1d0c9588db88d5272bb6427febccf9943e287bbb8d293fb) |
| 2 | Wallet B | Propose revision 2 against exact parent; deterministic diff is `AMOUNT` | [`0x54eeb4cf…b986a5`](https://explorer-studio-dev.genlayer.com/transactions/0x54eeb4cf25626f0bbd33c8beb0812a9f9e9b9de6c7ef9af355eadac710b986a5) |
| 3 | Wallet B | Stale assessment rejected; candidate state unchanged | [`0x22d9eb49…53cce5`](https://explorer-studio-dev.genlayer.com/transactions/0x22d9eb4986e104648452bbb5935931cbdfb0dd377254612a8fe0c2163653cce5) |
| 4 | Wallet B | Exact assessment returns `FULLY_DISCLOSED`; revision 2 becomes `CERTIFIED` | [`0x81930f08…1a834b`](https://explorer-studio-dev.genlayer.com/transactions/0x81930f0896d2ac36dc270495e8a8d6553b2626dc28ef931ea23b0902121a834b) |
| 5 | Wallet B | Unauthorized activation rejected; proposal pointer unchanged | [`0xe05aae09…7b9a38`](https://explorer-studio-dev.genlayer.com/transactions/0xe05aae0997e1e4a8bb9a9466d88f57fedf69b554071ba3a99cebfc9fd47b9a38) |
| 6 | Wallet A | Activate revision 2; parent superseded, child active, authorization queued | [`0x41bdad3e…a8e154`](https://explorer-studio-dev.genlayer.com/transactions/0x41bdad3eaec780fcb099978ae0b1f04de9895e36ca588b61b9ae66141aa8e154) |
| 7 | Wallet A | Replay activation rejected; active revision and authorization count unchanged | [`0x17a6c57b…f9887b`](https://explorer-studio-dev.genlayer.com/transactions/0x17a6c57b5efed39a2b71272eda58982894662625581cb9c8ffd0ce7e16f9887b) |
| 8 | Wallet A | Create adversarial proposal 2 with independent baseline and nonce | [`0x0da82953…16f610`](https://explorer-studio-dev.genlayer.com/transactions/0x0da829531dac4a2d67a5897dbd3992f9d0ec2af27f496365af526f0ddf16f610) |
| 9 | Wallet B | Propose hidden recipient, amount and nonce changes under “formatting only” label | [`0x2b015175…eb7d68`](https://explorer-studio-dev.genlayer.com/transactions/0x2b015175981e9ba869ddb5b7096bc8344ea0590b996f114a31d8c19c48eb7d68) |
| 10 | Wallet B | Semantic assessment returns `HIDDEN_MATERIAL_CHANGE`; revision 4 `BLOCKED` | [`0xe38131b9…27effc`](https://explorer-studio-dev.genlayer.com/transactions/0xe38131b966b3abbbf56b77342026cef10ecd8c5d53152e1fa21939edc427effc) |
| 11 | Wallet A | Blocked activation rejected; no second authorization or downstream effect | [`0x1fa0a4b6…0ae429`](https://explorer-studio-dev.genlayer.com/transactions/0x1fa0a4b6eec552158e4cb3988b0421ed1b59fd4827ec36e01fddd96b9d0ae429) |

## Downstream enforcement readback

After transaction 6 finalized, ScopeSentinel execution record 1 was `EXECUTION_QUEUED`. The finalized cross-contract message reached the constructor-bound executor, whose execution record 1 is `EXECUTED` with the same proposal ID, revision ID, manifest digest, action and authorization receipt. Its recipient allocation is exactly `1200`.

Final state:

- Guard: `2 proposals / 4 revisions / 2 assessments / 1 execution`.
- Executor: `1 execution / total_authorized 1200`.
- Executor guard: `0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885`.
- Happy revision: `ACTIVE`; parent: `SUPERSEDED`.
- Adversarial revision: `BLOCKED` with deterministic `RECIPIENT`, `AMOUNT`, and `NONCE` diffs.
- Stale, unauthorized, replay, and blocked attempts finalized without protected-state mutation.

Programmatic two-wallet SDK E2E result: **PASS**.

## Reproduce

```powershell
node scripts/inspect_state.mjs 0x944ED2e5D14C81c3D1Cb0B09efd7e091C3013885 0xF6c1Df76C59244268af9D5608486740DBe50D109
```

Private keys are never stored or published. The runner accepts them only through hidden terminal prompts.
