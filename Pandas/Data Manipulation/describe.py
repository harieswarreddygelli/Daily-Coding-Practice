import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

df = pd.DataFrame(Data)

print(df.describe()) # It will print the statistical summary of the DataFrame