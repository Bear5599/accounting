from file_processor import FileProcessor
from app_buttons import FileProcessorButtons
import os



csv_files = os.path.expanduser("~/Documents/accounting_files")
accounting_folder = FileProcessor(csv_files)
accounting_folder.combine_csvs_to_excel()

