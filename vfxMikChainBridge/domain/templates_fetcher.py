import os

from vfxMikChainBridge.domain.constants import TEMPLATES_FOLDER
from vfxMikChainBridge.adapters.file_template_repository import FilePresetRepository


class TemplatesHandler:
    def __init__(self):
        pass

    def list_json_files(self, directory_path):
        """
        Lists all JSON files in a given directory.
        """
        if not os.path.isdir(directory_path):
            raise ValueError(f"Le chemin spécifié n'est pas un répertoire valide : {directory_path}")
        
        json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]
        return json_files


if __name__ == "__main__":
    try:
        templates_handler = TemplatesHandler()
        fichiers_json = templates_handler.list_json_files(TEMPLATES_FOLDER)
        print(f"JSON files found : {fichiers_json}")
    except ValueError as e:
        print(e)
            