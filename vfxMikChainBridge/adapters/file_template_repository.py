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

    def load(self, file_path):
        """
        Loads the JSON data from the specified file.

        :param file_path: The absolute path to the JSON file.
        :type file_path: str
        :returns: The parsed JSON data as a dictionary.
        :rtype: dict
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file content is not valid JSON.
        """
        file = Path(file_path)

        if not file.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with file.open("r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file: {file_path}. Error: {e}")

    def list_files(self, absolute_path):
        """
        Lists all JSON files in the specified directory with their absolute paths.

        :param absolute_path: The absolute path to the directory.
        :returns: A list of absolute paths to JSON files in the directory.
        :rtype: list[str]
        """
        return [str(file.resolve()) for file in Path(absolute_path).glob("*.mc")]
