from dataclasses import dataclass
from pathlib import Path
from CNNClassifier import logger

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_data_file:Path
    unzip_dir:Path