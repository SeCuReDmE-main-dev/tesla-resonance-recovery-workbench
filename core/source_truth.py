"""Mandatory source-of-truth URL ledger."""

from __future__ import annotations

from dataclasses import dataclass


MANDATORY_SOURCE_CATEGORIES = {
    "tesla_primary",
    "haarp_public_primary",
    "haarp_public_dataset",
    "fractal_neutrogeometry_context",
    "fnp_qnn_validation",
    "materials_bridge",
    "access_account_docs",
}


@dataclass(frozen=True)
class MandatorySource:
    index: int
    title: str
    url: str
    category: str


MANDATORY_SOURCE_TRUTH_URLS: tuple[MandatorySource, ...] = (
    MandatorySource(1, "FNP-QNN-MVP validation repo", "https://github.com/SeCuReDmE-main-dev/FNP-QNN-MVP", "fnp_qnn_validation"),
    MandatorySource(2, "Tesla patent US568180A, high-frequency currents", "https://patents.google.com/patent/US568180A/en", "tesla_primary"),
    MandatorySource(3, "Tesla patent US645576A, transmission of electrical energy", "https://patents.google.com/patent/US645576A/en", "tesla_primary"),
    MandatorySource(4, "Tesla patent US649621A, apparatus for transmission", "https://patents.google.com/patent/US649621A/en", "tesla_primary"),
    MandatorySource(5, "Tesla patent US787412A, natural mediums", "https://patents.google.com/patent/US787412A/en", "tesla_primary"),
    MandatorySource(6, "Tesla Colorado Springs Notes", "https://archive.org/details/nikolateslacolor0000niko", "tesla_primary"),
    MandatorySource(7, "HAARP official site/about", "https://haarp.gi.alaska.edu/", "haarp_public_primary"),
    MandatorySource(8, "HAARP official FAQ", "https://haarp.gi.alaska.edu/faq", "haarp_public_primary"),
    MandatorySource(9, "HAARP diagnostic suite", "https://haarp.gi.alaska.edu/diagnostic-suite", "haarp_public_primary"),
    MandatorySource(10, "HAARP publications list", "https://haarp.gi.alaska.edu/publications", "haarp_public_primary"),
    MandatorySource(11, "UAF HAARP airglow article", "https://www.uaf.edu/news/haarp-to-produce-artificial-airglow-that-may-be-widely-visible-in-alaska.php", "haarp_public_primary"),
    MandatorySource(12, "Zenodo HAARP UH/IA waves dataset", "https://zenodo.org/records/18972204", "haarp_public_dataset"),
    MandatorySource(13, "Zenodo HAARP plasma ion-line data", "https://zenodo.org/records/12575819", "haarp_public_dataset"),
    MandatorySource(14, "UArctic HAARP infrastructure record", "https://www.uarctic.org/resources/infrastructure/details/29101", "haarp_public_primary"),
    MandatorySource(15, "NeutroGeometry and Fractal Geometry PDF", "https://fs.unm.edu/NSS/01NeutroGeometryFractal.pdf", "fractal_neutrogeometry_context"),
    MandatorySource(16, "NSIA Publishing House", "https://neutrosophic.org/nsia-publishing-house/", "fractal_neutrogeometry_context"),
    MandatorySource(17, "Pseudogap modulation paper, OSTI", "https://www.osti.gov/pages/biblio/2000768", "materials_bridge"),
    MandatorySource(18, "Trap-limited electron transport in semiconducting polymers", "https://research.rug.nl/en/publications/unification-of-trap-limited-electron-transport-in-semiconducting-/", "materials_bridge"),
    MandatorySource(19, "ChatGPT pricing/account source", "https://chatgpt.com/pricing/", "access_account_docs"),
    MandatorySource(20, "Google AI Pro / Antigravity benefits source", "https://support.google.com/googleone/answer/14534406", "access_account_docs"),
)


def mandatory_source_urls() -> list[str]:
    return [source.url for source in MANDATORY_SOURCE_TRUTH_URLS]


def validate_mandatory_sources() -> None:
    if len(MANDATORY_SOURCE_TRUTH_URLS) != 20:
        raise ValueError("mandatory source ledger must contain exactly 20 URLs")
    indexes = [source.index for source in MANDATORY_SOURCE_TRUTH_URLS]
    if indexes != list(range(1, 21)):
        raise ValueError("mandatory source indexes must be contiguous from 1 to 20")
    urls = mandatory_source_urls()
    if len(set(urls)) != len(urls):
        raise ValueError("mandatory source URLs must be unique")
    categories = {source.category for source in MANDATORY_SOURCE_TRUTH_URLS}
    missing = MANDATORY_SOURCE_CATEGORIES - categories
    if missing:
        raise ValueError(f"missing mandatory source categories: {sorted(missing)}")
