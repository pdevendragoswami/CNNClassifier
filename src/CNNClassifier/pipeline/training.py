from CNNClassifier.components.stage_01_data_ingestion import DataIngestion
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier import logger
from CNNClassifier.components.stage_02_prepare_base_model import PrepareBaseModel
from CNNClassifier.components.stage_03_train import Training


config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()

#config = ConfigurationManager()
prepare_base_model_config = config.get_prepare_base_model_config()
prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
prepare_base_model.get_base_model()
prepare_base_model.update_base_model()





#config = ConfigurationManager()

training_config = config.get_training_config()
training = Training(config=training_config)
training.get_base_model()
training.train_valid_generator()
training.train()
