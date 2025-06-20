import pandas as pd
import os

@data_loader
def check(*args, **kwargs) -> None:
    """
    Function to check the parquet creation
    """
    path = "data/output/"
    files = os.listdir(path)
    
    for file in files:
        df = pd.read_parquet(f"{path}{file}")
        print(df)