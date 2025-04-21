from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
from src.datascience.components.model_evaluate import ModelEvaluation


STAGE_NAME = "model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_evaluate_model(self):
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()
            model_eval = ModelEvaluation(config=model_eval_config)
            model_eval.log_into_mlflow()