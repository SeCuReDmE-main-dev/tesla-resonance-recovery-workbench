"""Evidence labeling and misuse boundary checks."""

from __future__ import annotations

from core.source_truth import MANDATORY_SOURCE_TRUTH_URLS, mandatory_source_urls

VALID_EVIDENCE_LABELS = {"confirmed", "modeled", "hypothesis", "unsupported"}
HAARP_SOURCE_URLS = {source.url for source in MANDATORY_SOURCE_TRUTH_URLS[6:14]}
BLOCKED_TERMS = {
    "retaliation",
    "target city",
    "earthquake weapon",
    "weather weapon",
    "biological effect",
    "attack plan",
}
POSITIVE_HAARP_REDIRECT = (
    "This claim is not treated as proof. Redirect to positive-use analysis: "
    "Tesla-source resonance math, public HAARP-class measurements, reproducible "
    "wave/fractal validation, and non-retaliatory civic science."
)


def validate_evidence_label(label: str) -> str:
    if label not in VALID_EVIDENCE_LABELS:
        raise ValueError(f"invalid evidence label: {label}")
    return label


def validate_claim_sources(evidence_label: str, source_urls: list[str]) -> str:
    """Require source URLs unless a claim is explicitly weak or rejected."""
    label = validate_evidence_label(evidence_label)
    if label in {"hypothesis", "unsupported"}:
        return label
    if not source_urls:
        raise ValueError("confirmed/modeled claims require at least one source_url")
    allowed_urls = set(mandatory_source_urls())
    unknown_urls = sorted(set(source_urls) - allowed_urls)
    if unknown_urls:
        raise ValueError(f"source_url not in mandatory source ledger: {unknown_urls}")
    return label


def validate_haarp_claim(evidence_label: str, source_urls: list[str], claim_text: str) -> dict[str, str]:
    """Validate HAARP-related claims and return a positive redirect when needed."""
    lowered = claim_text.lower()
    if "haarp" not in lowered:
        return {"status": validate_claim_sources(evidence_label, source_urls), "message": "non_haarp_claim"}

    if any(term in lowered for term in BLOCKED_TERMS):
        return {"status": "blocked_misuse", "message": POSITIVE_HAARP_REDIRECT}

    haarp_sources = set(source_urls) & HAARP_SOURCE_URLS
    if not haarp_sources:
        if evidence_label in {"hypothesis", "unsupported"}:
            return {"status": evidence_label, "message": POSITIVE_HAARP_REDIRECT}
        return {"status": "unsupported", "message": POSITIVE_HAARP_REDIRECT}

    return {"status": validate_claim_sources(evidence_label, source_urls), "message": "haarp_claim_has_public_source_anchor"}


def classify_request_text(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in BLOCKED_TERMS):
        return "blocked_misuse"
    if "haarp" in lowered and ("prove" in lowered or "caused" in lowered):
        return "requires_primary_evidence"
    return "allowed_positive_use"
