import pandas as pd

data = {
    'Department': ['Sales', 'Sales', 'Engineering', 'Engineering', 'HR', 'HR'],
    'Role': ['Junior', 'Senior', 'Junior', 'Senior', 'Junior', 'Senior'],
    'Salary': [40000, 75000, 60000, 110000, 38000, 65000],
    'Experience': [1, 5, 2, 7, 1, 4],
}

df = pd.DataFrame(data)

print(df)
print("\n","="*50,"\n")

# Raw counts of each Role
print(df['Role'].value_counts())
print("\n","="*30,"\n")

# Proportions (percentages when multiplied by 100)
print(df['Department'].value_counts(normalize=False))
print("\n","="*30,"\n")
