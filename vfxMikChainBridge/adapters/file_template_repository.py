import json
from pathlib import Path

from vfxMikChainBridge.domain.ports.file_repository import FileRepository


class FileTemplateRepository(FileRepository):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    # def load(self, template_file):
    #     file_path = self.base_dir / f"{template_file.name}.json"
    #     if not file_path.exists():
    #         raise FileNotFoundError(f"Preset {template_file.name} not found.")
    #     with open(file_path, "r") as file:
    #         data = json.load(file)
    #     return Template(name=data["name"], template_paths=data["template_paths"])

    def list_files(self):
        return [file.stem for file in self.base_dir.glob("*.json")]
