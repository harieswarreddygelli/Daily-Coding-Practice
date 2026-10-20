# df.isna() / df.isnull(): Check for Missing Values
# Both isna() and isnull() do the same thing—they return a DataFrame of True where 
# values are missing and False where they are present.

import pandas as pd

# Sample data with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 20, 30, None]}
df = pd.DataFrame(data)

# Check for missing values
print(df.isna())  # Same as df.isnull()