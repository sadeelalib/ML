import pandas as pd

# Load dataset
df = pd.read_csv('test2.csv')
'''
# Inspect the first few rows of the dataset
#print(df.head())

# Get a summary of the dataset
#print(df.info())

# Check for missing values
print(df.isnull().sum())


# Remove rows with missing values
#df_cleaned = df.dropna()

#print(df_cleaned.isnull().sum())
#print(df_cleaned['type'])


#Fill missing values with a specific value (e.g., 'Unknown')
df['type'].fillna('Unknown', inplace=True)

print(df)


# Fill missing numerical values with the median
#df['duration'] = df['duration'].fillna(df['duration'].median())

df['duration'] = df['duration'].str.replace(' min', '').astype(float)

# Step 2: Calculate the mean
duration = df['duration'].mean()

print(f"The mean duration is: {duration} minutes")
df['duration'] = df['duration'].fillna(df['duration'].mean())
print(df)

'''
# Check for duplicates
print(df.duplicated().sum())



# Remove duplicate rows
df_cleaned = df.drop_duplicates()
print(df_cleaned)


'''
# Remove duplicate rows
df_cleaned = df.drop_duplicates()
print(df_cleaned)


# Convert text to lowercase
df['title'] = df['title'].str.upper()
print(df['title'])

df['title'] = df['title'].str.upper()
print(df['title'])

# Standardize date format
df['date_added'] = pd.to_datetime(df['date_added'])
print(df['date_added'])

# Standardize categorical data
df['rating'] = df['rating'].str.upper()
print(df['rating'])

# Fix typos in categorical data
df['country'] = df['country'].replace({'Brazil': 'USA', 'United States': 'USA'})
print(df['country'])
'''
