"""Public HAARP source and dataset adapters with positive-use boundaries."""

from __future__ import annotations

from dataclasses import dataclass

from core.evidence_gate import POSITIVE_HAARP_REDIRECT, validate_haarp_claim
from core.source_truth import source_by_index, source_urls_by_index

UNSUPPORTED_CAUSAL_TERMS = {"caused", "cause", "prove", "proof", "control", "weapon"}


@dataclass(frozen=True)
class HaarpPublicAdapter:
    key: str
    source_indexes: tuple[int, ...]
    adapter_role: str

    @property
    def source_urls(self) -> list[str]:
        return source_urls_by_index(self.source_indexes)

    def as_payload(self) -> dict:
        return {
            "key": self.key,
            "source_indexes": list(self.source_indexes),
            "source_urls": self.source_urls,
            "adapter_role": self.adapter_role,
        }


def haarp_public_adapters() -> tuple[HaarpPublicAdapter, ...]:
    return (
        HaarpPublicAdapter(
            "haarp_public_primary_sources",
            (7, 8, 9, 10, 11),
            "Official public primary boundary for HAARP discussion.",
        ),
        HaarpPublicAdapter(
            "haarp_public_datasets",
            (12, 13),
            "Public dataset metadata for validation examples.",
        ),
        HaarpPublicAdapter(
            "haarp_infrastructure_record",
            (14,),
            "Public infrastructure metadata boundary.",
        ),
    )


def haarp_adapter_payloads() -> list[dict]:
    return [adapter.as_payload() for adapter in haarp_public_adapters()]


def evaluate_haarp_public_claim(claim_text: str, source_indexes: tuple[int, ...]) -> dict[str, str | list[str]]:
    source_urls = source_urls_by_index(source_indexes)
    lowered = claim_text.lower()
    if any(term in lowered for term in UNSUPPORTED_CAUSAL_TERMS):
        return {
            "claim_text": claim_text,
            "status": "unsupported",
            "source_urls": source_urls,
            "message": POSITIVE_HAARP_REDIRECT,
        }
    result = validate_haarp_claim("modeled", source_urls, claim_text)
    if result["status"] != "modeled":
        return {
            "claim_text": claim_text,
            "status": "unsupported",
            "source_urls": source_urls,
            "message": POSITIVE_HAARP_REDIRECT,
        }
    return {
        "claim_text": claim_text,
        "status": "modeled",
        "source_urls": source_urls,
        "message": "HAARP claim is limited to public source metadata.",
    }


def haarp_dataset_metadata() -> list[dict]:
    return [
        {
            "source_index": index,
            "title": source_by_index(index).title,
            "url": source_by_index(index).url,
            "use": "metadata anchor for public measurement validation",
        }
        for index in (12, 13, 14)
    ]
