import pandas as pd

Data = {
    'Name' :["Alice","Bob","Nathan","Henry"],
    'Age' :[25,30,35,40]
}
df = pd.DataFrame(Data)

print(df.at[3,'Name'])