"""Bounded materials-science bridge for Phase 2 validation."""

from __future__ import annotations

from dataclasses import dataclass

from core.scientific_claims import ScientificClaim, exportable_claim_payloads
from core.source_truth import source_urls_by_index


@dataclass(frozen=True)
class MaterialTransportProfile:
    key: str
    material_context: str
    source_indexes: tuple[int, ...]
    transport_reading: str
    evidence_label: str
    design_boundary: str

    @property
    def source_urls(self) -> list[str]:
        return source_urls_by_index(self.source_indexes)

    def as_payload(self) -> dict:
        claims = (
            ScientificClaim(
                self.key,
                self.transport_reading,
                self.evidence_label,
                self.source_indexes,
                self.design_boundary,
                "Cross-domain material transport links remain bounded until independently validated."
                if self.evidence_label == "hypothesis"
                else "",
            ),
        )
        return {
            "key": self.key,
            "material_context": self.material_context,
            "source_indexes": list(self.source_indexes),
            "source_urls": self.source_urls,
            "transport_reading": self.transport_reading,
            "evidence_label": self.evidence_label,
            "design_boundary": self.design_boundary,
            "validated_claims": exportable_claim_payloads(claims),
        }


def materials_bridge_profiles() -> tuple[MaterialTransportProfile, ...]:
    return (
        MaterialTransportProfile(
            "pseudogap_modulation_profile",
            "pseudogap modulation",
            (17,),
            "Pseudogap modulation is treated as a source-bound reference for comparing wave-friction and state-change language.",
            "modeled",
            "Descriptive material profile only; no device fabrication or operational design instructions.",
        ),
        MaterialTransportProfile(
            "polymer_trap_limited_transport_profile",
            "semiconducting polymer electron transport",
            (18,),
            "Trap-limited electron transport in semiconducting polymers is treated as a source-bound reference for bounded carrier-distribution language.",
            "modeled",
            "Descriptive transport profile only; no transistor optimization or device-tuning instructions.",
        ),
    )


def materials_bridge_payloads() -> list[dict]:
    return [profile.as_payload() for profile in materials_bridge_profiles()]
