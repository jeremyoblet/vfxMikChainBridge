class GlobalVariable:
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.value = data_dict['value']
        self.type = data_dict['type']
