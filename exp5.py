import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
data = pd.read_csv('C:\AIML\database.csv')

# Display basic information
print("Dataset info:")
print(data.info())

print("\nSummary statistics:")
print(data.describe())

# Checking for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Visualizing missing values
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Visualizing correlations
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title("Correlation Heatmap")
plt.show()

# Distribution of numerical columns
data.hist(bins=50, figsize=(20,15))
plt.suptitle("Distribution of Numerical Features")
plt.show()

# Pairplot for exploring relationships
sns.pairplot(data)
plt.suptitle("Pairplot of Numerical Features", y=1.02)
plt.show()

# Exporting the dataset after EDA
data.to_csv('path_to_exported_dataset_after_eda.csv', index=False)
