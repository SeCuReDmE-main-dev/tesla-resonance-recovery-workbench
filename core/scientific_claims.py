"""Source-bound scientific claim model for Phase 2."""

from __future__ import annotations

from dataclasses import dataclass

from core.evidence_gate import VALID_EVIDENCE_LABELS, validate_claim_sources, validate_haarp_claim
from core.source_truth import source_urls_by_index


@dataclass(frozen=True)
class ScientificClaim:
    key: str
    claim_text: str
    evidence_label: str
    source_indexes: tuple[int, ...]
    positive_use_note: str
    hypothesis_note: str = ""

    @property
    def source_urls(self) -> list[str]:
        return source_urls_by_index(self.source_indexes)

    def validate(self) -> None:
        if not isinstance(self.key, str) or not self.key.strip():
            raise ValueError("claim key is required and must be a non-empty string")
        if not isinstance(self.claim_text, str) or not self.claim_text.strip():
            raise ValueError("claim_text is required and must be a non-empty string")
        if not isinstance(self.positive_use_note, str) or not self.positive_use_note.strip():
            raise ValueError("positive_use_note is required and must be a non-empty string")
        if self.evidence_label not in VALID_EVIDENCE_LABELS:
            raise ValueError(f"invalid evidence_label: {self.evidence_label}")
        if self.evidence_label == "hypothesis" and (
            not isinstance(self.hypothesis_note, str) or not self.hypothesis_note.strip()
        ):
            raise ValueError("hypothesis claims require a non-empty hypothesis_note string")
        validate_claim_sources(self.evidence_label, self.source_urls)
        haarp_result = validate_haarp_claim(self.evidence_label, self.source_urls, self.claim_text)
        if haarp_result["status"] == "blocked_misuse":
            raise ValueError("blocked misuse claim cannot be registered")
        if "haarp" in self.claim_text.lower() and self.evidence_label in {"confirmed", "modeled"}:
            if haarp_result["status"] not in {self.evidence_label}:
                raise ValueError("HAARP claims require public sources #7-14")

    def as_payload(self) -> dict:
        self.validate()
        return {
            "key": self.key,
            "claim_text": self.claim_text,
            "evidence_label": self.evidence_label,
            "source_indexes": list(self.source_indexes),
            "source_urls": self.source_urls,
            "positive_use_note": self.positive_use_note,
            "hypothesis_note": self.hypothesis_note,
        }


def validate_claim_for_scientific_export(claim: ScientificClaim) -> None:
    claim.validate()
    if claim.evidence_label == "unsupported":
        raise ValueError("unsupported claims cannot be exported as scientific results")


def exportable_claim_payloads(claims: tuple[ScientificClaim, ...] | list[ScientificClaim]) -> list[dict]:
    payloads: list[dict] = []
    for claim in claims:
        validate_claim_for_scientific_export(claim)
        payloads.append(claim.as_payload())
    return payloads


def tesla_scientific_claims() -> tuple[ScientificClaim, ...]:
    return (
        ScientificClaim(
            "tesla_high_frequency_resonance",
            "High-frequency resonance is modeled as a mathematical oscillator and coupling problem.",
            "modeled",
            (2,),
            "Use source #2 to shape transparent resonance primitives.",
        ),
        ScientificClaim(
            "tesla_transmission_medium",
            "Transmission through a medium is modeled as source-bound coupling, loss, and boundary behavior.",
            "modeled",
            (3,),
            "Use source #3 to frame transmission as reproducible mathematics.",
        ),
        ScientificClaim(
            "tesla_apparatus_topology",
            "Apparatus descriptions are represented as non-operational topology.",
            "modeled",
            (4,),
            "Use source #4 for system relationships without optimization instructions.",
        ),
        ScientificClaim(
            "tesla_natural_medium",
            "Natural-medium propagation is treated as a positive-use wave-transmission question.",
            "modeled",
            (5,),
            "Use source #5 to keep natural-medium analysis civic and non-causal.",
        ),
    )


def fractal_scientific_claims() -> tuple[ScientificClaim, ...]:
    return (
        ScientificClaim(
            "fractal_wave_friction_hypothesis",
            "Fractal NeutroGeometry can be used as a bounded hypothesis layer for wave friction.",
            "hypothesis",
            (15,),
            "Use source #15 as the public mathematical anchor.",
            "The current project treats wave friction as a testable interpretation, not a confirmed physical law.",
        ),
    )


def all_phase_2_claims() -> tuple[ScientificClaim, ...]:
    return tesla_scientific_claims() + fractal_scientific_claims()
