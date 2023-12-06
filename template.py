import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

package_name = 'CNNClassifier'

list_of_files=[
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py",
   f"src/{package_name}/components/stage_01_data_ingestion.py",
   f"src/{package_name}/components/stage_02_prepare_base_model.py",
   f"src/{package_name}/components/stage_03_train.py",
   f"src/{package_name}/components/stage_04_evaluation.py",
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/utils/utils.py",
   f"src/{package_name}/config/__init__.py",
   f"src/{package_name}/config/configuration.py",
   f"src/{package_name}/pipeline/__init__.py",
   f"src/{package_name}/pipeline/stage_01_data_ingestion.py",
   f"src/{package_name}/pipeline/stage_02_prepare_base_model.py",
   f"src/{package_name}/pipeline/stage_03_train.py",
   f"src/{package_name}/pipeline/stage_04_evaluation.py", 
   f"src/{package_name}/pipeline/training.py",
   f"src/{package_name}/entity/__init__.py",
   f"src/{package_name}/entity/config_entity.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb",
   "README.md"]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir !='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'Creating file directory {file_dir} for file {file_name}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)):
        with open(file_path,'w') as f:
            logging.info(f'Empty file {file_path} is created')
            pass 
    else:
        logging.info(f'file {file_path} is already created.')
