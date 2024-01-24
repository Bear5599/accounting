import tkinter as tk
import file_processor

class FileProcessorButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Processor")

        # Example of adding a button
        self.process_button = tk.Button(self.root, text="Process File", command=self.process_file)
        self.process_button.pack()

    def process_file(self):
        
        pass

    def run(self):
        self.root.mainloop()
