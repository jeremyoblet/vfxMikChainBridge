from abc import ABC, abstractmethod

class FileRepository(ABC):
    @abstractmethod
    def save(self, absolute_file_path):
        pass

    @abstractmethod
    def load(self, absolute_file_path):
        pass

    @abstractmethod
    def list_files(self, absolute_path):
        """Give the list of the files contained in th edirectory."""
        pass
