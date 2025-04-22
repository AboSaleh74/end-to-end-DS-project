import joblib
import pandas as pd
import numpy as np
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        try:
            self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
            
        except Exception as e:
            self.model = joblib.load(Path("model/model.joblib"))
        
    def predict(self,data):
        
        prediction = self.model.predict(data)
        
        return prediction
    