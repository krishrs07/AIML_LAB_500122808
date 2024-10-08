import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

# Import data
data = pd.read_csv('C:\Users\lenovo\OneDrive\Desktop')

# Handling Missing Values
# Using SimpleImputer to replace missing values with the median
imputer = SimpleImputer(strategy='median')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

print("Missing values after imputation:\n", data_imputed.isnull().sum())

# Handling Outliers
# Using the Interquartile Range (IQR) method
Q1 = data_imputed.quantile(0.25)
Q3 = data_imputed.quantile(0.75)
IQR = Q3 - Q1

# Defining the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Removing outliers
data_no_outliers = data_imputed[(data_imputed >= lower_bound) & (data_imputed <= upper_bound)]

# Checking if there are any outliers left
print("Number of outliers per column:\n", (data_imputed < lower_bound) | (data_imputed > upper_bound))

# Exporting the cleaned dataset
data_no_outliers.to_csv('path_to_cleaned_dataset.csv', index=False)
