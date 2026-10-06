# Superseded deployments

## `0x04bc3dA7D0D550444760aa7F55c5688e39e69DC7`

Deployed on Studio Next on 2026-10-06 and retired before submission.

Live probing confirmed correct protocol identity, clean initial state, baseline creation, parent-bound revision creation, and stale-assessment rollback. Two assessment attempts finalized `MAJORITY_DISAGREE`; both preserved `0 assessments` and left revision 2 in `REVISION_PROPOSED`.

Root cause: the comparative validator demanded agreement over the full diagnostic material-category list, even though category differences other than `EXECUTION_ACTION` did not alter the contract consequence. This was stricter than the effect-aligned consensus rule.

Remediation: the validator now compares certification consequence and summary completeness, permits differences in non-consequential diagnostic categories, and explicitly requires `EXECUTION_ACTION` whenever deterministic action diff is non-empty. A new deployment and fresh full E2E run are required. This address must not be submitted as the active deployment.
