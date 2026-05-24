import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Set global visual style
sns.set_theme(style="whitegrid", palette="viridis")

def analyze_store_customers():
    """Analyzes the store_customers.csv dataset (Demographics & Spending)"""
    print("--- Analyzing Store Customers Dataset ---")
    try:
        df = pd.read_csv('store_customers.csv')
    except FileNotFoundError:
        print("store_customers.csv not found.")
        return

    # Handle missing values by dropping them for simplicity in this case
    # Alternatively, we could impute them
    original_len = len(df)
    df = df.dropna(subset=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
    print(f"Dropped {original_len - len(df)} rows with missing values.")

    # Select features for clustering
    features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    X = df[features]

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using Silhouette Score
    best_k = 2
    best_score = -1
    for k in range(2, 8):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        score = silhouette_score(X_scaled, kmeans.labels_)
        if score > best_score:
            best_score = score
            best_k = k
    
    print(f"Optimal number of clusters for Store Customers: {best_k} (Silhouette Score: {best_score:.3f})")

    # Fit final model
    kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Visualizations
    
    # 1. 3D Scatter Plot (using 2D plots for better readability in reports)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='Set1', s=100, alpha=0.8)
    plt.title('Store Customers: Annual Income vs Spending Score by Segment')
    plt.tight_layout()
    plt.savefig('results/store_customers_clusters.png', dpi=300)
    plt.close()

    # 2. Boxplots to understand cluster characteristics
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for i, feature in enumerate(features):
        sns.boxplot(data=df, x='Cluster', y=feature, ax=axes[i], palette='Set1')
        axes[i].set_title(f'Distribution of {feature} by Segment')
    plt.tight_layout()
    plt.savefig('results/store_customers_characteristics.png', dpi=300)
    plt.close()
    
    # Save clustered data
    df.to_csv('results/store_customers_clustered.csv', index=False)
    print("Store Customers analysis complete. Visualizations saved to 'results/'\n")
    
    return df.groupby('Cluster')[features].mean()

def analyze_behavioral_data():
    """Analyzes the sample_customer_data.csv dataset (Detailed Behavioral Metrics)"""
    print("--- Analyzing Detailed Behavioral Data ---")
    try:
        df = pd.read_csv('sample_customer_data.csv')
    except FileNotFoundError:
        print("sample_customer_data.csv not found.")
        return

    df = df.dropna()

    # Features: We use a mix of monetary, frequency and satisfaction metrics
    features = ['Purchase_Frequency', 'Customer_Lifetime_Value', 'Return_Rate', 'Customer_Satisfaction_Score']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters
    best_k = 2
    best_score = -1
    for k in range(2, 6): # Dataset is small, so we check fewer clusters
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        score = silhouette_score(X_scaled, kmeans.labels_)
        if score > best_score:
            best_score = score
            best_k = k

    print(f"Optimal number of clusters for Behavioral Data: {best_k} (Silhouette Score: {best_score:.3f})")

    kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    # 1. Scatter Plot (LTV vs Satisfaction)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Customer_Lifetime_Value', y='Customer_Satisfaction_Score', hue='Cluster', palette='Set2', s=150, alpha=0.9)
    plt.title('Behavioral: Customer Lifetime Value vs Satisfaction Score')
    plt.tight_layout()
    plt.savefig('results/behavioral_clusters.png', dpi=300)
    plt.close()

    # 2. Pairplot of key features to see all relationships
    pairplot_features = features + ['Cluster']
    sns.pairplot(df[pairplot_features], hue='Cluster', palette='Set2', corner=True)
    plt.savefig('results/behavioral_pairplot.png', dpi=300)
    plt.close()

    # Save clustered data
    df.to_csv('results/behavioral_data_clustered.csv', index=False)
    print("Behavioral data analysis complete. Visualizations saved to 'results/'\n")
    
    return df.groupby('Cluster')[features].mean()

if __name__ == "__main__":
    print("Starting Customer Segmentation Analysis...\n")
    
    store_summary = analyze_store_customers()
    if store_summary is not None:
        print("Store Customers Cluster Profiles (Mean Values):")
        print(store_summary)
        print("-" * 50)
        
    behavioral_summary = analyze_behavioral_data()
    if behavioral_summary is not None:
        print("Behavioral Data Cluster Profiles (Mean Values):")
        print(behavioral_summary)
        print("-" * 50)
        
    print("\nAll tasks completed successfully. Check the 'results' directory for outputs.")
