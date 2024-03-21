import os

class PdfOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.pdf_files = []
        self.base_file_names = []
        self.full_file_paths = []
        self.get_files()  # Initialize files and related properties

    def get_files(self):
        # Gets the files in a folder and initializes PDF-related lists
        self.files = os.listdir(self.folder_path)
        self.filter_pdf_files()
        self.set_base_file_names()
        self.set_full_file_paths()

    def filter_pdf_files(self):
        # Filters out PDF files from self.files
        self.pdf_files = [file for file in self.files if file.endswith('.pdf')]

    def set_base_file_names(self):
        # Sets base file names for PDF files (without extension)
        for file in self.pdf_files:
            base_name = os.path.splitext(file)[0]
            self.base_file_names.append(base_name)

    def set_full_file_paths(self):
        # Sets full file paths for PDF files
        for file in self.pdf_files:
            full_path = os.path.join(self.folder_path, file)
            self.full_file_paths.append(full_path)

# Usage
banking = os.path.expanduser("~/Documents/e_banking")
my_files = PdfOrganizer(banking)
