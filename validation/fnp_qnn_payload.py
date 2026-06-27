"""Export FNP-QNN validation payloads for resonance/fractal cases."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from core.evidence_gate import validate_claim_sources
from core.fractal_neutrogeometry import wave_friction_reading
from core.resonance import lc_resonance_hz, plasma_frequency_hz, standing_wave_nodes
from core.source_implantation import implantation_plan_payload, validate_eight_pass_source_implantation
from core.source_truth import MANDATORY_SOURCE_TRUTH_URLS, mandatory_source_urls, validate_mandatory_sources
from core.tesla_source_engine import concept_payloads, validate_source_bound_concepts


def build_payload() -> dict:
    validate_mandatory_sources()
    validate_eight_pass_source_implantation()
    validate_source_bound_concepts()
    source_urls = [
        MANDATORY_SOURCE_TRUTH_URLS[1].url,
        MANDATORY_SOURCE_TRUTH_URLS[2].url,
        MANDATORY_SOURCE_TRUTH_URLS[14].url,
        MANDATORY_SOURCE_TRUTH_URLS[0].url,
    ]
    validate_claim_sources("modeled", source_urls)
    reading = wave_friction_reading(
        system="tesla_resonance_recovery_workbench.wave_transmission_case_001",
        scale_min=0.01,
        scale_max=10.0,
        carrier="multi_scale_boundary_loss",
        d_f=1.42,
        d_min=1.0,
        d_max=2.0,
        observed_loss_ratio=0.31,
        boundary_instability=0.44,
        evidence_label="modeled",
    )
    return {
        "case_id": "TRRW-FNP-QNN-001",
        "title": "Tesla-source resonance with Fractal NeutroGeometry wave-friction reading",
        "source_categories": ["tesla_primary", "fractal_neutrogeometry_context", "fnp_qnn_validation"],
        "source_urls": source_urls,
        "mandatory_source_truth_urls": mandatory_source_urls(),
        "eight_pass_source_implantation": implantation_plan_payload(),
        "source_bound_concepts": concept_payloads(),
        "resonance": {
            "lc_frequency_hz": lc_resonance_hz(10e-6, 100e-12),
            "standing_wave_nodes_m": standing_wave_nodes(10.0, 2.0),
            "plasma_frequency_hz_at_1e12_m3": plasma_frequency_hz(1e12),
        },
        "fractal_neutrogeometry": asdict(reading),
        "hierarchy": "I -> I_system^S -> D_f -> dF -> i_fractal",
        "evidence_label": "modeled",
        "misuse_boundary": "No targeting, weapon, weather, earthquake, or biological-effect claims.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Export FNP-QNN validation payload")
    parser.add_argument("--out", default="output/fnp_qnn_payloads", help="Output directory")
    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload_path = out_dir / "trrw_fnp_qnn_case_001.json"
    payload_path.write_text(json.dumps(build_payload(), indent=2), encoding="utf-8")
    print(f"Wrote {payload_path.resolve()}")


if __name__ == "__main__":
    main()
