# program for converting bills into searchable files for excell
import os

accounting_files_dir = os.path.expanduser("~/Documents/accounting_files")

def file_finder(directory):
    file_names = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            file_names.append(full_path)
    print(file_names)
    return file_names

