import pandas as pd

@transformer
def transform(data: dict[pd.DataFrame], *args, **kwargs):
    """
    Function to transform and load the files

    Args:
        data: A dictionary with all data from each file
    """
    output_path = 'data/output/'

    for name, df in data.items():
        parquet_file = f'{output_path}{name}.parquet'
        df.to_parquet(parquet_file, index=False)
        print(f"Saved {parquet_file}")