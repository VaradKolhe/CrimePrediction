import pandas as pd
import numpy as np
import hdbscan
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Load the predicted crime data
print("Loading predicted crime data...")
df = pd.read_csv('predicted_crime_data.csv')

# Prepare coordinates for clustering
coordinates = df[['latitude', 'longitude']].values

# Scale the coordinates
scaler = StandardScaler()
scaled_coords = scaler.fit_transform(coordinates)

# Function to perform clustering with point limit
def cluster_with_limit(coords, max_points_per_cluster=180):
    # First perform HDBSCAN clustering with adjusted parameters
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=8,           
        min_samples=2,                
        metric='euclidean',
        cluster_selection_method='leaf',
        cluster_selection_epsilon=0.01,  
        alpha=0.2,                    
        allow_single_cluster=False
    )
    
    # Get initial clusters
    labels = clusterer.fit_predict(coords)
    
    # Process each cluster
    final_labels = np.copy(labels)
    current_max_label = np.max(labels) + 1
    
    for cluster_id in np.unique(labels):
        if cluster_id == -1:  # Skip noise
            continue
            
        # Get indices of points in this cluster
        cluster_indices = np.where(labels == cluster_id)[0]
        cluster_points = coords[cluster_indices]
        
        # If cluster is too large, split it
        if len(cluster_points) > max_points_per_cluster:
            # Use DBSCAN to split the large cluster with adjusted parameters
            dbscan = DBSCAN(
                eps=0.05,             
                min_samples=3         
            )
            sub_labels = dbscan.fit_predict(cluster_points)
            
            # Update labels for the split cluster
            for sub_label in np.unique(sub_labels):
                if sub_label == -1:  # Skip noise
                    continue
                # Get indices of points in this sub-cluster
                sub_cluster_indices = cluster_indices[sub_labels == sub_label]
                final_labels[sub_cluster_indices] = current_max_label
                current_max_label += 1
            
            # Mark remaining points as noise
            remaining_indices = cluster_indices[sub_labels == -1]
            final_labels[remaining_indices] = -1
    
    return final_labels

# Perform clustering with point limit
print("Performing clustering with point limit...")
cluster_labels = cluster_with_limit(scaled_coords, max_points_per_cluster=180)

# Add cluster labels to the DataFrame
df['cluster'] = cluster_labels

# Count the number of clusters and noise points
n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
n_noise = list(cluster_labels).count(-1)

print(f"\nClustering Results:")
print(f"Number of clusters found: {n_clusters}")
print(f"Number of noise points: {n_noise}")
print(f"Number of points per cluster:")
print(df['cluster'].value_counts().sort_index())

# Create a list to store cluster information
cluster_data = []

# Process each cluster
for cluster_id in sorted(df['cluster'].unique()):
    if cluster_id != -1:
        cluster_points = df[df['cluster'] == cluster_id]
        
        # Calculate risk level percentages for this cluster
        total_points = len(cluster_points)
        high_risk_points = len(cluster_points[cluster_points['risk_level'] == 'High'])
        medium_risk_points = len(cluster_points[cluster_points['risk_level'] == 'Medium'])
        
        high_risk_percentage = (high_risk_points / total_points) * 100
        medium_risk_percentage = (medium_risk_points / total_points) * 100
        
        # Determine cluster's risk level based on percentages
        if high_risk_percentage >= 23:
            cluster_risk_level = 'High'
        elif medium_risk_percentage >= 25:
            cluster_risk_level = 'Medium'
        else:
            cluster_risk_level = 'Low'
        
        # Get the most common city and area in the cluster
        most_common_city = cluster_points['city'].mode().iloc[0]
        most_common_area = cluster_points['area'].mode().iloc[0]
        
        # Get the most common crime description in the cluster
        most_common_crime = cluster_points['crime_description'].mode().iloc[0]
        
        # Compute cluster centroid
        centroid_lat = cluster_points['latitude'].mean()
        centroid_long = cluster_points['longitude'].mean()

        # Append the cluster summary
        cluster_data.append({
            'cluster': cluster_id,
            'city': most_common_city,
            'area': most_common_area,
            'latitude': centroid_lat,
            'longitude': centroid_long,
            'risk_level': cluster_risk_level,
            'total_points': total_points,
            'crime_description': most_common_crime  # Add most common crime description
        })

# Create DataFrame from cluster data
result_df = pd.DataFrame(cluster_data)

# Save the results
print("\nSaving clustered data to clustered_crime_data.csv...")
result_df.to_csv('clustered_crime_data.csv', index=False)

print("\nClustering complete. Results saved to clustered_crime_data.csv")

# Print summary of the clustered data
print("\nCluster Summary:")
print(f"Number of clusters: {len(result_df)}")
print("\nRisk Level Distribution:")
print(result_df['risk_level'].value_counts())
print("\nSample of clustered data:")
print(result_df.head()) 