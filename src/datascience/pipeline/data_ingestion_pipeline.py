from dataclasses import dataclass
from src.datascience.config.configration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger


stage_name="Data Ingestion stage"

class DataIngestionTrainingPipline:
    def __init__(self):
        pass
    
    def initate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__=="__main__":
    try:
        logger.info(f"Starting the {stage_name}")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f"Completed the {stage_name}")
    except Exception as e:
        logger.exception(e)
        raise e