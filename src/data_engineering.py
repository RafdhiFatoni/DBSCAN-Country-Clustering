import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def drop_columns(data, columns):
    """
    Drop specified columns from the DataFrame.

    Parameters:
        data (pd.DataFrame): The dataset from which to drop columns.
        columns (list): List of column names to drop.

    Returns:
        pd.DataFrame: DataFrame with specified columns dropped.
    """
    if data is not None and isinstance(columns, list):
        return data.drop(columns=columns)
    else:
        print("Invalid data or columns provided.")
        return data

def pairplot(data, hue=None):
    """
    Creates and displays a pair plot from the numerical columns of a DataFrame.

    Args:
        data (pd.DataFrame): The input DataFrame to visualize.
        hue (str, optional): A column name used to color the data points. Defaults to None.
    """
    if data is not None:
        data_numeric = data.select_dtypes(include=[np.number])
        sns.pairplot(data_numeric, hue=hue)
        plt.show()
    else:
        print("No data provided.")
        return None

def standardize_data(data):
    """
    Standardizes the input data using StandardScaler.

    This function scales the features of the DataFrame to have a 
    mean of 0 and a standard deviation of 1.

    Args:
        data (pd.DataFrame): The DataFrame with numerical data to standardize.

    Returns:
        pd.DataFrame: A new DataFrame with the standardized data.
    """
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(data)
    return pd.DataFrame(df_scaled, columns=data.columns)

def pca_transform(data, n_components=2):
    """
    Applies PCA to reduce the dimensionality of the dataset.

    Parameters:
        data (pd.DataFrame): The dataset to transform.
        n_components (int): Number of principal components to keep.

    Returns:
        pd.DataFrame: Transformed dataset with reduced dimensions.
    """
    pca = PCA(n_components=n_components)
    pc = pca.fit(data)
    transformed_data = pca.transform(data)
    pc_df = pd.DataFrame(
        data=transformed_data, 
        columns=[f'PC{i+1}' for i in range(n_components)],)
    return pc, pc_df

def loading_matrix(pca_object, feature_names):
    """
    Creates a loading matrix from a fitted PCA object.

    Args:
        pca_object (sklearn.decomposition.PCA): The fitted PCA model.
        feature_names (list): The list of original feature names from your data.

    Returns:
        pd.DataFrame: Loading matrix with features and their contributions.
    """

    loadings = pd.DataFrame(
        pca_object.components_.T, 
        columns=[f'PC{i+1}' for i in range(pca_object.n_components_)],
        index=feature_names
    )
    print("Loading matrix : ")
    print(loadings)
    return loadings

def visualisasi_pca(data, pca_data):
    """
    Visualizes the PCA results in a scatter plot.

    Parameters:
        data (pd.DataFrame): Original dataset.
        pca_data (pd.DataFrame): PCA transformed data.

    Returns:
        None: Displays a scatter plot of the PCA results.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(pca_data['PC1'], pca_data['PC2'], alpha=0.5)
    plt.title('PCA Result')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid()
    plt.show()






print("DBSCAN module loaded successfully.")