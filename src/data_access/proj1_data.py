import sys
import pandas as pd
import numpy as np
from typing import Optional
from dotenv import load_dotenv
import os

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME, COLLECTION_NAME
from src.exception import MyException

load_dotenv()

class Proj1Data:
    def __init__(self) -> None:
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                print(f"Using default database: {self.mongo_client.database.name}")
                collection = self.mongo_client.database[collection_name]
            else:
                print(f"Using passed database: {database_name}")
                collection = self.mongo_client.mongo_client[database_name][collection_name]

            print(f"Fetching data from MongoDB collection: {collection_name}")
            documents = list(collection.find())
            print(f"✅ Documents fetched: {len(documents)}")

            if not documents:
                raise Exception(f"No documents found in MongoDB collection '{collection_name}'")

            df = pd.DataFrame(documents)

            if "id" in df.columns.to_list():
                df.drop(columns=["id"], inplace=True)

            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)


