# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import MultiLabelBinarizer

# Step 1: Sample dataset of transactions (market basket)
transactions = [
    ['bread', 'milk', 'butter'],
    ['bread', 'butter'],
    ['milk', 'butter', 'cheese'],
    ['bread', 'cheese'],
    ['milk', 'cheese'],
    ['bread', 'milk', 'butter', 'cheese'],
    ['butter', 'cheese']
]

# Step 2: Convert transactions to a binary format (one-hot encoding)
mlb = MultiLabelBinarizer()
binary_matrix = mlb.fit_transform(transactions)
item_labels = mlb.classes_

# Convert binary matrix into a DataFrame for better visualization
df = pd.DataFrame(binary_matrix, columns=item_labels)
print("Binary Representation of Transactions:")
print(df)
