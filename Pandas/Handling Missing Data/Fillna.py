# df.fillna(): Fill Missing Values with Specific Values
# Replace NaN with a specific value like 0, mean(), median(), etc

import pandas as pd

# Sample data with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 20, 30, None]}
df = pd.DataFrame(data)

print(df,"\n \n")

# Fill columns with missing values
df_Fill = df.fillna(0)
print(df_Fill)
