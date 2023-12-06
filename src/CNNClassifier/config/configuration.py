import os
from pathlib import Path
from CNNClassifier.utils.utils import read_yaml,create_directory
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH

class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,param_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(param_file_path)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        #why self here
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            #why not here
            root_dir = config.root_dir,
            Source_URL = config.Source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir)

        return data_ingestion_config
        