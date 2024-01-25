import os
from openpyxl import Workbook

accounting_folder = os.path.expanduser("~/Documents/accounting_files")

class FileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.all_files_content = []

    def get_files(self):
        # gets the files in a folder
        self.files = os.listdir(self.folder_path)

    def full_path(self):
        # appends the file names to the folder path
        full_paths = []
        for file in self.files:
            full_paths.append(os.path.join(self.folder_path, file))
        return full_paths

    def csv_to_excel(self):
        # checks if files are .csv then combines them into a list
        self.get_files()
        csv_files = self.full_path()
        

        for file in csv_files:
            if file.endswith(".csv"):
                with open(file, "r") as acct_files:
                    for line in acct_files:
                        self.all_files_content.append(line)
                    
    def search_through_all(self, search):
        result = []
        for lines in self.all_files_content:
            if search.lower() in lines.lower():
                result.append(lines)
        print(len(result))
                


fp_accnt_files = FileProcessor(accounting_folder)
fp_accnt_files.csv_to_excel()
user_input = input("Search through the csv files: ")
fp_accnt_files.search_through_all(user_input)