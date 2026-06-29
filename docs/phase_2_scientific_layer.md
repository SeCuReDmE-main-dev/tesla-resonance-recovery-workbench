# Phase 2 Scientific Layer

Phase 2 converts the 8-pass source implantation contract into executable scientific modeling surfaces.

## Scientific Claim Enforcement

Every exported scientific claim uses:

- claim text;
- evidence label;
- mandatory source indexes;
- mandatory source URLs;
- positive-use note;
- hypothesis note when the label is `hypothesis`.

Rules:

- `confirmed` and `modeled` claims require source URLs from the mandatory ledger.
- `hypothesis` claims require an explicit note.
- `unsupported` claims cannot be exported as scientific results.

## Tesla Resonance Concepts

The Tesla layer exports descriptive, mathematical concepts for:

- high-frequency resonance from source #2;
- transmission-medium coupling from source #3;
- apparatus topology from source #4;
- natural-medium propagation from source #5.

These are not transmitter design, targeting, antenna-array optimization, weather claims, earthquake claims, or biological-effect claims.

## Fractal NeutroGeometry Wave Friction

The wave-friction reading now includes:

- normalized `D_f_hat`;
- normalized `dF`;
- transmission-friction score;
- uncertainty terms;
- preserved hierarchy `I -> I_system^S -> D_f -> dF -> i_fractal`.

Source #15 is the public anchor. The local Fractal NeutroGeometry book remains internal deeper context and is not promoted into public RAG by default.

## Materials Bridge

The materials bridge adds descriptive profiles only:

- pseudogap modulation from source #17;
- semiconducting-polymer electron transport from source #18.

The profiles do not provide device fabrication, transistor tuning, or operational optimization instructions.

## HAARP Public Boundary

HAARP adapters are limited to:

- public primary sources #7-#11;
- public datasets #12-#13;
- infrastructure record #14.

Causal claims remain `unsupported` and rerouted to positive-use Tesla math, public measurements, reproducible wave/fractal validation, and non-retaliatory civic science.

## Validation

Run:

```powershell
python -m pytest
python -m validation.fnp_qnn_payload --out output\fnp_qnn_payloads
python -m validation.phase_2_payload --out output\fnp_qnn_payloads
```

Expected Phase 2 payload:

`output\fnp_qnn_payloads\trrw_fnp_qnn_phase_2.json`
