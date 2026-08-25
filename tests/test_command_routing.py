import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ORCHESTRATOR_COMMANDS = {
    "df-feature": ("feature-workflow",),
    "df-fix": ("fix-workflow",),
    "df-auto": ("autopilot",),
    "df-build": ("subagent-driven-implementation", "autopilot"),
}

COMMAND_FORMATS = (
    (".claude/commands", ".md"),
    (".github/prompts", ".prompt.md"),
    ("commands", ".toml"),
)


class CommandRoutingTests(unittest.TestCase):
    def test_orchestrator_commands_follow_canonical_files_without_recursive_invocation(self):
        for command, skill_names in ORCHESTRATOR_COMMANDS.items():
            for directory, suffix in COMMAND_FORMATS:
                path = ROOT / directory / f"{command}{suffix}"
                content = path.read_text(encoding="utf-8")

                with self.subTest(command=command, format=directory):
                    for skill_name in skill_names:
                        self.assertIn(
                            f"skills/{skill_name}/SKILL.md",
                            content,
                        )
                    self.assertNotIn("devflow:", content)
                    for hidden_orchestrator in (
                        "feature-workflow",
                        "fix-workflow",
                        "autopilot",
                    ):
                        self.assertNotRegex(
                            content,
                            rf"(?i)\binvoke\s+(?:the\s+)?`?(?:devflow:)?"
                            rf"{hidden_orchestrator}`?\s+skill",
                        )


if __name__ == "__main__":
    unittest.main()
