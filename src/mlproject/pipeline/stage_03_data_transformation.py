from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path


STAGE_NAME='Data Transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("/Users/ravina/Desktop/project_mlflow/artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("your data scheme is not valid")

        except Exception as e:
            print(e) 

if __name__=='__main__':
    try:
        logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x=============x")
    except Exception as e:
         logger.exception(e)
         raise e       

