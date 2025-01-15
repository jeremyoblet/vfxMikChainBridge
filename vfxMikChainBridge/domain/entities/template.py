from pathlib import Path
import uuid

from vfxMikChainBridge.domain.entities.global_variable import GlobalVariable


class Template:
    
    GLOBAL_VARIABLES_KEY = "environment"
    
    def __init__(self, absolute_file_path, template_repository):
        self.absolute_file_path = absolute_file_path
        self.template_repository = template_repository
        self.uid = uuid.uuid4()
        self.name = Path(absolute_file_path).stem
        self.data = self.get_file_template_data()
        self.global_variables = self._add_global_variables()

    def get_file_template_data(self):
        data = self.template_repository.load(self.absolute_file_path)
        return data
        
    def get_global_variables_data(self):
        global_variables = self._get_value_by_key(self.data, self.GLOBAL_VARIABLES_KEY)
        return global_variables
    
    def _get_value_by_key(self, json_data, target_key):
        """
        Recursively searches a JSON dictionary and returns the value associated with a given key.

        :param json_data: The JSON dictionary to search.
        :type json_data: dict
        :param target_key: The key to search for in the JSON data.
        :type target_key: str
        :returns: The value associated with the key, or None if the key is not found.
        :rtype: any
        """
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
    
    def _add_global_variables(self):
        variables_data = self.get_global_variables_data()
        return  [GlobalVariable(value) for key, value in variables_data.items()]
 