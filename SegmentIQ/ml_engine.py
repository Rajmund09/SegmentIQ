import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import json

def process_dataset(filepath):
    """
    Processes a CSV dataset for customer segmentation.
    Expects columns: CustomerID, Gender, Age, Annual Income, Spending Score.
    """
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        return {"error": str(e)}

    # Ensure required columns exist, handle slight variations in naming
    required_cols = ['Age', 'Annual Income', 'Spending Score']
    actual_cols = df.columns.tolist()
    
    # Try to map columns if they don't match exactly
    col_mapping = {}
    for req in required_cols:
        for actual in actual_cols:
            if req.lower() in actual.lower() or req.replace(' ', '') in actual.replace(' ', ''):
                col_mapping[actual] = req
                
    df = df.rename(columns=col_mapping)
    
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        return {"error": f"Missing required columns: {missing_cols}"}

    # Clean data
    df = df.dropna(subset=required_cols)
    X = df[required_cols]

    # Preprocess
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Find optimal K
    best_k = 3
    best_score = -1
    max_k = min(8, len(df))
    
    elbow_inertia = []
    
    for k in range(2, max_k):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        elbow_inertia.append(kmeans.inertia_)
        score = silhouette_score(X_scaled, kmeans.labels_)
        if score > best_score:
            best_score = score
            best_k = k

    # Ensure at least 3 clusters for rich insights if score is close
    if best_k < 3 and len(df) > 10:
        best_k = 3

    # Final Model
    kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Generate Cluster Profiles and Labels
    cluster_summary = df.groupby('Cluster')[required_cols].mean().reset_index()
    
    # Simple logic to label clusters
    labels = {}
    for index, row in cluster_summary.iterrows():
        income = row['Annual Income']
        spending = row['Spending Score']
        
        if income > 70 and spending > 70:
            labels[int(row['Cluster'])] = "Premium Customers"
        elif income > 70 and spending <= 40:
            labels[int(row['Cluster'])] = "High Income / Low Spenders"
        elif income <= 40 and spending > 70:
            labels[int(row['Cluster'])] = "High Spenders / Low Income"
        elif income > 40 and income <= 70 and spending > 40 and spending <= 70:
            labels[int(row['Cluster'])] = "Average Regulars"
        else:
            labels[int(row['Cluster'])] = "Budget Customers"
            
    df['Segment_Name'] = df['Cluster'].map(labels)

    # Generate Insights
    insights = [
        f"Algorithm identified {best_k} optimal customer segments with a silhouette score of {best_score:.2f}.",
    ]
    
    if "Premium Customers" in labels.values():
        prem_cluster = [k for k, v in labels.items() if v == "Premium Customers"][0]
        count = len(df[df['Cluster'] == prem_cluster])
        insights.append(f"Premium Customers make up {count} users. Target them with VIP programs.")
        
    if "High Income / Low Spenders" in labels.values():
        insights.append("You have High Income / Low Spenders. Implement campaigns to unlock their purchasing power.")

    # Convert data for frontend visualization
    # We'll return JSON strings so it can be easily passed to Chart.js/Plotly
    
    plot_data = {
        "scatter": {
            "x": df['Annual Income'].tolist(),
            "y": df['Spending Score'].tolist(),
            "cluster": df['Cluster'].tolist(),
            "hover_names": df['Segment_Name'].tolist()
        },
        "summary": cluster_summary.to_dict(orient="records"),
        "labels": labels,
        "insights": insights,
        "elbow": elbow_inertia
    }
    
    return {"success": True, "data": json.dumps(plot_data)}
