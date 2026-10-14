import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

df = pd.DataFrame(Data)

print(df.dtypes) # It will print the data types of each column in the DataFrame