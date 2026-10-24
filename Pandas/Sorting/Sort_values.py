import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
        'Score': [85, 92, 85, 78],
        'Age': [21, 20, 23, 22],
    },
    index=[3, 1, 4, 2],
)

print(df)

print("\n","="*30,"\n")

# Sort by Score highest to lowest, then by Name alphabetically for ties
sorted_df = df.sort_values(by=['Score', 'Name'], ascending=[False, True])
print(sorted_df)
