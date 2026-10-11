import pandas as pd

Data ={
    'Name' :["Alice","Bob","Nathan"],
    'Age' :[25,30,35]
}

df = pd.DataFrame.from_records(Data)

print(df)