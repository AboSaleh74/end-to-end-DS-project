from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

stage_name="Data Ingestion stage"

try:
        logger.info(f"Starting the {stage_name}")
        obj = DataIngestionTrainingPipline()
        obj.initate_data_ingestion()
        logger.info(f"Completed the {stage_name}")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "data_validation"
try:
        logger.info(f"Starting the {STATGE_NAME}")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"Completed the {STATGE_NAME}")
except Exception as e:
        logger.exception(e)
        raise e
