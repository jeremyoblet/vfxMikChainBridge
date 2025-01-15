from vfxMikChainBridge.domain.ports.api import API


class APIAdapter(API):
    def __init__(self, services_container):
        self.collector_service = services_container.collector_service
        self.executor_service = services_container.executor_service
        self.templates_fetcher = services_container.templates_fetcher
    
    def fetch_templates(self):
        return self.templates_fetcher.list_absolute_templates_paths()
            
    def add_template_in_collection(self, template_path):
        self.collector_service.add_template_to_collection(template_path)

    def clear_collection(self):
        self.collector_service.clear_collection()

    def clear_available_templates(self):
        self.collector_service.clear_available_templates()

    def populate_available_templates(self):
        templates_files_in_dir = self.fetch_templates()
        
        for template_file in templates_files_in_dir:
            self.collector_service.add_template_to_available_templates(template_file)
        
    def get_available_templates(self):
        return self.collector_service.get_available_templates()
    
    def get_collected_templates(self):
        return self.collector_service.get_collected_templates()
    
    def get_collected_template_by_name(self, template_name):
        return self.collector_service.get_collected_template_by_name(template_name)
    
    def get_global_variables_from_template_name(self, template_name):
        return self.collector_service.get_global_variables_from_template_name(template_name)
    
    def execute_templates(self):
        template_executor = TemplatesExecutorService()
        template_executor.execute_templates()
    
    def launch_new_empty_mikchain(self):
        mikchain_launcher = SubprocessLauncherAdapter()
        mikchain_launcher.run("mikchain")
