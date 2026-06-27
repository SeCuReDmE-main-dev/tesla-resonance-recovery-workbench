"""Source-bound concept registry for the resonance recovery engine."""

from __future__ import annotations

from dataclasses import dataclass

from core.evidence_gate import validate_claim_sources, validate_haarp_claim
from core.source_truth import source_urls_by_index


@dataclass(frozen=True)
class SourceBoundConcept:
    key: str
    pass_number: int
    source_indexes: tuple[int, ...]
    evidence_label: str
    positive_use: str
    public_claim: str

    @property
    def source_urls(self) -> list[str]:
        return source_urls_by_index(self.source_indexes)

    def as_payload(self) -> dict:
        return {
            "key": self.key,
            "pass_number": self.pass_number,
            "source_indexes": list(self.source_indexes),
            "source_urls": self.source_urls,
            "evidence_label": self.evidence_label,
            "positive_use": self.positive_use,
            "public_claim": self.public_claim,
        }


SOURCE_BOUND_CONCEPTS: tuple[SourceBoundConcept, ...] = (
    SourceBoundConcept(
        "high_frequency_resonance_primitives",
        1,
        (2,),
        "modeled",
        "Analyze high-frequency resonance with transparent LC and damping primitives.",
        "The workbench models high-frequency resonance language from Tesla source #2.",
    ),
    SourceBoundConcept(
        "transmission_medium_coupling",
        2,
        (3,),
        "modeled",
        "Study medium coupling as a reproducible mathematical transmission problem.",
        "Transmission-medium concepts are source-bound to Tesla source #3.",
    ),
    SourceBoundConcept(
        "apparatus_topology",
        3,
        (4,),
        "modeled",
        "Represent apparatus relationships as abstract, non-operational topology.",
        "Apparatus structure is modeled from Tesla source #4 without operational optimization.",
    ),
    SourceBoundConcept(
        "natural_medium_boundary",
        4,
        (5,),
        "modeled",
        "Turn natural-medium language into civic positive-use propagation questions.",
        "Natural-medium concepts are source-bound to Tesla source #5.",
    ),
    SourceBoundConcept(
        "fractal_wave_friction",
        5,
        (15,),
        "hypothesis",
        "Use Fractal NeutroGeometry as a bounded interpretation of wave friction.",
        "Fractal wave-friction readings are hypotheses anchored to source #15.",
    ),
    SourceBoundConcept(
        "fnp_qnn_validation_bridge",
        6,
        (1, 6, 16, 17, 18),
        "modeled",
        "Package resonance, neutrosophic context, and materials bridge cases for FNP-QNN.",
        "Validation payloads use FNP-QNN plus supporting theory sources #1, #6, #16, #17, and #18.",
    ),
    SourceBoundConcept(
        "haarp_public_primary_boundary",
        7,
        (7, 8, 9, 10, 11),
        "modeled",
        "Restrict HAARP public claims to official public primary anchors.",
        "HAARP public-primary discussion is limited to sources #7 through #11.",
    ),
    SourceBoundConcept(
        "haarp_dataset_access_boundary",
        8,
        (12, 13, 14, 19, 20),
        "modeled",
        "Combine public datasets with local-first educational access language.",
        "Dataset and access claims are anchored to sources #12, #13, #14, #19, and #20.",
    ),
)


def validate_source_bound_concepts() -> None:
    seen_keys: set[str] = set()
    for concept in SOURCE_BOUND_CONCEPTS:
        if concept.key in seen_keys:
            raise ValueError(f"duplicate source-bound concept: {concept.key}")
        seen_keys.add(concept.key)
        validate_claim_sources(concept.evidence_label, concept.source_urls)
        if "haarp" in concept.key:
            result = validate_haarp_claim(concept.evidence_label, concept.source_urls, concept.public_claim)
            if result["status"] not in {concept.evidence_label, "unsupported"}:
                raise ValueError(f"HAARP concept failed boundary validation: {concept.key}")


def concept_payloads() -> list[dict]:
    validate_source_bound_concepts()
    return [concept.as_payload() for concept in SOURCE_BOUND_CONCEPTS]
