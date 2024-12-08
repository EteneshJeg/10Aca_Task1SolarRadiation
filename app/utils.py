import pandas as pd

def load_data(filepath):
    """Load solar data from a CSV file."""
    return pd.read_csv(filepath)

def filter_by_ghi(data, threshold):
    """Filter the data based on GHI threshold."""
    return data[data['GHI'] > threshold]
