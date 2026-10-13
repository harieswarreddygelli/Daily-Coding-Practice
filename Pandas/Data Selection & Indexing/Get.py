import pandas as pd

Data ={
    'Name' : ['Abhi','Reddy','Paul','Ram'], 
    'Age' : [21,20,23,24]
}   

df = pd.DataFrame(Data)

print(df.get('Name')) # Work same as df.['Name']

print(df.get('Age',default=18))