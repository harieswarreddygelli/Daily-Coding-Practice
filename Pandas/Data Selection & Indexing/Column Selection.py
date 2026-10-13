import pandas as pd

Data =  {
    'Name' : ['Rafi','Abhi','Chilaka','Chintu'],
    'Age' : [21,20,23,24]
}

df= pd.DataFrame(Data)

print(df['Age'])

print(df['Name'])