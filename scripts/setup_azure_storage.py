import os
from dotenv import load_dotenv, dotenv_values 

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

# loading variables from .env file
load_dotenv() 

def get_connection_string():
    return os.getenv("AZURE_STORAGE_CONNECTION_STRING")

def load_data_lake_client():
    account_url = "https://stmlops.blob.core.windows.net/" 
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    datalake_service_client = DataLakeServiceClient.from_connection_string(connection_string)

    file_sys_name = "stock_data"

    try:
        datalake_service_client.create_file_system(file_system="stock-data")
    except:
        print(f"Container {file_sys_name} already exists")

    file_sys_client = datalake_service_client.get_file_system_client(file_system="stock-data")

    return file_sys_client
