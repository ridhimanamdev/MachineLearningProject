##Mysql-->Train test split---> dataset

import os 
import sys
from src.MachineLearningProject import CustomException
from src.MachineLearningProject.logger import logging
import pandas as pd
from src.MachineLearningProject.utils import read_sql_data

from dataclasses import dataclass

@dataclass
class DataIngestioConfig:
    train_data_path:str=os.path.joins('artifact','train.csv')
    test_data_path:str=os.path.joins('artifact','test.csv')
    raw_data_path:str=os.path.joins('artifact','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestioConfig()

    def initiate_data_ingestion(self):
        try:
            #reading data from mysql 
            df= read_sql_data()
            logging.info("Reading from mysql dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            
        except Exception as e:
            raise CustomException(e,sys)
        

    
    