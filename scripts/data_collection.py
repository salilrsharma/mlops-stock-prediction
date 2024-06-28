import pandas as pd
import yfinance as yf
from setup_azure_storage import load_data_lake_client

ticker = ["AAPL", "MSFT", "AMZN", "NVDA"]

file_sys_client = load_data_lake_client()

for t in ticker:
    file_sys_client.create_directory(directory=t)
    data = yf.download(t)
    data.to_csv(t)

    # load data to the directory under file name hist_data
    dir_client = file_sys_client.get_directory_client(t)
    file_client = dir_client.get_file_client("hist_data")

    with open(file=t, mode="rb") as data:
        file_client.upload_data(data, overwrite=True)



