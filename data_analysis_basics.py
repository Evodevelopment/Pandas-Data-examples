import pandas as pd

# Read in CSV file
data = pd.read_csv('data.csv')

# Display first 5 rows of data
print(data.head())

# Display summary statistics for numerical columns
print(data.describe())

# Group data by category and calculate average value of numeric columns
grouped_data = data.groupby('category').mean()
print(grouped_data)
