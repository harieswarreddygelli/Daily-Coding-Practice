import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'], 
    'Age' : [21,20,23,24]
}   

DF = pd.DataFrame(Data)

print(DF.head(2)) # It will print first 2 rows of the DataFrame