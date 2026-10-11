import pandas as pd

Name = ["Alice","Bob","Billa","Charlie"]
Age = [25,30,35,40]
df=pd.Series(Age,index=Name)

print(df)