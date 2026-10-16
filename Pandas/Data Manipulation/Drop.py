import pandas as pd

Data = {
    'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
    'Age': [21, 20, 23, 24],
}

DF = pd.DataFrame(Data)

# Drops the row with index label 2 
print(DF.drop(2))
print("="*30,"\n")
# Drops the 'Age' column
print(DF.drop('Age', axis=1))