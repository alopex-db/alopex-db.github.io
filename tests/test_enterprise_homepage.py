import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
MKDOCS = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

ENTERPRISE_URL = (
    "https://asopi.tech/en/services/alopex-enterprise"
    "?utm_source=alopex_db_docs&utm_medium=documentation"
    "&utm_campaign=enterprise_package_20260804"
    "&utm_content=docs_enterprise_section_en"
)
SPONSOR_URL = (
    "https://github.com/sponsors/asopitech"
    "?metadata_source=alopex_db_docs"
    "&metadata_campaign=sponsor_early_access"
    "&metadata_content=docs_sponsor_section_en"
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


def section(markdown: str, heading_fragment: str) -> str:
    heading = re.search(
        rf"^## .*{re.escape(heading_fragment)}.*$", markdown, re.MULTILINE
    )
    if heading is None:
        raise AssertionError(f"Section heading is missing: {heading_fragment}")
    end = markdown.find("\n---\n", heading.start())
    return markdown[heading.start():] if end == -1 else markdown[heading.start():end]


class HomepageFunnelTest(unittest.TestCase):
    def test_hero_focuses_on_the_oss_product(self) -> None:
        hero_start = INDEX.index('<div class="hero" markdown>')
        hero_end = INDEX.index("</div>", hero_start)
        hero = INDEX[hero_start:hero_end]

        self.assertIn("[Get Started]", hero)
        self.assertIn("[View on GitHub", hero)
        self.assertNotIn("Enterprise", hero)
        self.assertNotIn("Sponsor", hero)

    def test_enterprise_section_has_one_commercial_route(self) -> None:
        enterprise = section(INDEX, "Alopex Enterprise")
        self.assertIn(ENTERPRISE_COPY, enterprise)
        self.assertIn(
            f"[Discuss an Enterprise use case]({ENTERPRISE_URL})"
            '{ .md-button .md-button--primary '
            'data-analytics-event="docs_enterprise_cta_click" }',
            enterprise,
        )
        self.assertNotIn("github.com/sponsors", enterprise)

    def test_sponsor_section_matches_the_public_tiers(self) -> None:
        sponsor = section(INDEX, "Sponsor Alopex OSS")
        for expected in (
            "$3 / month — OSS Support",
            "$12 / month — Early Access",
            "$99 / month — Enterprise-focused Early Access",
            "experiments, design drafts, internal notes, and prototypes",
            "enterprise-focused enhancements across the asopitech ecosystem",
            "security and deployment",
        ):
            self.assertIn(expected, sponsor)

        self.assertIn(
            f"[Compare sponsor tiers]({SPONSOR_URL})"
            '{ .md-button .md-button--primary '
            'data-analytics-event="docs_sponsor_early_access_click" }',
            sponsor,
        )
        self.assertNotIn("utm_", SPONSOR_URL)

    def test_no_page_promises_more_than_github_sponsors(self) -> None:
        for forbidden in (
            "private Enterprise repositories",
            "full access",
            "Enterprise Access",
        ):
            self.assertNotIn(forbidden.lower(), INDEX.lower())

        self.assertIn(
            "Sponsorship does not include an Alopex Enterprise product license, "
            "SLA, or commercial support.",
            INDEX,
        )

    def test_page_and_navigation_prioritize_oss_before_secondary_routes(self) -> None:
        self.assertLess(
            INDEX.index("## :rocket: Current Status"),
            INDEX.index("## Alopex Enterprise"),
        )
        self.assertLess(
            INDEX.index("## :handshake: Join the Pack"),
            INDEX.index("## :handshake: Sponsor Alopex OSS"),
        )

        nav = MKDOCS.split("\nnav:\n", maxsplit=1)[1]
        getting_started = nav.index("  - Getting Started:")
        enterprise = nav.index(
            "  - Enterprise package (in design): /#alopex-enterprise"
        )
        sponsor = nav.index("  - Sponsor early access: /#sponsor-early-access")
        self.assertLess(getting_started, enterprise)
        self.assertLess(enterprise, sponsor)

        self.assertIn('<a id="alopex-enterprise"></a>', INDEX)
        self.assertIn('<a id="sponsor-early-access"></a>', INDEX)


if __name__ == "__main__":
    unittest.main()
