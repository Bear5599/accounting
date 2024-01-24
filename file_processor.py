import os
class FileProcesser:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []

    def get_files(self):
        self.files = os.listdir(self.folder_path)

    def full_path(self):
        # Generate a list of full file paths
        full_paths = []
        for file in self.files:
            full_paths.append(os.path.join(self.folder_path, file))
        return full_paths
