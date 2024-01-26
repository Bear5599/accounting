import os
from openpyxl import Workbook
import csv

accounting_folder = os.path.expanduser("~/Documents/accounting_files")


class FileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.full_file_paths = []
        self.search_results = []
        self.all_csv_content = []

    def get_files(self):
        # gets the files in a folder
        self.files = os.listdir(self.folder_path)
        return self.files

    def full_path(self):
        # appends the file names to the folder path
        for file in self.files:
            self.full_file_paths.append(os.path.join(self.folder_path, file))
        return self.full_file_paths

    def get_csv(self):
        # checks if files are .csv then combines them into a list
        self.get_files()
        csv_files = self.full_path()
        for file in csv_files:
            if file.endswith(".csv"):
                with open(file, "r") as acct_files:
                    for line in acct_files:
                        self.all_csv_content.append(line)
        return self.all_csv_content
    
    def search_all_files(self):
        self.get_csv()
        search = input("Search for a word in this file: ")
        
        for lines in self.all_csv_content:
            if search.lower() in lines.lower():
                self.search_results.append(lines)
        print(f"There are {len(self.search_results)} occurances of {search} in this file")
        for items in self.search_results:
            print(items)
        return self.search_results

    def combine_csvs_to_excel(self):
    # Step 1: Create a new Excel workbook
        workbook = Workbook()
        active_sheet = workbook.active
        self.full_path()

        # Step 2: Iterate over the CSV files
        for file in self.full_file_paths:
            if file.endswith(".csv"):
                # Create a new sheet for each CSV file
                sheet_name = os.path.basename(file).replace('.csv', '')
                if sheet_name == active_sheet.title:
                    sheet = active_sheet
                else:
                    sheet = workbook.create_sheet(title=sheet_name)
                with open(file, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        sheet.append(row)


        workbook.save(filename=os.path.join(self.folder_path, "combined_csv_files.xlsx"))






