import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

DF = pd.DataFrame(Data)

print(DF.tail(2)) # It will print last 2 rows of the DataFrame