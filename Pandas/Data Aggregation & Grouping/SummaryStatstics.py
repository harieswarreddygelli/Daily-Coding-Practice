import pandas as pd
# Sample data
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

print(df)
print("\n","="*30,"\n")

# Calculate summary statistics
print(df.count())  # Count non-NA entries
print("\n","="*30,"\n")

print(df.sum())    # Sum of each column
print("\n","="*30,"\n")

print(df.mean())   # Mean of each column
print("\n","="*30,"\n")

print(df.min())    # Minimum value of each column
print("\n","="*30,"\n")

print(df.max())    # Maximum value of each column
print("\n","="*30,"\n")

print(df.median()) # Median of each column
print("\n","="*30,"\n")