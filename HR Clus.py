import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Define data points
data = np.array([[1, 2],
                 [2, 3],
                 [6, 5],
                 [7, 8]])

# Perform Agglomerative Clustering
linked = linkage(data, method='average')

# Create Dendrogram
plt.figure(figsize=(10, 5))

# Labels correspond to each data point
dendrogram(linked,
           orientation='top',
           labels=['A', 'B', 'C', 'D'],  # Custom labels for x-axis
           distance_sort='descending',
           show_leaf_counts=False)  # Remove the leaf counts if not needed

# Set the title and axis labels
plt.title('Dendrogram for Agglomerative Clustering')
plt.xlabel('Clusters')  # X-axis label showing "Clusters"
plt.ylabel('Distance')

# Show plot
plt.show()
