import pandas as pd

from setup_azure_storage import get_connection_string

df = pd.read_csv('https://stmlops.blob.core.windows.net/stock-data/AAPL/hist_data', storage_options={"account_name": "mlops", "access_key": ""})