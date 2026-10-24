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

# Rank the students by their scores
# Rank scores from highest to lowest
df['Rank_Avg'] = df['Score'].rank(ascending=False, method='average')
df['Rank_Dense'] = df['Score'].rank(ascending=False, method='dense')
df['Rank_Min'] = df['Score'].rank(ascending=False, method='min')

print(df[['Name', 'Score', 'Rank_Avg', 'Rank_Dense', 'Rank_Min']])
