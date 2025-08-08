import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, adjusted_rand_score, adjusted_mutual_info_score
from sklearn.neighbors import NearestNeighbors
import plotly.express as px
import plotly.graph_objects as go

def optimal_cluster(df, k=3):
    neigh = NearestNeighbors(n_neighbors=k)
    neigh.fit(df)
    distances, indices = neigh.kneighbors(df)

    distances = np.sort(distances[:, k-1], axis=0)

    plt.figure(figsize=(10, 6))
    plt.plot(distances, marker='o')
    plt.title('K-distance Graph')
    plt.xlabel('Points sorted by distance')
    plt.ylabel('K-distance')
    plt.grid()
    plt.show()

def dbscan_clustering(df, eps=0.5, min_samples=3):
    """
    Perform DBSCAN clustering on the given DataFrame.

    Parameters:
        df (pd.DataFrame): The dataset to cluster.
        eps (float): The maximum distance between two samples for one to be considered as in the neighborhood of the other.
        min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.

    Returns:
        pd.DataFrame: DataFrame with cluster labels.
    """
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    df['cluster'] = dbscan.fit_predict(df)

    # Visualize clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], hue='cluster', palette='viridis', alpha=0.7)
    plt.title('DBSCAN Clustering')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    return df