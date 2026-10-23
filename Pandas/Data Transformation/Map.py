#  df['column'].map(): Apply a Function to a Series
# The map() function is used only on Pandas Series and applies a function to each element.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
    'Math': [80, 90, 70, 85],
    'Science': [88, 76, 92, 84],
})

print(df)
print("\n","="*30,"\n")


# Map names to grades/labels using a dictionary
grade_map = {'Abhi': 'A', 'Reddy': 'A+', 'Paul': 'B', 'Ram': 'A'}
df['Grade'] = df['Name'].map(grade_map)

# Or use a function on each individual value in a Series
df['Math_Bonus'] = df['Math'].map(lambda score: score + 5)

print(df[['Name', 'Grade', 'Math', 'Math_Bonus']])
