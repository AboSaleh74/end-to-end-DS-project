from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


stage_name="Data Ingestion stage"

try:
        logger.info(f"Starting the {stage_name}")
        obj = DataIngestionTrainingPipline()
        obj.initiate_data_ingestion()
        logger.info(f"Completed the {stage_name}")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "data validation stage"
try:
        logger.info(f"Starting the {STATGE_NAME}")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"Completed the {STATGE_NAME}")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "data transformation stage"

try:
        logger.info(f"Starting the {STATGE_NAME}")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f"Completed the {STATGE_NAME}")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "model trainer stage"

try:
        logger.info(f"Starting the {STATGE_NAME}")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f"Completed the {STATGE_NAME}")
except Exception as e:
        logger.exception(e)
        raise e

