import pandas as pd  # Import the pandas library for data manipulation

# Define a dictionary with sample data containing missing values (None)
Data = {
    'A': [1, 2, None, 4],       # Column 'A' with missing value at index 2
    'B': [None, 20, 30, None]   # Column 'B' with missing values at index 0 and 3, and 20 at index 1
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(Data)

# Replace None (treated as NaN in pandas) with 0 and replace 20 with 21 across the DataFrame
# Note: replace() returns a new DataFrame by default without modifying 'df' in place
updated_df = df.replace({None: 0, 20: 21})

# Print the resulting DataFrame to the console/output
print(updated_df)