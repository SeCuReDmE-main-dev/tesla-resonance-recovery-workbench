# Tesla Resonance Recovery Workbench

## School Authentication And Secret Boundary
This repository is a small SecuredMe school tool. Official classroom use must not require `.env` files, API keys, raw tokens, or local model secrets. Student and teacher workflows must use Codex/OpenAI or Antigravity/Gemini through browser WebAuth, fingerprinted session approval, and encrypted local session records when authentication is needed.

The reason for excluding generic local AI routes from official school mode is student and teacher safety: education accounts, provider-side account controls, browser login, and governed AI refusal behavior are safer than unguided local model endpoints for classroom cybersecurity and algorithm-building tools.

> **Development status.** This school tool is currently tagged **pre-alpha / in development**. External PRs are not evaluated for merge until the maintained tool reaches a stable, fully functional 100% classroom release after the pre-alpha phase. Issues and forks remain allowed, but official PR review is paused until that stability gate is met.

> **SecuredMe Education visual theme.** This pre-alpha school tool uses the shared SecuredMe Education open-source visual identity. See [assets/securedme/education](assets/securedme/education) for light/dark logo and thin banner assets.


Open-source research workbench for source-grounded Tesla resonance reconstruction, Fractal NeutroGeometry wave-friction analysis, and FNP-QNN validation cases.

> **Official school governance.** This is a classroom/research workbench, not a validated energy, medical, safety, or physical-claim engine. The maintained school route supports Codex/OpenAI or Antigravity/Gemini only. See [SCHOOL_TOOL_GOVERNANCE.md](SCHOOL_TOOL_GOVERNANCE.md) and [AGENTS.md](AGENTS.md).

> **Notice and disclaimer.** The existing project license remains active. See [NOTICE](NOTICE) and [DISCLAIMER](DISCLAIMER) for attribution, school-governance, and misuse-responsibility boundaries.

This project is designed to be used with local Python first, and optionally with Codex/OpenAI or Google Antigravity-style authenticated development accounts. Users bring their own account when they want assisted coding, review, or agentic validation. This repository does not include shared API keys, embedded secrets, or a required hosted backend.

## What this is

Tesla Resonance Recovery Workbench is a positive-use scientific tool for reconstructing resonance problems from primary sources, testing mathematical interpretations, and packaging reproducible cases for FNP-QNN validation.

It focuses on:

- Tesla-source resonance reconstruction;
- wave transmission, loss, coupling, and standing-wave analysis;
- Fractal NeutroGeometry variables: `D_f`, `D_f_hat`, `dF`, `i_fractal`;
- evidence labels: `confirmed`, `modeled`, `hypothesis`, `unsupported`;
- a fixed 20-source mandatory URL ledger for source-of-truth validation;
- civic and educational transparency.

It is not a HAARP replica, weapon model, weather-control tool, biological-effects tool, or retaliation system.

## 8-pass source implantation

The engine is built around a fixed 8-pass source implantation contract:

| Pass | Focus | Mandatory source indexes |
| --- | --- | --- |
| 1 | Tesla high-frequency core | #2 |
| 2 | Tesla energy transmission | #3 |
| 3 | Tesla apparatus architecture | #4 |
| 4 | Tesla natural mediums | #5 |
| 5 | Fractal NeutroGeometry math anchor | #15 |
| 6 | Validation and supporting theory | #1, #6, #16, #17, #18 |
| 7 | HAARP public primary boundary | #7, #8, #9, #10, #11 |
| 8 | HAARP datasets and access model | #12, #13, #14, #19, #20 |

The first 5 passes are the deep core-engine layer. The final 3 passes add validation, public HAARP evidence boundaries, materials bridge, datasets, and access documentation. The implementation lives in `core/source_implantation.py` and is exported in every FNP-QNN validation payload.

## Who this is for

- Students learning scientific source discipline and reproducible modeling.
- Teachers building classroom cases around resonance, evidence, and ethical tooling.
- Researchers exploring fractal/neutrosophic interpretations of wave propagation.
- Civic science users who want transparent models instead of fear-driven claims.

## Use with Codex/OpenAI

The workbench can be opened in a Codex/OpenAI coding environment for assisted implementation, review, testing, and documentation.

Recommended workflow:

1. Clone this repository locally.
2. Sign in to your own Codex/OpenAI environment.
3. Ask the assistant to inspect the repository before editing.
4. Run the local tests and validation cases on your own machine.

The project does not require OpenAI credentials for local validation. OpenAI account usage is optional and controlled by the user. Check current plan details on the official pricing and help pages:

- https://chatgpt.com/pricing/
- https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers

## Use with Google Antigravity

The workbench is also intended to be friendly to Google Antigravity-style authenticated development accounts.

Recommended workflow:

1. Clone this repository.
2. Open it in Antigravity or a compatible local development environment.
3. Use your own Google account and plan if you want agent-assisted work.
4. Keep all generated validation outputs inside local `output/` folders unless you intentionally promote them.

The project does not store Google credentials. Check current official Google AI and Antigravity plan information:

- https://gemini.google/subscriptions/
- https://support.google.com/googleone/answer/14534406

## Education and school accounts

The workbench is designed so students and teachers can run the core validation locally without paid accounts. School-managed Google/OpenAI accounts, education plans, institutional accounts, or affordable individual AI coding plans can help with agent-assisted exploration, but they are optional.

Do not assume all school accounts have the same limits. Always follow your institution's acceptable-use policy and privacy rules.

## Local-first setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pytest
python -m validation.fnp_qnn_payload --out output\fnp_qnn_payloads
```

The repository uses Python standard library modules for the initial scaffold. Future numerical backends must remain optional unless the validation need is clearly documented.

## Validation with FNP-QNN

FNP-QNN-MVP is the validation/proof sandbox for this project:

https://github.com/SeCuReDmE-main-dev/FNP-QNN-MVP

This workbench exports structured cases that can be inspected, challenged, and imported into FNP-QNN validation flows. FNP-QNN is not treated as proof by authority. It is the reproducible simulator surface where claims become testable.

## Ethics and positive-use boundaries

This project is built for transparency, education, scientific repair, and reproducible validation.

Blocked uses:

- transmitter targeting;
- antenna-array optimization for operational systems;
- weather, earthquake, or biological-effect claims without primary reproducible evidence;
- retaliation language;
- weaponization;
- claims that Tesla's consciousness or literal soul has been recreated.

HAARP-related claims must cite public sources #7-14 from `docs/source_ledger.md`. Unsupported causal claims are rerouted to positive-use analysis: Tesla-source resonance mathematics, public measurements, reproducible wave/fractal validation, and non-retaliatory civic science.

The 1910 Tesla Council used in private writing is a source-grounded historical simulation, not a literal resurrection or authority claim.



