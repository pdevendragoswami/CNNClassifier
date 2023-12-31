import os
from pathlib import Path
from urllib import request
from zipfile import ZipFile
from CNNClassifier import logger
from tqdm import tqdm
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.utils import utils

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f'trying to download the file')
            request.urlretrieve(url = self.config.Source_URL, filename = self.config.local_data_file)
        else:
            logger.info(f"file {self.config.local_data_file} already exist")
    
    def get_updated_list_of_files(self,list_of_files):
        return [file for file in list_of_files if file.endswith('.jpg')]

    def preprocess(self,zipfile,file,working_dir):
        target_file_path = os.path.join(working_dir,file)
        if not os.path.exists(target_file_path):
            zipfile.extract(file,working_dir)

        if os.path.getsize(target_file_path) == 0:
            logger.info(f"removing file:{target_file_path} of size: {os.path.getsize(target_file_path)}")
            os.remove(target_file_path)


    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode = 'r') as zipfile:
            list_of_files = zipfile.namelist()
            updated_list_of_files = self.get_updated_list_of_files(list_of_files)
            for file in tqdm(updated_list_of_files):
                self.preprocess(zipfile, file, self.config.unzip_dir)
                
