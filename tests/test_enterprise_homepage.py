import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

HERO_URL = (
    "https://asopi.tech/en/services/alopex-enterprise"
    "?utm_source=alopex_db_docs&utm_medium=documentation"
    "&utm_campaign=enterprise_package_20260804&utm_content=docs_home_en"
)
ENTERPRISE_URL = (
    "https://asopi.tech/en/services/alopex-enterprise"
    "?utm_source=alopex_db_docs&utm_medium=documentation"
    "&utm_campaign=enterprise_package_20260804"
    "&utm_content=docs_enterprise_section_en"
)
SPONSOR_URL = (
    "https://github.com/sponsors/asopitech"
    "?metadata_source=alopex_db_docs"
    "&metadata_campaign=enterprise_early_access"
    "&metadata_content=docs_enterprise_section_en"
)

ENTERPRISE_COPY = """## Alopex Enterprise — Commercial Feature Package

Alopex Enterprise is a commercial feature package built on the Alopex DB OSS foundation.

It is not a support tier or a support add-on. It adds enterprise capabilities in four areas:

- **Security Suite** — data protection, identity, policy, classification, revocation, and re-encryption
- **Unified Query Model & Enterprise Search** — SQL, AQL, PromQL, full-text, structured, vector, and aggregation workloads
- **Observe** — SLOs, error budgets, burn rates, operational decisions, and automation
- **Unified Infrastructure** — configuration, service discovery, internal DNS, and higher-level platform services

The package is currently in architecture design and technical validation. It is not generally available.
"""


def section(markdown: str, heading_prefix: str) -> str:
    start = markdown.index(heading_prefix)
    end = markdown.find("\n---\n", start)
    return markdown[start:] if end == -1 else markdown[start:end]


def enterprise_section(markdown: str) -> str:
    heading = re.search(r"^## .*Alopex Enterprise.*$", markdown, re.MULTILINE)
    if heading is None:
        raise AssertionError("Alopex Enterprise section heading is missing")
    end = markdown.find("\n---\n", heading.start())
    return markdown[heading.start():] if end == -1 else markdown[heading.start():end]


class EnterpriseHomepageTest(unittest.TestCase):
    def test_enterprise_section_uses_approved_package_copy(self) -> None:
        enterprise = enterprise_section(INDEX)
        self.assertIn(ENTERPRISE_COPY, enterprise)
        self.assertNotIn("commercial middleware", enterprise.lower())

    def test_hero_has_measured_enterprise_cta(self) -> None:
        hero = section(INDEX, '<div class="hero" markdown>')
        self.assertIn(
            f"[Explore Alopex Enterprise]({HERO_URL})"
            '{ .md-button data-analytics-event="docs_enterprise_cta_click" }',
            hero,
        )

    def test_enterprise_section_has_both_measured_ctas(self) -> None:
        enterprise = enterprise_section(INDEX)
        self.assertIn(
            f"[Discuss an Enterprise use case]({ENTERPRISE_URL})"
            '{ .md-button .md-button--primary '
            'data-analytics-event="docs_enterprise_cta_click" }',
            enterprise,
        )
        self.assertIn(
            f"[Sponsor early access]({SPONSOR_URL})"
            '{ .md-button '
            'data-analytics-event="docs_sponsor_early_access_click" }',
            enterprise,
        )

        sponsor_target = re.search(
            r"\[Sponsor early access\]\(([^)]+)\)", enterprise
        )
        self.assertIsNotNone(sponsor_target)
        self.assertNotIn("utm_", sponsor_target.group(1))

    def test_navigation_uses_in_design_label_and_homepage_anchor(self) -> None:
        nav = MKDOCS.split("\nnav:\n", maxsplit=1)[1]
        self.assertRegex(
            nav,
            r"(?m)^  - Enterprise package \(in design\): /#alopex-enterprise$",
        )

        anchor_position = INDEX.index('<a id="alopex-enterprise"></a>')
        heading_position = INDEX.index("## Alopex Enterprise")
        self.assertLess(anchor_position, heading_position)


if __name__ == "__main__":
    unittest.main()
