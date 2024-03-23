import os
import PyPDF4

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

    def pdf_to_text(self):
        with open("pdf_text.txt", "a") as pdf_pages:  # Open the output file once, outside the loop
            for pdf in self.full_file_paths:
                with open(pdf, 'rb') as pdf_file:
                    pdf_reader = PyPDF4.PdfFileReader(pdf_file)
                    num_pages = pdf_reader.numPages
                    
                    for page_num in range(num_pages):
                        page_obj = pdf_reader.getPage(page_num)
                        text = page_obj.extractText()
                        pdf_pages.write(text)  # Write the extracted text to the file

                



# Usage
banking = os.path.expanduser("~/Documents/e_banking")
my_files = PdfOrganizer(banking)
my_files.pdf_to_text()
