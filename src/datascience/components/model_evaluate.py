import os 
import mlflow
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from urllib.parse import urlparse
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from src.datascience.utils.common import save_json
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience import logger
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories,save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_report(self, y_true, y_pred):
        r2 = r2_score(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        
        report = {
            "r2_score": r2,
            "rmse": rmse,
            "mae": mae
        }
        
        return report
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        X_test = test_data.drop(self.config.target_column, axis=1)
        y_test = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme
        
        with mlflow.start_run():
            
            predicted_qualities = model.predict(X_test)
            (r2, rmse, mae) = self.eval_report(y_test, predicted_qualities).values()
            
            scores = {
                "r2_score": r2,
                "rmse": rmse,
                "mae": mae
            }
            save_json(path=Path(self.config.report_file_path), data=scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("r2_score", r2)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ElasticNet")
            else:
                mlflow.sklearn.log_model(model,"model")