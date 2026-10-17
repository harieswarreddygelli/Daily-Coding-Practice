import pandas as pd

data = {
    'Department': ['Sales', 'Sales', 'Engineering', 'Engineering', 'HR', 'HR'],
    'Role': ['Junior', 'Senior', 'Junior', 'Senior', 'Junior', 'Senior'],
    'Salary': [40000, 75000, 60000, 110000, 38000, 65000],
    'Experience': [1, 5, 2, 7, 1, 4],
}

df = pd.DataFrame(data)

print(df)
print("\n","="*30,"\n")

pt = df.pivot_table(
    values='Salary',
    index='Department',
    columns='Role',
    aggfunc='mean',
    fill_value=0,
)
print(pt)