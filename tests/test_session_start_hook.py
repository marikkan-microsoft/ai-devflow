import shutil
import subprocess
import tempfile
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

    def test_copied_install_path_can_contain_spaces(self):
        with tempfile.TemporaryDirectory(prefix="devflow hook ") as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "hooks", root / "hooks")
            router = root / "skills" / "using-devflow" / "SKILL.md"
            router.parent.mkdir(parents=True)
            shutil.copyfile(ROOT / "skills" / "using-devflow" / "SKILL.md", router)

            result = subprocess.run(
                ["bash", str(root / "hooks" / "session-start.sh")],
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertTrue(result.stdout.startswith("devflow loaded."))
            self.assertIn(router.read_text(encoding="utf-8"), result.stdout)
            self.assertEqual(result.stderr, "")

    def test_missing_router_reports_the_fallback_without_claiming_loading(self):
        with tempfile.TemporaryDirectory(prefix="devflow hook ") as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "hooks", root / "hooks")

            result = subprocess.run(
                ["bash", str(root / "hooks" / "session-start.sh")],
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("using-devflow router not found", result.stdout)
            self.assertIn("Skills may still be available", result.stdout)
            self.assertNotIn("devflow loaded.", result.stdout)
            self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
