class TemplatesCollectorService:
    def __init__(self, template_processor_service):
        self.template_processor_service = template_processor_service
        self._available_templates = []
        self._collected_templates = []

    def _create_template_from_path(self, template_path):
        new_template =  self.template_processor_service.create_template_representation(template_path)
        self.template_processor_service.load_template_data(new_template)
        new_template.global_variables = self.template_processor_service.extract_global_variables(new_template)
        return new_template

    def add_template_to_collection(self,template):
        template_representation = self._create_template_from_path(template)
        if template_representation not in self._collected_templates:
            self._collected_templates.append(template_representation)
            
    def remove_template_to_collection(self, template):
        if template in self._collected_templates:
            self._collected_templates.remove(template)
           
    def clear_collection(self):
            self._collected_templates.clear()

    def add_template_to_available_templates(self,template):
        if template not in self._available_templates:
            self._available_templates.append(template)
            
    def remove_template_to_available_templates(self, template):
        if template in self._available_templates:
            self._available_templates.remove(template)
          
    def clear_available_templates(self):
        self._available_templates.clear()
   
    def get_available_templates(self):
        return self._available_templates
    
    def get_collected_templates(self):
        return self._collected_templates
    
    def get_collected_template_by_name(self, template_name):
        for template in self._collected_templates:
            if template_name == template.name:
                return template
    
    def get_global_variables_from_template_name(self, template_name):
        template = self.get_collected_template_by_name(template_name)
        return template.global_variables
        
    def set_available_templates(self, templates):
        self._available_templates = templates
    
    def set_collected_templates(self, templates):
        self._collected_templates = templates
