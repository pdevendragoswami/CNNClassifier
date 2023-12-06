from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.stage_02_prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

config = ConfigurationManager()
prepare_base_model_config = config.get_prepare_base_model_config()
prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
prepare_base_model.get_base_model()
prepare_base_model.update_base_model()
