from cnnClass import logger
from cnnClass.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"{STAGE_NAME} started")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.error(f"{STAGE_NAME} failed due to: {str(e)}")
    raise e

