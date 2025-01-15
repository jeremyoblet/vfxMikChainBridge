from vfxMikChainBridge.domain.entities.template import Template


class TemplateProcessorService:
    def __init__(self, template_repository):
        self.template_repository = template_repository
    
    def create_template_representation(self, absolute_file_path):
        """
        Create a representation of a template based on its file type.
        """
        template = Template(absolute_file_path, self.template_repository)
        return template
    
    def fill_template_global_variables(self, template, global_variables):
        """
        Fill the template with the provided global variables.
        """
        pass