from typing_extensions import Self
from vfxMikChainBridge.domain.ports.api import API

from vfxMikChainBridge.domain.template_processor_service import TemplateProcessorService
from vfxMikChainBridge.domain.templates_collector_service import TemplatesCollectorService
from vfxMikChainBridge.domain.templates_executor_service import TemplatesExecutorService
from vfxMikChainBridge.domain.templates_fetcher_service import TemplatesFetcherService

from vfxMikChainBridge.domain.constants import TEMPLATES_FOLDER


class APIAdapter(API):
    def __init__(self, templates_collector, templates_fetcher):
        self.template_processor = None
        self.templates_collector = templates_collector
        self.templates_executor = None
        self.templates_fetcher = templates_fetcher
    
    def fetch_templates(self, path_directory):
        return self.templates_fetcher.list_absolute_templates_paths(path_directory)
            
    def add_template_in_collection(self, template_path):
        self.templates_collector.add_template_to_collection(template_path)

    def clear_collection(self):
        self.templates_collector.clear_collection()

    def clear_available_templates(self):
        self.templates_collector.clear_available_templates()

    def populate_available_templates(self):
        templates_files_in_dir = self.fetch_templates(TEMPLATES_FOLDER)
        
        for template_file in templates_files_in_dir:
            self.templates_collector.add_template_to_available_templates(template_file)
        
    def get_available_templates(self):
        return self.templates_collector.get_available_templates()
    
    def get_collected_templates(self):
        return self.templates_collector.get_collected_templates()
    
    def execute_all_templates(self):
        pass
    
    def launch_new_empty_mikchain(self):
        pass


if __name__ == "__main__":
    try:
        # instantiate modules
        templates_collector = TemplatesCollectorService()
        templates_fetcher = TemplatesFetcherService()
        api = APIAdapter(templates_collector, templates_fetcher)
        
        # get templates
        templates_files_in_dir = api.fetch_templates(TEMPLATES_FOLDER)

        for template_file in templates_files_in_dir:
            templates_collector.add_template_to_available_templates(template_file)

        available_templates = api.get_available_templates()
        print(f"available templates : {available_templates}")
        
        collected_templates = api.get_collected_templates()
        print(f"collected templates : {collected_templates}")

        templates_collector.add_template_to_collection(available_templates[0])
        print(f"collected templates after add : {collected_templates}")

        api.clear_collection()
        api.clear_available_templates()
        
        print(f"collected templates after clear : {collected_templates}")
        print(f"available templates after clear : {available_templates}")
    except ValueError as e:
        print(e)
            