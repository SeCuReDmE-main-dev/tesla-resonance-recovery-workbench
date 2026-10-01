# Tesla Resonance Recovery Workbench

![Tesla Resonance Recovery Workbench — SecuredMe Education](docs/assets/repository/readme-banner-2026.png)

[![License SEL-2.0](https://img.shields.io/badge/license-SEL--2.0-6F42FF)](LICENSE)
[![Pre-alpha](https://img.shields.io/badge/status-pre--alpha-0E7490)](AGENTS.md)
[![Issues](https://img.shields.io/github/issues/SeCuReDmE-main-dev/tesla-resonance-recovery-workbench)](https://github.com/SeCuReDmE-main-dev/tesla-resonance-recovery-workbench/issues)
[![Main history](https://img.shields.io/github/last-commit/SeCuReDmE-main-dev/tesla-resonance-recovery-workbench/main)](https://github.com/SeCuReDmE-main-dev/tesla-resonance-recovery-workbench/commits/main/)
[![SPONSORED BY E2B FOR STARTUPS](https://img.shields.io/badge/SPONSORED%20BY-E2B%20FOR%20STARTUPS-ff3001?style=for-the-badge&labelColor=black)](https://e2b.dev/startups)

Calculate bounded resonance examples and prepare source-bound scientific validation cases.

[Public surface](https://tesla-recovery.securedme.ca/) · [Tool documentation](https://securedme-main-dev.github.io/securedme-scholarium/en/tools/tesla-workbench/) · [Education hub](https://securedme.ca/product/education/)

**Status:** pre-alpha, active public development. Public pages and a successful local test do not establish a deployed school service. E2B sponsorship recognition is separate from runtime availability and included quota.

## How it works

Transport-neutral Python tools calculate ideal LC resonance, damped response and standing-wave examples. Validation payloads are proposals for review; the workbench does not operate physical equipment.

## Local development

Record the checkout and existing changes before editing:

```powershell
git status --short --branch
git rev-parse HEAD
```

In a clean development checkout, use the committed lockfile or package manifest. The commands below are setup instructions, not a claim that every dependency or optional service has been verified:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
```

Run the relevant local checks from the repository root; the indicated `Set-Location` is needed only when starting from that root:

```powershell
python -m pytest
```

## Source map

- [core/resonance.py](core/resonance.py)
- [core/webmcp.py](core/webmcp.py)
- [validation](validation)
- [tests](tests)
- [docs](docs)

## Practice exercise

Calculate ideal LC resonance for positive component values, compare with the elementary formula, then state the assumptions and units.

During an individual course, learners choose suite tools to practice. The eight-week final project is the learner's own tool, submitted by the learner to an eligible hackathon after checking its age, AI, originality and licensing rules.

## Boundaries and privacy

No energy, medical, weather-control or validated physical-effect claim is established. A simulation and an exported payload are not experimental evidence. Public site availability still needs confirmation.

The official school routes are Codex/OpenAI and Antigravity/Gemini with human review. Never distribute raw tokens, learner data, prompts or private correspondence. No hidden learner analytics are added. Public analytics require explicit consent; general autocapture and session replay remain disabled. Optional local technical telemetry is separate from learner records and product audit history.

See [AGENTS.md](AGENTS.md) and [SCHOOL_TOOL_GOVERNANCE.md](SCHOOL_TOOL_GOVERNANCE.md) for current authority and provider boundaries. Maintainer-authorized maintenance follows repository protections and required reviews. General contribution restrictions remain governed by [CONTRIBUTING.md](CONTRIBUTING.md).

## License, authorship and history

The repository's actual license is [SEL-2.0](LICENSE). Keep the license, attribution, notices and safety boundaries when reusing the code.

Jean-Sebastien Beaulieu · [ORCID 0009-0007-2904-0443](https://orcid.org/0009-0007-2904-0443) · [SecuredMe](https://securedme.ca/)

[README source before curation](docs/archive/README-before-curation-2026-09-30.txt) retains the exact previous text, implementation journals and attribution. It is historical: its old telemetry commands, readiness claims and contribution dates are not current operating instructions. [Presentation history](docs/repository-presentation-history-2026-09-30.md) retains previous badges. [GitHub social image](docs/assets/repository/github-social-preview-2026.jpg) accompanies this README.
