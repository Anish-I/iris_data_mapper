import pandas as pd

# Load the Iris dataset from the provided Excel file
iris_data = pd.read_excel("iris-data(1).xlsx")

# Calculate the correlation matrix
correlation_matrix = iris_data.corr()

# Print the correlation matrix
print(correlation_matrix)
