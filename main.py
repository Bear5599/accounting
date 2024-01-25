from file_processor import FileProcessor
from app_buttons import FileProcessorButtons
import os

csv_files = os.path.expanduser("~/Documents/accounting_files")


class FileMaker:
    def __init__(self, folder_path):
        self.file_processor = FileProcessor(folder_path)
        self.ui = FileProcessorButtons(self.file_processor)

    def run(self):
        self.ui.run()

if __name__ == "__main__":
    my_files = FileMaker(csv_files)
    my_files.file_processor.full_path()
    