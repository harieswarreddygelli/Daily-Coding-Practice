# df.notna() / df.notnull(): Check for Non-Missing Values
# These return a DataFrame of True for non-missing values and False for missing ones.

import pandas as pd

# Sample data with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 20, 30, None]}
df = pd.DataFrame(data)

# Check for missing values

print(df.notna())  # Same as df.notnull()