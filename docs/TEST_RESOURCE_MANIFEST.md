# Test resource manifest

## Source policy

No external URL is used. The proof obligation concerns the relation between immutable on-chain parent/revision records. Using a self-authored text is acceptable for this narrow relation because it cannot establish an external fact or unlock a claim about real-world truth.

All fixtures are synthetic and must be labeled synthetic in submission evidence.

## Actors

- Deployer: deploy only; never used as the operational happy/conflict actor.
- Wallet A: proposal creator and activation authority for its own proposal.
- Wallet B: independent revision proposer and assessment requester.
- Reviewer wallet: may create and test its own isolated proposal without allowlisting.

## Baseline fixture

Purpose: wallet security audit. Amount: `1000`. Target `0xaaaa…aaaa`, selector `0x12345678`, recipient `0xbbbb…bbbb`, asset `NATIVE`.

## Fully disclosed fixture

Text and manifest raise amount to `1200` for an added mobile-wallet review. Summary explicitly discloses amount and scope. Expected: `CERTIFIED`, then creator activation succeeds.

## Poisoned summary fixture

Summary says formatting only while text expands spending authority and changes beneficiary/purpose. Expected: `BLOCKED`; activation leaves complete state unchanged.

## Required permutations

- correct/wrong parent digest;
- current/stale proposal revision;
- text-only/action-changing revision;
- complete/incomplete summary;
- normal/prompt-injected text;
- valid/malformed/disagreed consensus;
- creator/reviewer/outsider activation;
- first activation/replay;
- correct/cross-proposal revision.
