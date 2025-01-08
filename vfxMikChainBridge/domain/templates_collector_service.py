from vfxMikChainBridge.domain.template_processor_service import TemplateProcessorService


class TemplatesCollectorService:
    def __init__(self):
        self._available_templates = []
        self._collected_templates = []

    def create_template_from_path(self, template_path):
        return TemplateProcessorService().create_template_representation(template_path)

    def add_template_to_collection(self,template):
        template_representation = self.create_template_from_path(template)
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
    
    def set_available_templates(self, templates):
        self._available_templates = templates
    
    def set_collected_templates(self, templates):
        self._collected_templates = templates

  
if __name__ == "__main__":
    try:
        templates_collector = TemplatesCollectorService()
    except ValueError as e:
        print(e)