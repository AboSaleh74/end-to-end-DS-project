from src.datascience import logger
from src.datascience.config.configuration import modelTrainerConfig
from  sklearn.linear_model import ElasticNet
import joblib
import os
import pandas as pd



class ModelTrainer:
    def __init__(self,config: modelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_dir)
        test_data = pd.read_csv(self.config.test_data_dir)
        
        train_x = train_data.drop(columns=[self.config.target_column], axis=1)
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        lr = ElasticNet(
            alpha=self.config.aplha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        lr.fit(train_x, train_y)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))