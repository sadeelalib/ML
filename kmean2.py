import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample data: Quantity and UnitPrice
data = {
    'Customer': ['A', 'B', 'C', 'D', 'E'],
    'Quantity': [5, 8, 10, 15, 20],
    'UnitPrice': [2, 2.5, 3, 3.5, 4]
}

df = pd.DataFrame(data)

# Step 1: Prepare the features
X = df[['Quantity', 'UnitPrice']]

# Step 2: Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=2, random_state=0)  # K=2 clusters
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Display the results
print(df)
