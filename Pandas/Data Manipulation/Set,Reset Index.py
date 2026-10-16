import pandas as pd

Data = {
    'Name': ['Abhi', 'Reddy', 'Paul', 'Ram'],
    'Age': [21, 20, 23, 24],
}

df = pd.DataFrame(Data)

df_indexed = df.set_index('Name') # It will set the 'Name' column as the index of the DataFrame
print(df_indexed) 

# Resetting index on the DataFrame that actually had 'Name' set as index
print(df_indexed.reset_index())