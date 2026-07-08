"""AlgoQuest/Qbit Education adapter hook for Tesla Workbench."""

from __future__ import annotations

import hashlib

APP_SLUG = "tesla-workbench"
HUB_SLUG = "algoquest"
EVENT_SCHEMA = "securedme.education.student-learning-event.v1"
OUTBOX_KEY = "securedme.education.algoquest.outbox.v1"
_FORBIDDEN_EVENT_KEYS = {
    "api_key",
    "cookie",
    "mandatory_source_truth_urls",
    "materials_bridge",
    "raw_payload",
    "scientific_results",
    "secret",
    "source_urls",
    "student_name",
    "token",
}


def build_learning_event_stub(artifact_ref: str, *, score: float = 93) -> dict:
    return build_learning_event(artifact_ref, score=score)


def build_learning_event(artifact_ref: str, *, score: float = 93, workflow: str = "validation_export") -> dict:
    if not artifact_ref or not artifact_ref.startswith(f"{APP_SLUG}:"):
        raise ValueError("artifact_ref must be a tesla-workbench artifact pointer")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return {
        "schema": EVENT_SCHEMA,
        "app_slug": APP_SLUG,
        "artifact_ref": artifact_ref,
        "skill_area": "resonance_workbench_reasoning",
        "difficulty_band": "beginner",
        "score": score,
        "threshold": 93,
        "attempt_count": 1,
        "blocked_reason": "",
        "next_step_hint": "Open AlgoQuest to translate the workbench result into a safe learning plan.",
        "qbit_help_accepted": False,
        "risk_flags": [],
        "contract_version": "v1",
        "raw_secret_stored": False,
        "dry_run": True,
        "workflow": workflow,
        "outbox_key": OUTBOX_KEY,
    }


def build_payload_learning_event(payload: dict, *, workflow: str = "validation_export", score: float = 93) -> dict:
    case_id = payload.get("case_id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise ValueError("payload must contain a case_id")
    artifact_ref = f"{APP_SLUG}:case:{_stable_case_ref(case_id)}"
    event = build_learning_event(artifact_ref, score=score, workflow=workflow)
    leaked_keys = _FORBIDDEN_EVENT_KEYS & set(event)
    if leaked_keys:
        raise ValueError(f"forbidden event keys: {sorted(leaked_keys)}")
    return event


def _stable_case_ref(case_id: str) -> str:
    normalized = case_id.strip().lower().encode("utf-8")
    return hashlib.sha256(normalized).hexdigest()[:16]
