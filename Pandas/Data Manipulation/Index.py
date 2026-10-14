import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'],
    'Age' : [21,20,23,24]
}

DF = pd.DataFrame(Data)

print(DF.index) # It will print the index of the DataFrame