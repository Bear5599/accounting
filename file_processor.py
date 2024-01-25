import os
from openpyxl import Workbook

accounting_folder = os.path.expanduser("~/Documents/accounting_files")
user_input = input("Search through the csv files: ")


class FileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.all_files_content = []
        self.search_results = []

    def get_files(self):
        # gets the files in a folder
        self.files = os.listdir(self.folder_path)
        return self.files

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
        return self.all_files_content
                    
    def search_all_files(self, search):
        for lines in self.all_files_content:
            if search.lower() in lines.lower():
                self.search_results.append(lines)
        print(f"There are {len(self.search_results)} occurances in this file")
        for items in self.search_results:
            print(items)
        return self.search_results


