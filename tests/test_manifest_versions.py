import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ManifestVersionTests(unittest.TestCase):
    def read_manifest(self, path):
        return json.loads((ROOT / path).read_text(encoding="utf-8"))

    def test_release_versions_are_consistent(self):
        release = self.read_manifest("plugin.json")
        version = release["version"]
        self.assertIsInstance(version, str)
        self.assertTrue(version)

        for path in (
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
            ".cursor-plugin/plugin.json",
        ):
            with self.subTest(manifest=path):
                manifest = self.read_manifest(path)
                self.assertEqual(manifest["name"], release["name"])
                self.assertEqual(manifest.get("version"), version)

        marketplace = self.read_manifest(".claude-plugin/marketplace.json")
        entries = [
            plugin
            for plugin in marketplace["plugins"]
            if plugin["name"] == release["name"]
        ]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].get("version"), version)


if __name__ == "__main__":
    unittest.main()
