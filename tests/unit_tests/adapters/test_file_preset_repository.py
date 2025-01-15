from pathlib import Path
import unittest
from unittest.mock import MagicMock, mock_open, patch

from vfxMikChainBridge.domain.entities.preset import Preset
from vfxMikChainBridge.adapters.file_preset_repository import FilePresetRepository


class TestPrestRepository(unittest.TestCase):
    
    def setUp(self):
        self.mock_base_dir = MagicMock(spec=Path)
        self.repo = FilePresetRepository(base_dir=self.mock_base_dir)
           
           
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save(self, mock_json_dump, mock_open):
        preset = Preset(name="test_preset", template_paths=["/path/to/template1", "/path/to/template2"])
        mock_file_path = self.mock_base_dir / "test_preset.json"

        self.repo.save(preset)

        mock_open.assert_called_once_with(mock_file_path, "w")
        mock_json_dump.assert_called_once_with(
            {"name": preset.name, "paths": preset.template_paths}, mock_open.return_value
        )

    @patch("builtins.open", new_callable=mock_open, read_data='{"name": "test_preset", "template_paths": ["/path1", "/path2"]}')
    @patch("pathlib.Path.exists")
    def test_load(self, mock_exists, mock_open):
        mock_exists.return_value = True
        preset = self.repo.load(Preset(name="test_preset", template_paths=[]))

        mock_open.assert_called_once_with(self.mock_base_dir / "test_preset.json", "r")

        self.assertEqual(preset.name, "test_preset")
        self.assertEqual(preset.template_paths, ["/path1", "/path2"])
     
    @patch("pathlib.Path.glob")
    def test_list_files_returns_file_names_without_extensions(self, mock_glob):
        self.mock_base_dir.glob.return_value = [
            Path("/fake/dir/preset1.json"),
            Path("/fake/dir/preset2.json"),
        ]

        files = self.repo.list_files()

        self.assertEqual(files, ["preset1", "preset2"])
        self.mock_base_dir.glob.assert_called_once_with("*.json")
    
    # @patch("pathlib.Path.exists")
    # def test_load_file_not_found(self, mock_exists):
    #     mock_exists.return_value = False

    #     with self.assertRaises(FileNotFoundError):
    #         self.repo.load(Preset(name="non_existent", template_paths=[]))
            
if __name__ == "__main__":
    unittest.main()
