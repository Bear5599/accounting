import tkinter as tk
from file_processor import FileProcessor
import os
import time

folder_path = os.path.expanduser("~/Documents/accounting_files")

# creates buttons for the app, using the commands in file_processor.py
class FileProcessorButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Converter app")
        self.file_processor = FileProcessor(folder_path)
        self.button_names = self.file_processor.get_names_without_ext()
        self.first_buttons = []

        # Example of adding a button
        
    def first_buttons_creator(self):
        for names in self.button_names:
            csv_buttons = tk.Button(self.root, text=names)
            csv_buttons.pack()
            self.first_buttons.append(names)

    def hide_first_buttons(self):
        for buttons in self.first_buttons:
            buttons.pack_forget()
        

    def run(self):
        # this should do everything so the only command is run
        self.root.mainloop()

my_folder = FileProcessorButtons()
my_folder.first_buttons_creator()
my_folder.run()