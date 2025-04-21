import os
from src.datascience.config.configuration import DataTransformationConfig
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTrasformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_dir)
        
        train , test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Train test split completed")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)