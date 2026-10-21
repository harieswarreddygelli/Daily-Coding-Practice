import pandas as pd

# Sample data with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 20, 30, None]}
df = pd.DataFrame(data)

print(df,"\n \n")

# estimating missing values along the index
df_Fill = df.interpolate()
print(df_Fill)
