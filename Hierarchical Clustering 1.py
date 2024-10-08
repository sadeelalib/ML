# Pehle zaroori libraries ko import karain
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Sample data points (2D mein)
data = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [8, 8],
    [3, 8],
    [6, 3]
])

# Linkage matrix banayein (Ward's method use kar rahein hain)
Z = linkage(data, method='ward')

# Dendrogram plot karna
plt.figure(figsize=(10, 7))
plt.title("Dendrogram")
dendrogram(Z)
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()
