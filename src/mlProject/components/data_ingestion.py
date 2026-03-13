import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.mlProject.logger import logging


class DataIngestion:

    def initiate_data_ingestion(self):

        logging.info("Reading dataset")

        df = pd.read_csv("data/train.csv", low_memory=False)

        os.makedirs("artifacts", exist_ok=True)

        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

        train_path = "artifacts/train.csv"
        test_path = "artifacts/test.csv"

        train_set.to_csv(train_path, index=False)
        test_set.to_csv(test_path, index=False)

        logging.info("Data Ingestion Completed")

        return train_path, test_path