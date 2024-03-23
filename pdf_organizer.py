import os
import PyPDF4
import tabula
import warnings

# Suppress specific FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning, message=".*errors='ignore' is deprecated.*")


class PdfOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.pdf_files = []
        self.base_file_names = []
        self.full_file_paths = []
        self.pdf_content = []
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

    def pdf_table(self):
        tables = tabula.read_pdf(self.full_file_paths[1], pages="all")
        with open("pdf_tables.txt", "a") as pdf_table:
            for table in tables:
                pdf_table.write(table.to_csv())  # Convert the DataFrame to string
                pdf_table.write("\n\n")  # Add some space between tables for readability


    def all_pdf_tables(self):
        with open("all_pdf_tables.txt", "a") as table_file:
            for pdf_location in self.full_file_paths:
                # Attempt to read tables from the current PDF
                tables = tabula.read_pdf(pdf_location, pages="all", multiple_tables=True)

                # Iterate over each table (DataFrame) found
                for table in tables:
                    # Convert the DataFrame to CSV format and write it to the file
                    table_file.write(table.to_csv(index=False))
                    table_file.write("\n\n")  # Add spacing for readability between tables

            

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
my_files.all_pdf_tables()
