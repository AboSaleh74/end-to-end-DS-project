from src.datascience import logger
import os
from dotenv import load_dotenv
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STATGE_NAME = "Data Ingestion stage"

try:
        logger.info(f"Starting the >>>>>{STATGE_NAME}<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.initiate_data_ingestion()
        logger.info(f"Completed the >>>>>{STATGE_NAME}<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "data validation stage"
try:
        logger.info(f"Starting the >>>>>{STATGE_NAME}<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"Completed the >>>>>{STATGE_NAME}<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "data transformation stage"

try:
        logger.info(f"Starting the >>>>>{STATGE_NAME}<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f"Completed the >>>>>{STATGE_NAME}<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "model trainer stage"

try:
        logger.info(f"Starting the >>>>>{STATGE_NAME}<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f"Completed the >>>>>{STATGE_NAME}<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STATGE_NAME = "model evaluation stage"

load_dotenv

os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

try : 
        logger.info(f"Starting the >>>>>{STATGE_NAME}<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_evaluate_model()
        logger.info(f"Completed the >>>>>{STATGE_NAME}<<<<<")
except Exception as e:
        logger.exception(e)
        raise e