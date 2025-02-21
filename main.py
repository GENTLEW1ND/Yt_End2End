from yt_mlProject import logger
from yt_mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from yt_mlProject.pipeline.stage_02_data_validaiton  import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
        logger.exception(e)
        raise e