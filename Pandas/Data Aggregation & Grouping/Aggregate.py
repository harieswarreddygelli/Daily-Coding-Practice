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
# Multiple aggregations on a single column
print(df['Salary'].agg(['min', 'max', 'mean', 'median']))
print("\n","="*30,"\n")

# Groupby + custom named aggregations
summary = df.groupby('Department').agg(
    avg_salary=('Salary', 'mean'),
    max_salary=("Salary",'max'),
    max_exp=('Experience', 'max'),
    min_exp=('Experience','min'),
    headcount=('Role', 'count'),
)
print(summary)