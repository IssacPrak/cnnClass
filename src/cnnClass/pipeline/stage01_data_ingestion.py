from cnnClass.config.configuration import ConfigurationManager
from cnnClass.components.data_ingestion import DataIngestion
from cnnClass import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Starting data Ingestion pipeline : {STAGE_NAME}...")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed successfully")

    except Exception as e:
        logger.error(f"An error occurred in {STAGE_NAME} : {str(e)}")
        logger.exception(e)
        raise e