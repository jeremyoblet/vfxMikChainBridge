from vfxMikChainBridge.domain.entities.template import Template


class TemplateProcessorService:
    
    @staticmethod
    def create_template_representation(absolute_file_path):
        """
        Create a representation of a template based on its file type.
        """
        template = Template(absolute_file_path)
        return template
    
    @staticmethod
    def fill_template_global_variables(template, global_variables):
        """
        Fill the template with the provided global variables.
        """
        pass