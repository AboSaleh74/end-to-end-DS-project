from src.datascience import logger
from src.datascience.config.configration import ConfigurationManager
from src.datascience.components.data_validation import DataValiadtion


STATGE_NAME = "data_validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        
        
if __name__ == "__main__":
    try:
        logger.info(f"Starting the {STATGE_NAME}")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"Completed the {STATGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e