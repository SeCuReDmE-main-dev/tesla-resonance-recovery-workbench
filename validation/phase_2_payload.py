"""Export Phase 2 scientific-layer payloads for FNP-QNN validation."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from core.fractal_neutrogeometry import wave_friction_reading
from core.haarp_public_adapter import (
    evaluate_haarp_public_claim,
    haarp_adapter_payloads,
    haarp_dataset_metadata,
)
from core.materials_bridge import materials_bridge_payloads
from core.scientific_claims import all_phase_2_claims, exportable_claim_payloads
from core.source_implantation import implantation_plan_payload, validate_eight_pass_source_implantation
from core.source_truth import mandatory_source_urls, validate_mandatory_sources


def build_phase_2_payload() -> dict:
    validate_mandatory_sources()
    validate_eight_pass_source_implantation()
    fractal_reading = wave_friction_reading(
        system="tesla_resonance_recovery_workbench.phase_2_wave_friction",
        scale_min=0.01,
        scale_max=25.0,
        carrier="source_bound_multi_scale_transmission",
        d_f=1.38,
        d_min=1.0,
        d_max=2.0,
        observed_loss_ratio=0.29,
        boundary_instability=0.34,
        measurement_uncertainty=0.18,
        evidence_label="hypothesis",
    )
    return {
        "case_id": "TRRW-FNP-QNN-PHASE-2",
        "title": "Phase 2 source-bound scientific modeling layer",
        "mandatory_source_truth_urls": mandatory_source_urls(),
        "eight_pass_source_implantation": implantation_plan_payload(),
        "scientific_results": exportable_claim_payloads(all_phase_2_claims()),
        "fractal_neutrogeometry": asdict(fractal_reading),
        "materials_bridge": materials_bridge_payloads(),
        "haarp_public_adapters": haarp_adapter_payloads(),
        "haarp_dataset_metadata": haarp_dataset_metadata(),
        "haarp_boundary_status": evaluate_haarp_public_claim("HAARP caused an unsupported causal event", (7,)),
        "hierarchy": "I -> I_system^S -> D_f -> dF -> i_fractal",
        "misuse_boundary": "Unsupported causal claims are not exported as scientific results.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Phase 2 FNP-QNN validation payload")
    parser.add_argument("--out", default="output/fnp_qnn_payloads", help="Output directory")
    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload_path = out_dir / "trrw_fnp_qnn_phase_2.json"
    payload_path.write_text(json.dumps(build_phase_2_payload(), indent=2), encoding="utf-8")
    print(f"Wrote {payload_path.resolve()}")


if __name__ == "__main__":
    main()
