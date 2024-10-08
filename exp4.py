import pandas as pd

# Import data
data = pd.read_csv('C:\AIML\database.csv')

# Show details of the dataset
print("Number of rows and columns: ", data.shape)
print("\nFirst five rows:\n", data.head())
print("\nSize of dataset: ", data.size)
print("\nNumber of missing values:\n", data.isnull().sum())

# Summarize numerical columns
print("\nSum of numerical columns:\n", data.sum(numeric_only=True))
print("\nAverage of numerical columns:\n", data.mean(numeric_only=True))
print("\nMinimum values in numerical columns:\n", data.min(numeric_only=True))
print("\nMaximum values in numerical columns:\n", data.max(numeric_only=True))

# Export data
data.to_csv('exported_dataset.csv', index=False)
