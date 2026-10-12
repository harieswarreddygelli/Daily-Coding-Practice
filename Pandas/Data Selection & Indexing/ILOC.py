import pandas as pd

Data = {
    'Name' :["Alice","Bob","Nathan","Harry"],
    'Age' :[25,30,35,40]
}

df=pd.DataFrame(Data)

print(df.iloc[2])

print(df.iloc[[0,3], [0]])