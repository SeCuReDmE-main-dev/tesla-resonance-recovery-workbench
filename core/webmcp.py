"""Transport-neutral WebMCP surface for bounded workbench calculations."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Callable, Mapping

from .evidence_gate import classify_request_text
from .fractal_neutrogeometry import wave_friction_reading
from .haarp_public_adapter import evaluate_haarp_public_claim
from .resonance import damped_response_amplitude, lc_resonance_hz, plasma_frequency_hz, standing_wave_nodes
from .scientific_claims import ScientificClaim, validate_claim_for_scientific_export
from .source_implantation import implantation_plan_payload

SCHEMA = "securedme.webmcp.v1"
PRODUCT = "tesla-workbench"


def _property_schema(name: str) -> dict[str, object]:
    if name in {"claim", "measurements", "approval"}:
        return {"type": "object"}
    if name == "sourceIndexes":
        return {"type": "array", "items": {"type": "integer"}, "maxItems": 128}
    if name in {"inductanceH", "capacitanceF", "driveFrequencyHz", "naturalFrequencyHz", "dampingRatio", "lengthM", "wavelengthM", "electronDensityM3", "scaleMin", "scaleMax", "dF", "dMin", "dMax", "observedLossRatio", "boundaryInstability", "measurementUncertainty"}:
        return {"type": "number"}
    return {"type": "string", "minLength": 1, "maxLength": 4096}


@dataclass(frozen=True)
class Tool:
    name: str
    effect: str
    description: str
    required: tuple[str, ...] = ()
    optional: tuple[str, ...] = ()

    def descriptor(self) -> dict[str, object]:
        return {"name": self.name, "mode": self.effect, "effect": self.effect, "description": self.description, "inputSchema": {"type": "object", "properties": {name: _property_schema(name) for name in (*self.required, *self.optional)}, "required": list(self.required), "additionalProperties": False}, "outputSchema": {"type": "object"}, "availability": "available", "handler": {"kind": "python", "module": "core.webmcp"}}


DOMAIN_TOOLS = (
    Tool("tesla_calculate_lc_resonance", "READ", "Calculate ideal LC resonance from positive component values.", ("inductanceH", "capacitanceF")),
    Tool("tesla_calculate_damped_response", "READ", "Calculate normalized damped oscillator response.", ("driveFrequencyHz", "naturalFrequencyHz", "dampingRatio")),
    Tool("tesla_calculate_standing_wave_nodes", "READ", "Calculate ideal one-dimensional standing-wave node positions.", ("lengthM", "wavelengthM")),
    Tool("tesla_calculate_plasma_frequency", "READ", "Calculate electron plasma frequency from a positive density.", ("electronDensityM3",)),
    Tool("tesla_build_wave_friction_reading", "READ", "Build a bounded Fractal NeutroGeometry hypothesis reading.", ("system", "scaleMin", "scaleMax", "carrier", "dF", "dMin", "dMax", "observedLossRatio", "boundaryInstability"), ("measurementUncertainty", "evidenceLabel")),
    Tool("tesla_classify_request_safety", "READ", "Classify a request against positive-use workbench boundaries.", ("text",)),
    Tool("tesla_validate_scientific_claim", "READ", "Validate an explicitly source-bound scientific claim.", ("claim",)),
    Tool("tesla_evaluate_haarp_public_claim", "READ", "Evaluate a HAARP statement only against public-source boundaries.", ("claimText", "sourceIndexes")),
    Tool("tesla_inspect_source_ledger", "READ", "Inspect the maintained source-implantation ledger."),
    Tool("tesla_build_validation_payload", "STAGE", "Stage a validation payload without operating physical equipment.", ("caseRef", "measurements")),
)
COMMON_TOOLS = (
    Tool("securedme_companion_context", "READ", "Return a sanitized neutral workbench projection."),
    Tool("securedme_qbit_plan_handoff", "STAGE", "Prepare a Qbit return proposal without changing progression.", ("missionRef", "summary")),
)
TOOLS = DOMAIN_TOOLS + COMMON_TOOLS


def manifest() -> dict[str, object]:
    return {"schema": SCHEMA, "product": {"slug": PRODUCT, "canonicalStateOwner": "algoquest"}, "slug": PRODUCT, "canonicalStateOwner": "algoquest", "tools": [tool.descriptor() for tool in TOOLS], "boundaries": {"authority": "Scientific claims require human review.", "secrets": "No credentials are returned.", "externalWrites": "No physical or external operation is performed.", "heroProgression": "AlgoQuest alone owns Hero Book progression.", "physicalControl": False, "weaponization": False, "causalWeatherClaims": False, "scientificAuthority": "human"}, "theme": {"source": "assets/landing/secureme.ca-product/education/desing/stitch_securedme_education_hub_design_system/stitch_securedme_education_hub_design_system/design.md", "sourceStatus": "fallback_missing_product_stitch"}}


def _claim(payload: Mapping[str, Any]) -> dict[str, object]:
    raw = payload.get("claim")
    if not isinstance(raw, Mapping):
        raise ValueError("claim must be an object")
    claim = ScientificClaim(
        key=str(raw.get("key", "")),
        claim_text=str(raw.get("claimText", "")),
        evidence_label=str(raw.get("evidenceLabel", "")),
        source_indexes=tuple(int(item) for item in raw.get("sourceIndexes", [])),
        positive_use_note=str(raw.get("positiveUseNote", "")),
        hypothesis_note=str(raw.get("hypothesisNote", "")),
    )
    validate_claim_for_scientific_export(claim)
    return {"valid": True, "claim": claim.as_payload(), "humanReviewRequired": True}


def _wave(payload: Mapping[str, Any]) -> dict[str, object]:
    value = wave_friction_reading(
        system=str(payload["system"]), scale_min=float(payload["scaleMin"]), scale_max=float(payload["scaleMax"]),
        carrier=str(payload["carrier"]), d_f=float(payload["dF"]), d_min=float(payload["dMin"]), d_max=float(payload["dMax"]),
        observed_loss_ratio=float(payload["observedLossRatio"]), boundary_instability=float(payload["boundaryInstability"]),
        measurement_uncertainty=float(payload.get("measurementUncertainty", 0.0)), evidence_label=str(payload.get("evidenceLabel", "modeled")),
    )
    result = asdict(value)
    result["hierarchy"] = "I -> I_system^S -> D_f -> dF -> i_fractal"
    return result


def _stage(payload: Mapping[str, Any]) -> dict[str, object]:
    measurements = payload.get("measurements")
    if not payload.get("caseRef") or not isinstance(measurements, Mapping):
        raise ValueError("caseRef and measurements are required")
    return {"status": "staged", "caseRef": payload["caseRef"], "measurements": dict(measurements), "physicalAction": False, "humanReviewRequired": True}


def _handoff(payload: Mapping[str, Any]) -> dict[str, object]:
    if not payload.get("missionRef") or not payload.get("summary"):
        raise ValueError("missionRef and summary are required")
    return {"status": "staged", "missionRef": payload["missionRef"], "summary": payload["summary"], "progressChanged": False, "nextAction": "return_to_qbit_for_human_review"}


HANDLERS: dict[str, Callable[[Mapping[str, Any]], object]] = {
    "tesla_calculate_lc_resonance": lambda p: {"frequencyHz": lc_resonance_hz(float(p["inductanceH"]), float(p["capacitanceF"]))},
    "tesla_calculate_damped_response": lambda p: {"relativeAmplitude": damped_response_amplitude(float(p["driveFrequencyHz"]), float(p["naturalFrequencyHz"]), float(p["dampingRatio"]))},
    "tesla_calculate_standing_wave_nodes": lambda p: {"nodesM": standing_wave_nodes(float(p["lengthM"]), float(p["wavelengthM"]))},
    "tesla_calculate_plasma_frequency": lambda p: {"frequencyHz": plasma_frequency_hz(float(p["electronDensityM3"]))},
    "tesla_build_wave_friction_reading": _wave,
    "tesla_classify_request_safety": lambda p: {"classification": classify_request_text(str(p["text"]))},
    "tesla_validate_scientific_claim": _claim,
    "tesla_evaluate_haarp_public_claim": lambda p: evaluate_haarp_public_claim(str(p["claimText"]), tuple(int(item) for item in p["sourceIndexes"])),
    "tesla_inspect_source_ledger": lambda p: {"passes": implantation_plan_payload(), "readOnly": True},
    "tesla_build_validation_payload": _stage,
    "securedme_companion_context": lambda p: {"schema": "HeroBookPanelState.projection.v1", "product": PRODUCT, "specialist": "Tesla Workbench", "persona": "neutral scientific workbench", "canonicalStateOwner": "algoquest", "sanitized": True},
    "securedme_qbit_plan_handoff": _handoff,
}


def invoke(name: str, payload: Mapping[str, Any] | None = None) -> dict[str, object]:
    if name not in HANDLERS:
        return {"ok": False, "error": {"code": "TOOL_NOT_ALLOWED", "message": "Unknown Tesla Workbench tool."}}
    try:
        value = HANDLERS[name](payload or {})
    except (KeyError, TypeError, ValueError) as exc:
        return {"ok": False, "error": {"code": "INVALID_INPUT", "message": str(exc)}}
    return {"ok": True, "tool": name, "result": value, "trace": {"product": PRODUCT, "sanitized": True}}
