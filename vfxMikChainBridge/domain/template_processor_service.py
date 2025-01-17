from vfxMikChainBridge.domain.entities.template import Template
from vfxMikChainBridge.domain.entities.global_variable import GlobalVariable


class TemplateProcessorService:
    
    GLOBAL_VARIABLES_KEY = "environment"

    def __init__(self, template_repository):
        self.template_repository = template_repository
    
    def create_template_representation(self, absolute_file_path):
        """
        Create a representation of a template based on its file type.
        """
        template = Template(absolute_file_path)
        return template
    
    def load_template_data(self, template):
        data = self.template_repository.load(template.absolute_file_path)
        template.data = data

    def extract_global_variables(self, template):
        variables_data = self._get_value_by_key(template.data, self.GLOBAL_VARIABLES_KEY)
        return [GlobalVariable(value) for key, value in variables_data.items()]

    def _get_value_by_key(self, json_data, target_key):
        if target_key in json_data:
            return json_data[target_key]
        for key, value in json_data.items():
            if isinstance(value, dict):
                result = self._get_value_by_key(value, target_key)
                if result is not None:
                    return result
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        result = self._get_value_by_key(item, target_key)
                        if result is not None:
                            return result
        return None
    
# if __name__ == "__main__":
    
#     from vfxMikChainBridge.adapters.file_template_repository import FileTemplateRepository
    
#     # Initialisation
#     template_path = "/s/prods/crashtst/_admin/mikchain/templates/new_publish/executables/make_artefact.mc"
#     template = Template(template_path)
#     template_repository = FileTemplateRepository(template_path)
#     processor = TemplateProcessorService(template_repository)

#     # Chargement et traitement
#     processor.load_template_data(template)
#     template.global_variables = processor.extract_global_variables(template)

#     print(template.name)
#     print(template.uid)
#     print(template.absolute_file_path)
#     print(template.data)