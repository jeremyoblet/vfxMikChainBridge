import unittest
from unittest.mock import MagicMock

from vfxMikChainBridge.domain.templates_fetcher_service import TemplatesFetcherService


class TestTemplatesFetcherService(unittest.TestCase):
    def setUp(self):
        """
        Prépare les mocks et l'instance de TemplatesFetcherService avant chaque test.
        """
        self.mock_repository = MagicMock() 
        self.fetcher_service = TemplatesFetcherService(templates_repository=self.mock_repository)

    def test_list_absolute_templates_paths(self):
        """
        Teste que list_absolute_templates_paths retourne les chemins absolus corrects.
        """
        self.mock_repository.list_files.return_value = [
            "/path/to/template1.json",
            "/path/to/template2.json",
        ]
        
        result = self.fetcher_service.list_absolute_templates_paths("/absolute/path")
        self.mock_repository.list_files.assert_called_once_with("/absolute/path")
        self.assertEqual(result, ["/path/to/template1.json", "/path/to/template2.json"])

    def test_list_templates_names(self):
        """
        Teste que list_templates_names retourne les noms de fichiers sans extensions.
        """
        self.mock_repository.list_files.return_value = [
            "/path/to/template1.json",
            "/path/to/template2.json",
        ]
        
        result = self.fetcher_service.list_templates_names("/absolute/path")
        expected_result = ["template1", "template2"]
        self.mock_repository.list_files.assert_called_once_with("/absolute/path")
        self.assertEqual(result, expected_result)

    def test_list_templates_names_no_files(self):
        """
        Teste que list_templates_names retourne une liste vide si aucun fichier n'est trouvé.
        """
        self.mock_repository.list_files.return_value = []
        result = self.fetcher_service.list_templates_names("/absolute/path")
        expected_result = []
        
        self.mock_repository.list_files.assert_called_once_with("/absolute/path")
        self.assertEqual(result, expected_result)

    def test_list_absolute_templates_paths_invalid_path(self):
        """
        Teste que list_absolute_templates_paths lève une exception si un chemin invalide est utilisé.
        """
        self.mock_repository.list_files.side_effect = FileNotFoundError("Invalid directory")
        
        with self.assertRaises(FileNotFoundError):
            self.fetcher_service.list_absolute_templates_paths("/invalid/path")
        
        self.mock_repository.list_files.assert_called_once_with("/invalid/path")


if __name__ == "__main__":
    unittest.main()
