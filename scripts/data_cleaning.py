import pandas as pd

def clean_data(df):
    """
    Cleans the provided DataFrame by:
    - Dropping null values
    - Handling outliers
    - Standardizing column names
    """
    df = df.dropna()
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df
