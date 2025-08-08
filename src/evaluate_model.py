import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score, adjusted_rand_score, adjusted_mutual_info_score

def evaluate_clustering_unsupervised(df, cluster_col):
    """
    Mengevaluasi clustering hanya dengan metrik internal (tanpa label kebenaran).
    """
    features = df.drop(columns=[cluster_col]).select_dtypes(include=np.number)
    labels = df[cluster_col]
    
    unique_labels = set(labels)
    num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
    
    if num_clusters > 1 and num_clusters < len(df):
        silhouette_avg = silhouette_score(features, labels)
    else:
        silhouette_avg = None # Tidak bisa dihitung
        print(f"Silhouette score tidak bisa dihitung. Ditemukan {num_clusters} cluster.")

    return {
        'jumlah_cluster': num_clusters,
        'jumlah_noise': np.sum(labels == -1),
        'silhouette_score': silhouette_avg
    }

def save_model (model, filepath):
    """
    Save the trained model to a file.

    Parameters:
        model: The trained model to save.
        filepath (str): Path to save the model.
    """
    import joblib
    try:
        joblib.dump(model, filepath)
        print(f"Model saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving model: {e}")

print("Evaluate module loaded successfully.")