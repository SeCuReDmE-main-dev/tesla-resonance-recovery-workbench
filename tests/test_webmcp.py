from core.webmcp import DOMAIN_TOOLS, TOOLS, invoke, manifest


def test_manifest_has_ten_domain_and_two_common_tools() -> None:
    assert manifest()["schema"] == "securedme.webmcp.v1"
    assert len(DOMAIN_TOOLS) == 10
    assert len(TOOLS) == len({tool.name for tool in TOOLS}) == 12
    assert all(tool["inputSchema"]["additionalProperties"] is False for tool in manifest()["tools"])
    assert all(set(tool["inputSchema"]["required"]) <= set(tool["inputSchema"]["properties"]) for tool in manifest()["tools"])


def test_lc_resonance_calls_real_primitive() -> None:
    response = invoke("tesla_calculate_lc_resonance", {"inductanceH": 0.001, "capacitanceF": 0.000001})
    assert response["ok"] is True
    assert response["result"]["frequencyHz"] > 0


def test_wave_reading_preserves_indeterminacy_hierarchy() -> None:
    response = invoke("tesla_build_wave_friction_reading", {"system": "fixture", "scaleMin": 1, "scaleMax": 2, "carrier": "wave", "dF": 1.5, "dMin": 1, "dMax": 2, "observedLossRatio": 0.2, "boundaryInstability": 0.3})
    assert response["result"]["hierarchy"] == "I -> I_system^S -> D_f -> dF -> i_fractal"


def test_validation_payload_is_staged_only() -> None:
    response = invoke("tesla_build_validation_payload", {"caseRef": "fixture:case", "measurements": {"frequency": 1}})
    assert response["result"]["physicalAction"] is False
    assert response["result"]["humanReviewRequired"] is True


def test_unknown_tool_fails_closed() -> None:
    assert invoke("tesla_operate_transmitter")["error"]["code"] == "TOOL_NOT_ALLOWED"
