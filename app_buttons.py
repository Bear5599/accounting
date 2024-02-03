import tkinter as tk
from file_processor import FileProcessor
from functools import partial
import os

folder_path = os.path.expanduser("~/Documents/accounting_files")

# creates buttons for the app, using the commands in file_processor.py
class FileProcessorButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Searching App")
        self.file_processor = FileProcessor(folder_path)
        self.button_names = self.file_processor.get_names_without_ext()
        self.first_buttons = []
        self.row_two_entry = tk.Entry(self.root) 

    def first_buttons_creator(self):
        self.file_processor.file_scanner()
        button_names = self.file_processor.file_dict
        for names in button_names:
            # Create a partial function with the current 'names' as argument
            my_command = partial(self.button_command, names)
            csv_button = tk.Button(self.root, text=names, command=my_command)
            csv_button.pack()
            self.first_buttons.append(csv_button)

    def button_command(self, key):
        # When this function is called it creates the data from the file
        # and puts it in file_processor.py to be muniplulated
        content = self.file_processor.file_dict[key]
        self.file_processor.button_content.append(content)
        for buttons in self.first_buttons:
            buttons.pack_forget()
        self.second_buttons_creator()

    def second_buttons_creator(self):
        self.row_two_entry.pack()
        row_one = tk.Button(self.root, text="Search for a term in the file", command=self.second_buttons_commands)
        row_one.pack()

    def second_buttons_commands(self):
        text = self.row_two_entry.get()
        print(text)
        self.file_processor.search_one_file(text)
        

    def run(self):
        # this should do everything so the only command is run
        self.root.mainloop()

my_folder = FileProcessorButtons()
my_folder.first_buttons_creator()
my_folder.run()