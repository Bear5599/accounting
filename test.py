import tkinter as tk
import os

folder = os.path.expanduser("~/Documents/accounting_files")

def file_scanner():
    file_dict = {}

    my_folder = os.listdir(folder)
    for item in my_folder:
        if item.endswith(".csv"):
            full_path = os.path.join(folder, item)
            file_name_no_extension = os.path.splitext(item)[0]

            with open(full_path, "r") as file:
                file_content = file.read()
                file_dict[file_name_no_extension] = file_content

    print(file_dict)
    return file_dict  # You might want to return this dictionary for further use

file_scanner()
