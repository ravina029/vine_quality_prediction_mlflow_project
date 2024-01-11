from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import  DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME="Data ingestion stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data validation stage'

try:
        logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME='Data Transformation stage'
try:
        logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
         logger.exception(e)
         raise e       

STAGE_NAME='Model trai ning stage'

try:
        logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
        obj=ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
except Exception as e:
        logger.exception(e)
        raise e       




    
 
        