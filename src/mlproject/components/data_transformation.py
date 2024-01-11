import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd 
from mlproject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        ##we can add different datatransformation techniques such as pca,Scarl and all, 
        ## we can perform all kind of EDA
        #probable here we are adding only train test split.

    def train_test_splitting(self):
            df1=pd.read_csv(self.config.data_path)
            #df=df1.drop(['Id'],axis=1,inplace=True)

            train,test=train_test_split(df1)

            train.to_csv(os.path.join(self.config.root_dir, 'train.csv'),index=False)
            test.to_csv(os.path.join(self.config.root_dir, 'test.csv'),index=False)

            logger.info("splitted data into training and test sets")
            logger.info(train.shape)
            logger.info(test.shape)

            print(train.shape)
            print(test.shape)
            #return 'done'
            