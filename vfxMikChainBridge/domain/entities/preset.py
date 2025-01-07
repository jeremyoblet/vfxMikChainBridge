class Preset:
    def __init__(self, name, template_paths):
        self.name = name
        self.template_paths = template_paths

    def add_path(self, path):
        if path not in self.template_paths:
            self.template_paths.append(path)

    def remove_path(self, path):
        if path in self.template_paths:
            self.template_paths.remove(path)

    def has_path(self, path):
        return path in self.template_paths
