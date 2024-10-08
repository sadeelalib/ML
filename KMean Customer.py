import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset from the Excel file
file_path = 'C:/Users/PMLS/Desktop/Presentation/Machine Learning/K Mean/OnlineRetail.xlsx'
df = pd.read_excel(file_path, sheet_name='Online Retail')

# Display the first few rows of the dataset to understand its structure
df.head()





from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Drop rows with missing CustomerID values
df_cleaned = df.dropna(subset=['CustomerID'])

# Grouping the data by CustomerID to aggregate purchasing behavior
customer_data = df_cleaned.groupby('CustomerID').agg({
    'Quantity': 'sum',  # Total quantity purchased
    'UnitPrice': 'mean',  # Average unit price per customer
}).reset_index()

# Creating a total spend column for the customer
customer_data['TotalSpend'] = customer_data['Quantity'] * customer_data['UnitPrice']
print(customer_data['TotalSpend'])
# Normalize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


customer_data_scaled = scaler.fit_transform(customer_data[['Quantity', 'UnitPrice', 'TotalSpend']])




'''
# Using the elbow method to find the optimal number of clusters
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(customer_data_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(K, inertia, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Assuming 4 clusters is optimal based on the elbow curve
kmeans = KMeans(n_clusters=4, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(customer_data_scaled)

# Visualizing the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Quantity', y='TotalSpend', hue='Cluster', data=customer_data, palette='viridis', s=100)
plt.title('Customer Segments based on Purchasing Behavior')
plt.show()
'''

