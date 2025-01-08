from pathlib import Path

from vfxMikChainBridge.domain.constants import TEMPLATES_FOLDER
from vfxMikChainBridge.domain.entities.template import Template
from vfxMikChainBridge.adapters.file_template_repository import FileTemplateRepository


class TemplatesFetcherService:
    def __init__(self):
        pass

    def list_absolute_templates_paths(self, absolute_directory_path):
        """
        Lists all JSON absolute file paths in a given directory.
        """
        templates_repository = FileTemplateRepository()
        return templates_repository.list_files(absolute_directory_path)

    def list_templates_names(self, absolute_directory_path):
        """
        Lists all JSON file names in a given directory.
        """
        absolute_paths = self.list_absolute_templates_paths(absolute_directory_path)
        return [Path(path).stem for path in absolute_paths]


if __name__ == "__main__":
    try:
        templates_fetcher = TemplatesFetcherService()

        template_paths = templates_fetcher.list_absolute_templates_paths(TEMPLATES_FOLDER)
        print(f"JSON file pqths found: {template_paths}")
        
        template_names = templates_fetcher.list_templates_names(TEMPLATES_FOLDER)
        print(f"JSON file names found: {template_names}")
    except ValueError as e:
        print(e)
