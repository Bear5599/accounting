import os
import csv
from openpyxl import Workbook

class FileProcesser:
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
            if file.endswith('.csv'):
                wb = Workbook()
                ws = wb.active

                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        ws.append(row)

                excel_file = file.replace('.csv', '.xlsx')
                wb.save(excel_file)

                print(f"Converted {file} to {excel_file}")
