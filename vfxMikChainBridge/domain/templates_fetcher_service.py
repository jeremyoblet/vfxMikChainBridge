from pathlib import Path


class TemplatesFetcherService:
    def __init__(self, templates_repository):
        """
        Service for fetching templates.

        :param templates_repository: Instance of a repository to interact with file templates.
        """
        self.templates_repository = templates_repository


    def list_absolute_templates_paths(self):
        """
        Lists all JSON absolute file paths in a given directory.

        :param absolute_directory_path: Absolute path to the directory to search.
        :return: List of absolute paths to JSON files.
        """
        return self.templates_repository.list_files()

    def list_templates_names(self):
        """
        Lists all JSON file names (without extensions) in a given directory.

        :param absolute_directory_path: Absolute path to the directory to search.
        :return: List of template names (file names without extensions).
        """
        absolute_paths = self.list_absolute_templates_paths()
        return [Path(path).stem for path in absolute_paths]
