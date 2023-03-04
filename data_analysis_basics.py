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


#In this example, we first import the Pandas library using the import statement. We then read in a CSV file called data.csv using the pd.read_csv() 
#function and assign it to a variable called data. We then use the head() method to display the first 5 rows of data and the describe() method to display 
# summary statistics for the numerical columns in the dataset.

#Finally, we group the data by category using the groupby() method and calculate the average value of the numeric columns using the mean() method. 
#The resulting grouped data is then printed to the console.
