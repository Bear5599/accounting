import tkinter as tk
from file_processor import FileProcesser
import os

folder_path = os.path.expanduser("~/Documents/")

class FileProcessorButtons:
    def __init__(self, button_maker):
        self.root = tk.Tk()
        self.root.title("File Processor")
        self.button_maker = button_maker

        # Example of adding a button
        self.process_button = tk.Button(self.root, text="Process File", command=self.process_file)
        self.process_button.pack()

    def button_creator(self):
        pass

    def run(self):
        self.root.mainloop()
