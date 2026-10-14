import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

df = pd.DataFrame(Data)

print(df.info()) # It will print the concise summary of the DataFrame