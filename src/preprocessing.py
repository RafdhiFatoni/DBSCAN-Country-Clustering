import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def show_shape(data):
    """
    Display the shape of the given DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset to check.

    Returns:
        tuple: Shape of the DataFrame (rows, columns).
    """
    if data is not None:
        return data.shape
    else:
        print("No data provided.")
        return None

def preview(data):
    """
    Display the first few rows of the DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset to preview.

    Returns:
        pd.DataFrame: The first few rows of the DataFrame.
    """
    if data is not None:
        return data.head()
    else:
        print("No data provided.")
        return None

def info(data):
    """
    Display a summary of the DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset to summarize.

    Returns:
        pd.DataFrame: Summary statistics of the DataFrame.
    """
    if data is not None:
        return data.info()
    else:
        print("No data provided.")
        return None

def summary(data):
    """
    Display a summary of the DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset to summarize.

    Returns:
        pd.DataFrame: Summary statistics of the DataFrame.
    """
    if data is not None:
        return data.describe()
    else:
        print("No data provided.")
        return None

def check_missing(data):
    """
    Check for missing values in the DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset to check.

    Returns:
        pd.Series: Series indicating the number of missing values per column.
    """
    if data is not None:
        return data.isnull().sum()
    else:
        print("No data provided.")
        return None

def check_duplicates(data):
    duplicated_rows = data.duplicated().sum()
    print(f"Number of duplicated rows: {duplicated_rows}")


print("Data processing module loaded successfully.")