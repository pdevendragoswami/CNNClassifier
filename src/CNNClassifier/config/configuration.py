import os
from pathlib import Path
from CNNClassifier.utils.utils import read_yaml,create_directory
from CNNClassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConfig,PrepareCallbacksConfig
from CNNClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH

class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,param_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(param_file_path)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            Source_URL = config.Source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir)

        return data_ingestion_config

    def get_prepare_base_model_config(self)-> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES)

        return prepare_base_model_config

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directory([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    

    def get_training_config(self)-> TrainingConfig :
        config = self.config.training
        prepare_base_model = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,'PetImages')
        create_directory([config.root_dir])

        training_config = TrainingConfig(
            root_dir = Path(config.root_dir),
            trained_model_path = Path(config.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = self.params.EPOCHS,
            params_batch_size = self.params.BATCH_SIZE,
            params_is_augmentation = self.params.AUGMENTATION,
            params_image_size = self.params.IMAGE_SIZE)

        return training_config

    def get_validation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=os.path.join(self.config.training.trained_model_path),
            training_data=os.path.join(self.config.data_ingestion.unzip_dir,'PetImages'),
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config

 