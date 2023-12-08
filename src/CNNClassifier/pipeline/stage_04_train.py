from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.stage_04_train import Training
from CNNClassifier.pipeline.stage_03_prepare_callback import callback_list
from CNNClassifier import logger
try:
    config = ConfigurationManager()

    #prepare_callbacks_config = config.get_prepare_callback_config()
    #prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
    #callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list=callback_list)
    #training.train()
    
except Exception as e:
    pass

