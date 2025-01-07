from abc import ABC, abstractmethod

class FileRepository(ABC):
    @abstractmethod
    def save(self, file):
        pass

    @abstractmethod
    def load(self, file):
        pass

    @abstractmethod
    def list_files(self, path_directory):
        """Give the list of the files contained in th edirectory."""
        pass
