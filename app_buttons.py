import tkinter as tk
from file_processor import FileProcessor
from functools import partial
import os

folder_path = os.path.expanduser("~/Documents/accounting_files")

# creates buttons for the app, using the commands in file_processor.py
class FileProcessorButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Converter app")
        self.file_processor = FileProcessor(folder_path)
        self.button_names = self.file_processor.get_names_without_ext()
        self.first_buttons = []
        self.row_two_entry = tk.Entry(self.root)  # Store Entry as an instance variable
        self.row_two_entry.bind("<Return>", self.on_enter)

        # Example of adding a button

    def button_command(self, key):
        content = self.file_processor.file_dict[key]
        # Perform actions with 'content'
        return content
    def first_buttons_creator(self):
        self.file_processor.file_scanner()
        button_names = self.file_processor.file_dict
        for names in button_names:
            # Create a partial function with the current 'names' as argument
            my_command = partial(self.button_command, names)
            csv_button = tk.Button(self.root, text=names, command=my_command)
            csv_button.pack()

    # def first_buttons_creator(self):
    #     self.file_processor.list_of_csvs()
    #     button_content = self.file_processor.list_of_csv_files

    #     for index, name in enumerate(self.button_names):
    #         # Ensure button_content has the same number of items as button_names
    #         if len(button_content) != len(self.button_names):
    #             print("Error: Button names and content count do not match.")
    #             return

    #         content = button_content[index]
    #         csv_button = tk.Button(self.root, text=name, command=lambda c=content: self.first_buttons_commands(c))
    #         csv_button.pack()
    #         self.first_buttons.append(csv_button)

    def first_buttons_commands(self, content):
        for buttons in self.first_buttons:
            buttons.pack_forget()
        self.file_processor.button_content.append(content)
        self.second_buttons_creator()

    def second_buttons_creator(self):
        self.row_two_entry.pack()
        row_one = tk.Button(self.root, text="Search for a term in the file", command=self.second_buttons_commands)
        row_one.pack()

    def second_buttons_commands(self):
        text = self.row_two_entry.get()
        self.file_processor.search_one_file(text)
        print(self.file_processor.one_file_search)
        self.row_two_entry.delete(0, tk.END)  # Clear the entry here

    def on_enter(self, event=None):  # Optional event argument
        self.row_two_entry.delete(0, tk.END)

    def run(self):
        # this should do everything so the only command is run
        self.root.mainloop()

my_folder = FileProcessorButtons()
my_folder.first_buttons_creator()
my_folder.run()