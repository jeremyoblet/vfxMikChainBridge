from pathlib import Path
import uuid


class Template:
    def __init__(self, absolute_file_path):
        self.uid = uuid.uuid4()
        self.absolute_file_path = absolute_file_path
        self.name = Path(absolute_file_path).stem
        self.data = None
        self.global_variables = []
