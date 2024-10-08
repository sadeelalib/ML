import pandas as pd
#Merging DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})
df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})
df_merged = pd.merge(df1, df2, on='key', how='inner').sum()
print(df_merged)
