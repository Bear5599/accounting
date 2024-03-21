import os


def get_files(self):
    # gets the files in a folder
    self.files = os.listdir(self.folder_path)
    return self.files
    
def get_names_without_ext(self):
    self.get_files()
    for files in self.files:
        if files.endswith(".csv"):
            self.base_file_names.append(os.path.basename(files.strip(".csv")))
    return self.base_file_names

def full_path(self):
    # appends the file names to the folder path
    for file in self.files:
        self.full_file_paths.append(os.path.join(self.folder_path, file))
    return self.full_file_paths