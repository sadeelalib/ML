import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Define the data
data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [150, 200, 300, 250, 100, 150]
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Process the data
# Create a pivot table to show the structure
pivot_df = df.pivot(index='Region', columns='Product', values='Sales')
print(pivot_df)

# Step 4: Plot the bar chart
sns.set_theme(style="whitegrid")
sns.barplot(x='Product', y='Sales', hue='Region', data=df)
# Add titles and labels
plt.title('Sales by Product and Region')
plt.xlabel('Product')
plt.ylabel('Sales')

# Show the plot
plt.show()


