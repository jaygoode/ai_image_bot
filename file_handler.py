import os


class FileHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def get_files(self):
        image_files = os.listdir(self.image_folder)
        return image_files

    def move_files(self, files):
        if isinstance(files, list):
            for file in files:
                os.rename(file, self.image_folder)
        else:
            os.rename(file, self.image_folder)
