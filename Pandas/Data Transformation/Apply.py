# df.apply(): Apply a Function to Rows or Columns
# # The apply() function is used to apply a function along either axis=0 (columns) or axis=1 (rows).

import pandas as pd

df = pd.DataFrame({
    'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
    'Math': [80, 90, 70, 85],
    'Science': [88, 76, 92, 84],
})

print(df)
print("\n","="*30,"\n")


# Default (axis=0): passes each column as a Series to the function
print(df[['Math', 'Science']].apply(max))
print("\n","="*30,"\n")

# axis=1: passes each row at a time to calculate total marks
df['Total'] = df[['Math', 'Science']].apply(lambda row: row['Math'] + row['Science'], axis=1)
print(df)
print("\n","="*30,"\n")
