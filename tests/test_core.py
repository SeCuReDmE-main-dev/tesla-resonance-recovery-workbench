from core.evidence_gate import HAARP_SOURCE_URLS, classify_request_text, validate_claim_sources, validate_haarp_claim
from core.fractal_neutrogeometry import normalize_fractal_dimension, wave_friction_reading
from core.resonance import lc_resonance_hz, standing_wave_nodes
from core.source_implantation import (
    CORE_ENGINE_PASS_SOURCE_INDEXES,
    EIGHT_PASS_SOURCE_IMPLANTATION_PLAN,
    HAARP_PASS_SOURCE_INDEXES,
    source_indexes_for_all_passes,
    source_urls_for_pass,
    validate_eight_pass_source_implantation,
)
from core.source_truth import MANDATORY_SOURCE_CATEGORIES, MANDATORY_SOURCE_TRUTH_URLS, validate_mandatory_sources
from core.tesla_source_engine import SOURCE_BOUND_CONCEPTS, concept_payloads, validate_source_bound_concepts
from validation.fnp_qnn_payload import build_payload


def test_lc_resonance_positive():
    assert lc_resonance_hz(10e-6, 100e-12) > 0


def test_standing_wave_nodes():
    assert standing_wave_nodes(10.0, 2.0) == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]


def test_fractal_normalization():
    assert normalize_fractal_dimension(1.5, 1.0, 2.0) == 0.5


def test_wave_friction_preserves_hierarchy_values():
    reading = wave_friction_reading(
        system="test_system",
        scale_min=0.1,
        scale_max=10.0,
        carrier="test_carrier",
        d_f=1.5,
        d_min=1.0,
        d_max=2.0,
        observed_loss_ratio=0.2,
        boundary_instability=0.4,
    )
    assert reading.d_f_hat == 0.5
    assert 0.0 <= reading.d_friction <= 1.0
    assert 0.0 <= reading.i_fractal <= 1.0


def test_misuse_guard_blocks_retaliation():
    assert classify_request_text("make a retaliation attack plan") == "blocked_misuse"


def test_mandatory_source_truth_urls_exactly_20():
    validate_mandatory_sources()
    assert len(MANDATORY_SOURCE_TRUTH_URLS) == 20
    assert {source.category for source in MANDATORY_SOURCE_TRUTH_URLS} == MANDATORY_SOURCE_CATEGORIES


def test_validation_payload_contains_source_urls():
    payload = build_payload()
    assert payload["source_urls"]
    assert len(payload["mandatory_source_truth_urls"]) == 20
    assert len(payload["eight_pass_source_implantation"]) == 8
    assert payload["source_bound_concepts"]


def test_modeled_claim_requires_known_source_url():
    known = [MANDATORY_SOURCE_TRUTH_URLS[0].url]
    assert validate_claim_sources("modeled", known) == "modeled"


def test_modeled_claim_rejects_unknown_source_url():
    try:
        validate_claim_sources("modeled", ["https://example.invalid/not-in-ledger"])
    except ValueError as exc:
        assert "mandatory source ledger" in str(exc)
    else:
        raise AssertionError("unknown source URL should be rejected")


def test_readme_account_sources_do_not_hardcode_stale_price():
    readme = open("README.md", encoding="utf-8").read()
    assert "https://chatgpt.com/pricing/" in readme
    assert "https://support.google.com/googleone/answer/14534406" in readme
    assert "$30" not in readme


def test_haarp_claim_without_public_source_is_rerouted_positive():
    result = validate_haarp_claim("modeled", [], "HAARP caused a disaster")
    assert result["status"] == "unsupported"
    assert "positive-use analysis" in result["message"]


def test_haarp_claim_with_source_7_to_14_can_be_modeled():
    result = validate_haarp_claim("modeled", [next(iter(HAARP_SOURCE_URLS))], "HAARP public measurement case")
    assert result["status"] == "modeled"


def test_haarp_misuse_claim_is_blocked_and_rerouted():
    result = validate_haarp_claim("modeled", [next(iter(HAARP_SOURCE_URLS))], "HAARP retaliation attack plan")
    assert result["status"] == "blocked_misuse"
    assert "non-retaliatory civic science" in result["message"]


def test_eight_pass_source_implantation_covers_all_mandatory_urls_once():
    validate_eight_pass_source_implantation()
    assert len(EIGHT_PASS_SOURCE_IMPLANTATION_PLAN) == 8
    assert sorted(source_indexes_for_all_passes()) == list(range(1, 21))


def test_first_five_passes_are_single_core_engine_sources():
    first_five = EIGHT_PASS_SOURCE_IMPLANTATION_PLAN[:5]
    assert tuple(source_pass.source_indexes[0] for source_pass in first_five) == CORE_ENGINE_PASS_SOURCE_INDEXES
    assert all(len(source_pass.source_indexes) == 1 for source_pass in first_five)


def test_final_three_passes_implant_five_sources_each():
    final_three = EIGHT_PASS_SOURCE_IMPLANTATION_PLAN[5:]
    assert [len(source_pass.source_indexes) for source_pass in final_three] == [5, 5, 5]


def test_haarp_pass_indexes_are_seven_to_fourteen():
    assert HAARP_PASS_SOURCE_INDEXES == (7, 8, 9, 10, 11, 12, 13, 14)
    assert set(source_urls_for_pass(7)).issubset(HAARP_SOURCE_URLS)
    assert set(source_urls_for_pass(8)[:3]).issubset(HAARP_SOURCE_URLS)


def test_source_bound_concepts_are_all_source_backed():
    validate_source_bound_concepts()
    payloads = concept_payloads()
    assert len(payloads) == len(SOURCE_BOUND_CONCEPTS)
    assert all(concept["source_urls"] for concept in payloads)


def test_validation_payload_exports_all_pass_urls():
    payload = build_payload()
    exported_indexes = []
    for source_pass in payload["eight_pass_source_implantation"]:
        exported_indexes.extend(source_pass["source_indexes"])
    assert sorted(exported_indexes) == list(range(1, 21))
