from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def fetch_templates(self):
        pass
    
    @abstractmethod
    def add_template_in_collection(self, template_path):
        pass
    
    @abstractmethod
    def clear_collection(self):
        pass

    @abstractmethod
    def clear_available_templates(self):
        pass
    
    @abstractmethod
    def populate_available_templates(self):
        pass
    
    @abstractmethod
    def get_available_templates(self):
        pass
    
    @abstractmethod
    def get_collected_templates(self):
        pass
    
    @abstractmethod
    def execute_templates(self):
        pass
    
    @abstractmethod
    def launch_new_empty_mikchain(self):
        pass
