import tkinter as tk
from file_processor import FileProcessor
import os

folder_path = os.path.expanduser("~/Documents/accounting_files")

# creates buttons for the app, using the commands in file_processor.py
class FileProcessorButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Processor")
        self.file_processor = FileProcessor(folder_path)
        self.button_names = self.file_processor.get_names_without_ext()

        # Example of adding a button
        
    def button_creator(self):
        pass
        

    def run(self):
        self.root.mainloop()

my_folder = FileProcessorButtons()
print(my_folder.button_names)