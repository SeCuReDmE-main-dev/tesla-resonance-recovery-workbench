"""Eight-pass source implantation contract.

This module is the source map for the project build sequence. Every pass is
linked to mandatory source indexes so implementation, validation payloads, and
docs can prove where each concept entered the workbench.
"""

from __future__ import annotations

from dataclasses import dataclass

from core.source_truth import source_urls_by_index


@dataclass(frozen=True)
class SourceImplantationPass:
    pass_number: int
    focus: str
    source_indexes: tuple[int, ...]
    engine_role: str
    positive_boundary: str

    @property
    def source_urls(self) -> list[str]:
        return source_urls_by_index(self.source_indexes)


EIGHT_PASS_SOURCE_IMPLANTATION_PLAN: tuple[SourceImplantationPass, ...] = (
    SourceImplantationPass(
        1,
        "Tesla high-frequency core",
        (2,),
        "Implant high-frequency current language into resonance primitives.",
        "No targeting, no operational transmitter design, and no weapon claims.",
    ),
    SourceImplantationPass(
        2,
        "Tesla energy transmission",
        (3,),
        "Bind transmission-medium reasoning to source-backed modeled claims.",
        "Transmission claims stay mathematical unless independently validated.",
    ),
    SourceImplantationPass(
        3,
        "Tesla apparatus architecture",
        (4,),
        "Represent apparatus topology as abstract system structure.",
        "Architecture is not an antenna-array optimization surface.",
    ),
    SourceImplantationPass(
        4,
        "Tesla natural mediums",
        (5,),
        "Bridge natural-medium propagation into civic positive-use analysis.",
        "Natural-medium claims must not become unsupported HAARP causality.",
    ),
    SourceImplantationPass(
        5,
        "Fractal NeutroGeometry math anchor",
        (15,),
        "Bind wave friction and multi-scale uncertainty to Fractal NeutroGeometry.",
        "Fractal readings are validation hypotheses, not proof by authority.",
    ),
    SourceImplantationPass(
        6,
        "Validation and supporting theory",
        (1, 6, 16, 17, 18),
        "Connect FNP-QNN, Tesla notes, neutrosophic context, and materials bridge.",
        "Supporting theory must remain explicitly labeled and reproducible.",
    ),
    SourceImplantationPass(
        7,
        "HAARP public primary boundary",
        (7, 8, 9, 10, 11),
        "Gate HAARP references through official public primary sources.",
        "Unsupported causal claims are rerouted to positive measurement questions.",
    ),
    SourceImplantationPass(
        8,
        "HAARP datasets and access model",
        (12, 13, 14, 19, 20),
        "Add dataset anchors plus Codex/OpenAI and Google account-access docs.",
        "Access language cites official pages and avoids stale pricing promises.",
    ),
)


CORE_ENGINE_PASS_SOURCE_INDEXES = (2, 3, 4, 5, 15)
HAARP_PASS_SOURCE_INDEXES = (7, 8, 9, 10, 11, 12, 13, 14)


def source_indexes_for_all_passes() -> list[int]:
    indexes: list[int] = []
    for source_pass in EIGHT_PASS_SOURCE_IMPLANTATION_PLAN:
        indexes.extend(source_pass.source_indexes)
    return indexes


def source_urls_for_pass(pass_number: int) -> list[str]:
    for source_pass in EIGHT_PASS_SOURCE_IMPLANTATION_PLAN:
        if source_pass.pass_number == pass_number:
            return source_pass.source_urls
    raise ValueError(f"unknown source implantation pass: {pass_number}")


def validate_eight_pass_source_implantation() -> None:
    if len(EIGHT_PASS_SOURCE_IMPLANTATION_PLAN) != 8:
        raise ValueError("source implantation plan must contain exactly 8 passes")
    pass_numbers = [source_pass.pass_number for source_pass in EIGHT_PASS_SOURCE_IMPLANTATION_PLAN]
    if pass_numbers != list(range(1, 9)):
        raise ValueError("source implantation pass numbers must be contiguous from 1 to 8")
    first_five = EIGHT_PASS_SOURCE_IMPLANTATION_PLAN[:5]
    if any(len(source_pass.source_indexes) != 1 for source_pass in first_five):
        raise ValueError("the first 5 passes must each implant exactly one source")
    if tuple(source_pass.source_indexes[0] for source_pass in first_five) != CORE_ENGINE_PASS_SOURCE_INDEXES:
        raise ValueError("the first 5 passes must implant the selected core-engine sources")
    final_three = EIGHT_PASS_SOURCE_IMPLANTATION_PLAN[5:]
    if any(len(source_pass.source_indexes) != 5 for source_pass in final_three):
        raise ValueError("the final 3 passes must each implant exactly 5 sources")
    if sorted(source_indexes_for_all_passes()) != list(range(1, 21)):
        raise ValueError("the 8-pass plan must cover each mandatory source exactly once")


def implantation_plan_payload() -> list[dict]:
    validate_eight_pass_source_implantation()
    return [
        {
            "pass_number": source_pass.pass_number,
            "focus": source_pass.focus,
            "source_indexes": list(source_pass.source_indexes),
            "source_urls": source_pass.source_urls,
            "engine_role": source_pass.engine_role,
            "positive_boundary": source_pass.positive_boundary,
        }
        for source_pass in EIGHT_PASS_SOURCE_IMPLANTATION_PLAN
    ]
