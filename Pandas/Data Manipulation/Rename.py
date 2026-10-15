import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

DF = pd.DataFrame(Data)

print(DF.rename(columns={'Name':'Full Name','Age':'Years'})) # It will rename the column names of the DataFrame