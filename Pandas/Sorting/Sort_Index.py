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


print("\nDataFrame sorted by index:")
print(df.sort_index())