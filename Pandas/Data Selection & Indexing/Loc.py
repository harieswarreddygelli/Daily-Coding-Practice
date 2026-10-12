import pandas as pd

Data ={
    'Name': ["Ram", "Bob", "Lucky", "Hari"],
    'Age': [25, 23, 22, 30]
}
df = pd.DataFrame(Data,index=['a','b','c','d'])

print(df.loc['c'])

print(df.loc[['a','d'],['Name']])