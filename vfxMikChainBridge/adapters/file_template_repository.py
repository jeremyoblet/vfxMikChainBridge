import json
from pathlib import Path

from vfxMikChainBridge.domain.ports.file_repository import FileRepository


class FileTemplateRepository(FileRepository):
    """
    This class implements the FileRepository interface and provides methods to 
    interact with template files stored on the filesystem.
    """
    
    def __init__(self):
        pass
        
    def save(self, absolute_file_path):
        """
        This method is a placeholder for saving a template file.
        Currently, saving templates is not required.

        :param absolute_file_path: The absolute path of the file to save.
        """
        pass

    def load(self, absolute_file_path):
        """
        This method is a placeholder for loading a template file content.
        Currently, saving templates is not required.

        :param absolute_file_path: The absolute path of the file to load.
        """
        pass

    def list_files(self, absolute_path):
        """
        Lists all JSON files in the specified directory with their absolute paths.

        :param absolute_path: The absolute path to the directory.
        :returns: A list of absolute paths to JSON files in the directory.
        :rtype: list[str]
        """
        return [str(file.resolve()) for file in Path(absolute_path).glob("*.json")]
