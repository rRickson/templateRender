class BaseTemplate:
    def __init__(self):
        self.file_name = ""

    def create_file(self):
        self.set_file_name()
        self.set_file_content()
        self.build()

    def set_file_name(self, file_name):
        self.file_name = file_name;

    def set_file_content(self):
        pass

    def build(self):
        pass
