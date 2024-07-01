import os
import yaml
from logger_setup import logger
import json


class FileHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.archive_image_folder = image_folder + "\\archive\\"

    def get_files(self):
        image_files = os.listdir(self.image_folder)
        return image_files

    def move_file(self, file):
        os.rename(file, self.archive_image_folder + "\\" + file)

    def create_ai_state_file(self, filepath):
        if not os.path.exists(filepath):
            try:
                data = {"models_active": [], "ollama_open": False}
                with open("state.yaml", "w") as yaml_file:
                    yaml.dump(data, yaml_file, default_flow_style=False)
            except Exception as e:
                logger.error(f"Failed to open yaml file. {e}")
        else:
            logger.info(f"ai state file already exists as filepath: {filepath}")

    def read_yaml_file(self, filepath):
        try:
            with open(filepath, "r") as yaml_file:
                logger.info(yaml.safe_load(yaml_file))
                return yaml.safe_load(yaml_file)
        except Exception as e:
            logger.error(f"Failed to open yaml file. {e}")
