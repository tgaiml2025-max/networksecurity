import sys
from networksecurity.component.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngetionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngetionConfig(trainingpipelineconfig)
        data_ingetion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        
        dataingestionartifact = data_ingetion.initiate_data_ingestion()
        print(dataingestionartifact)
        
        
    except Exception as e:
            raise NetworkSecurityException(e,sys)
