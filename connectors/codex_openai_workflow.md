# Codex / OpenAI Workflow

1. Clone the repository locally.
2. Open the folder in Codex or another OpenAI-authenticated coding environment.
3. Ask the agent to inspect the repository before editing.
4. Run:

```powershell
python -m pytest
python -m validation.fnp_qnn_payload --out output\fnp_qnn_payloads
```

No OpenAI token is required by the repository itself. Account limits, plan availability, and Codex usage rules are controlled by OpenAI and may change. Refer to:

- https://chatgpt.com/pricing/
- https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
- https://help.openai.com/en/articles/20001106-codex-rate-card

