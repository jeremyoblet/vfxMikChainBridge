import json
from pathlib import Path

from vfxMikChainBridge.domain.entities.preset import Preset
from vfxMikChainBridge.domain.ports.file_repository import FileRepository


class FilePresetRepository(FileRepository):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def save(self, preset):
        file_path = self.base_dir / f"{preset.name}.json"
        with open(file_path, "w") as file:
            json.dump({"name": preset.name, "paths": preset.template_paths}, file)

    def load(self, preset):
        file_path = self.base_dir / f"{preset.name}.json"
        if not file_path.exists():
            raise FileNotFoundError(f"Preset {preset.name} not found.")
        with open(file_path, "r") as file:
            data = json.load(file)
        return Preset(name=data["name"], template_paths=data["template_paths"])

    def list_files(self):
        return [file.stem for file in self.base_dir.glob("*.json")]
