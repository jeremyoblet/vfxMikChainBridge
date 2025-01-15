class TemplatesExecutorService:
    def __init__(self, templates_collector_service, binary_command, subprocess_runner):
        self.templates_collector_service = templates_collector_service
        self.binary_command = binary_command
        self.subprocess_runner = subprocess_runner
        self.collected_templates= None
        
    def collect_templates(self):
        self.collected_templates = self.templates_collector_service.get_collected_templates()
        print(self.collected_templates)
        
    def build_execution_command_from_global_variables(self, template):
        binary = self.binary_command + " "
        command = binary
        command = command + template.absolute_file_path
        global_variables = template.global_variables
        for variable in global_variables:
            command = command + " --"
            command = command + variable.name.lower() + "=" + variable.value.lower()
        return command

    def execute_templates(self):
        print(self.collect_templates)
        for template in self.collected_templates:
            command = self.build_execution_command_from_global_variables(template)
            print(command)
            self.subprocess_runner.run(command)
