import os


class FileHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.archive_image_folder = image_folder + "\\archive\\"

    def get_files(self):
        image_files = os.listdir(self.image_folder)
        return image_files

    def move_file(self, file):
        breakpoint()
        os.rename(file, self.archive_image_folder + "\\" + file)
