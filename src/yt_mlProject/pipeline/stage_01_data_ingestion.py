## Not in use Right now and some changes are needed in config_entity file to extract zip file.
## Also some changes are needed in configuration.py file for the same reason

from yt_mlProject.config.configuration import ConfigurationManager
from yt_mlProject.components.data_ingestion import dataIngestion
from yt_mlProject import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = dataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e