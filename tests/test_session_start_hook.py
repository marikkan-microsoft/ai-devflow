import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SessionStartHookTests(unittest.TestCase):
    def test_router_is_printed_as_plain_text(self):
        # Claude Code only adds plain stdout (or hookSpecificOutput.additionalContext)
        # to the session context; any other JSON shape is silently dropped.
        result = subprocess.run(
            ["bash", str(ROOT / "hooks" / "session-start.sh")],
            capture_output=True,
            text=True,
            check=True,
        )
        router = (ROOT / "skills" / "using-devflow" / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(result.stdout.startswith("devflow loaded."))
        self.assertIn(router, result.stdout)


if __name__ == "__main__":
    unittest.main()
