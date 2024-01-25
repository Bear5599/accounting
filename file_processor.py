import os
from openpyxl import Workbook
import pandas

accounting_folder = os.path.expanduser("~/Documents/accounting_files")

class FileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []

    def get_files(self):
        self.files = os.listdir(self.folder_path)

    def full_path(self):
        full_paths = []
        for file in self.files:
            full_paths.append(os.path.join(self.folder_path, file))
        return full_paths

    def csv_to_excel(self):
        self.get_files()
        csv_files = self.full_path()

        for file in csv_files:
            if file.endswith(".csv"):
                pass

fp_accnt_files = FileProcessor(accounting_folder)

fp_accnt_files.csv_to_excel()