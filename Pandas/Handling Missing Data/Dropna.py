import pandas as pd

# Sample data with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 20, 30, None]}
df = pd.DataFrame(data)

# Drop columns with missing values
df_drop_cols = df.dropna(axis=1)
print(df_drop_cols)

# Drop rows with missing values
df_drop_rows = df.dropna()
print(df_drop_rows)