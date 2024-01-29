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
        self.button_content = []

        # Example of adding a button
        
    def first_buttons_creator(self):
        self.file_processor.list_of_csvs()
        button_content = self.file_processor.list_of_csv_files

        for index, name in enumerate(self.button_names):
            # Ensure button_content has the same number of items as button_names
            if len(button_content) != len(self.button_names):
                print("Error: Button names and content count do not match.")
                return

            content = button_content[index]
            csv_button = tk.Button(self.root, text=name, command=lambda c=content: self.first_button_commands(c))
            csv_button.pack()
            self.first_buttons.append(csv_button)

    def first_button_commands(self, content):
        for buttons in self.first_buttons:
            buttons.pack_forget()
        self.button_content.append(content)
        self.file_processor.search_one_file()
        return content 
    
    def second_button_commands(self):
        # create a search bar that searches through the items in self.button_content
        pass

    def run(self):
        # this should do everything so the only command is run
        self.root.mainloop()

my_folder = FileProcessorButtons()
my_folder.first_buttons_creator()
my_folder.run()