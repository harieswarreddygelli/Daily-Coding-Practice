import pandas as pd
Data={
     'Name':["Ram","Sita","Lakshman","Hanuman"],
     'Age':[25,23,22,30]
 }

df=pd.DataFrame.from_dict(Data)
print(df) 