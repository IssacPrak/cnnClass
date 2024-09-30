from cnnClass import logger
from cnnClass.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClass.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClass.pipeline.stage03_training import ModelTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"{STAGE_NAME} started")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.error(f"{STAGE_NAME} failed due to: {str(e)}")
    raise e



STAGE_NAME = "Model preparation stage"
try:
    logger.info(f"{STAGE_NAME} started")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.error(f"{STAGE_NAME} failed due to: {str(e)}")
    raise e



STAGE_NAME = "Training"
try:
    logger.info(f"{STAGE_NAME} started")
    # TODO: Implement training logic here
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.exception(f"{STAGE_NAME} failed due to: {str(e)}")
    raise e
