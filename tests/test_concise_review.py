"""Offline skill contracts, not a simulation of an agent performing a review."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ConciseReviewTests(unittest.TestCase):
    def read(self, relative_path):
        path = ROOT / relative_path
        self.assertTrue(path.is_file(), f"Missing artifact: {relative_path}")
        return path.read_text(encoding="utf-8")

    def test_skill_is_model_invoked_and_follows_devflow_anatomy(self):
        text = self.read("skills/concise-review/SKILL.md")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertIn("\nname: concise-review\n", frontmatter)
        self.assertRegex(frontmatter, r"\ndescription: .+ Use when .+\n")
        self.assertNotIn("disable-model-invocation", frontmatter)
        self.assertEqual(
            re.findall(r"^## (.+)$", text, re.MULTILINE),
            [
                "Overview",
                "When to Use",
                "Process",
                "Common Rationalizations",
                "Red Flags",
                "Verification",
            ],
        )
        self.assertIn("**When NOT to use:**", text)
        self.assertIn("**Related:**", text)
        self.assertLessEqual(len(text.splitlines()), 200)

    def test_reporting_mode_reuses_the_existing_review_contract(self):
        text = self.read("skills/concise-review/SKILL.md")
        for target in (
            "../review-code/SKILL.md",
            "../../references/code-review-rubric.md",
        ):
            self.assertIn(f"]({target})", text)
        for label in (
            "Critical",
            "Important",
            "Suggestion",
            "APPROVE",
            "REQUEST CHANGES",
            "INCOMPLETE",
        ):
            self.assertIn(label, text)
        self.assertIn("read-only", text)
        self.assertIn(
            "../concise-review/SKILL.md",
            self.read("skills/review-code/SKILL.md"),
        )
        for path in ("references/code-review-rubric.md", "agents/code-reviewer.md"):
            with self.subTest(consumer=path):
                self.assertIn("../skills/concise-review/SKILL.md", self.read(path))

    def test_command_routes_and_catalogs_expose_the_skill(self):
        for directory, suffix in (
            (".claude/commands", ".md"),
            (".github/prompts", ".prompt.md"),
            ("commands", ".toml"),
        ):
            with self.subTest(format=directory):
                text = self.read(f"{directory}/df-concise-review{suffix}")
                self.assertIn("skills/concise-review/SKILL.md", text)

        for path in (
            "skills/README.md",
            "docs/usage.md",
            "AGENTS.md",
            "CLAUDE.md",
            "docs/architecture.md",
        ):
            with self.subTest(catalog=path):
                self.assertIn("concise-review", self.read(path))


if __name__ == "__main__":
    unittest.main()
