from file_processor import FileProcesser
from app_buttons import FileProcessorButtons

class FileMaker:
    def __init__(self, folder_path):
        self.file_processor = FileProcesser(folder_path)
        self.ui = FileProcessorButtons(self.file_processor)

    def run(self):
        self.ui.run()

if __name__ == "__main__":
    pass