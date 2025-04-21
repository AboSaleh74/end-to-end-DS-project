from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTrasformation
from src.datascience import logger

from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        
        try:
            with open("artifacts/data_validation/status.txt", "r") as file:
                status = file.read().split(" ")[-1]
                logger.info(f"Data Validation status: {status}")
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTrasformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Data Validation failed. Data Transformation cannot proceed.")
        except Exception as e:
            logger.exception(e)
            raise e
        

                