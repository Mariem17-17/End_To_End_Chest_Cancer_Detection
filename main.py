from CNN_classifier import logger
from CNN_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNN_classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from CNN_classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Mariem17-17/End_To_End_Chest_Cancer_Detection.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Mariem17-17"
os.environ["MLFLOW_TRACKING_PASSWORD"]="b2cb51c880480b3e7ecabc262adbc2bd575b7555"

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e