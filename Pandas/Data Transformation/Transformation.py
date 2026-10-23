#  df.transform(): Apply a Function to Transform Data
# The transform() function applies a function element-wise but maintains the original structure of the DataFrame.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
    'Math': [80, 90, 70, 85],
    'Science': [88, 76, 92, 84],
})

print(df)
print("\n","="*30,"\n")

# Add a column showing each student's difference from the class average in Math
df['Diff_From_Avg'] = df['Math'].transform(lambda x: x - x.mean())

print(df[['Name', 'Math', 'Diff_From_Avg']])
