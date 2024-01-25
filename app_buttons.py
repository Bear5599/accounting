import tkinter as tk
from file_processor import FileProcessor
import os

folder_path = os.path.expanduser("~/Documents/accounting_files")

# creates buttons for the app, using the commands in file_processor.py
class FileProcessorButtons:
    def __init__(self, button_maker):
        self.root = tk.Tk()
        self.root.title("File Processor")
        self.button_maker = button_maker
        self.file_process = FileProcessor(button_maker)

        # Example of adding a button
        self.process_button = tk.Button(self.root, text="Process File", command=self.process_file)
        self.process_button.pack()

    def button_creator(self):
        self.file_process
        

    def run(self):
        self.root.mainloop()
