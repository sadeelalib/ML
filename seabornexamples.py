import pandas as pd
'''
# Step 1: Read data from a CSV file
df = pd.read_csv('people.csv')
print("DataFrame read from CSV:")
print(df)

# Step 2: Perform some data manipulation
df['Cumulative Sales'] = df['Sales'].cumsum()
print("\nDataFrame after manipulation:")
print(df)

# Step 3: Write the manipulated data to an Excel file
df.to_excel('output.xlsx', sheet_name='SalesData', index=False)
print("\nData written to 'output.xlsx'.")
'''
#print(df.isnull())


#import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Frank'],
    'age': [24, 27, 22, 32, 29, 24],
    'city': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'score': [85, 87, 78, 92, 85, 90]
}

df = pd.DataFrame(data)

# Group by city and calculate mean score
grouped = df.groupby('city')['score'].mean()
print(grouped)
