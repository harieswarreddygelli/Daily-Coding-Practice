import pandas as pd

Data={
    'Name':["Ram","Sita","Lakshman","Hanuman"],
    'Age':[25,23,22,30],
    'Gender':["Male","Female","Male","Male"]
}

df=pd.DataFrame(Data)
print(df)