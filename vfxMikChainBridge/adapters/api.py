from vfxMikChainBridge.domain.ports.api import API

from vfxMikChainBridge.adapters.subprocess_launcher import SubprocessLauncherAdapter

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
    
    def get_collected_template_by_name(self, template_name):
        return self.templates_collector.get_collected_template_by_name(template_name)
    
    def get_global_variables_from_template_name(self, template_name):
        return self.templates_collector.get_global_variables_from_template_name(template_name)
    
    def execute_templates(self):
        template_executor = TemplatesExecutorService()
        template_executor.execute_templates()
    
    def launch_new_empty_mikchain(self):
        mikchain_launcher = SubprocessLauncherAdapter()
        mikchain_launcher.run("mikchain")

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
        templates_collector.add_template_to_collection(available_templates[1])


        print(f"collected templates after add : {collected_templates}")

        api.execute_templates(collected_templates)

        # api.clear_collection()
        # api.clear_available_templates()
        
        # print(f"collected templates after clear : {collected_templates}")
        # print(f"available templates after clear : {available_templates}")
        
        # specific_template = templates_collector.get_collected_template_by_name('auto_publish_test')
        # print(specific_template)
        # print(specific_template.name)
        
        # vars = templates_collector.get_global_variables_from_template_name('auto_publish_test')
        # print(vars)
        
    except ValueError as e:
        print(e)
            