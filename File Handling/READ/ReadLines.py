# Read Lines

# Read one line of the file:

with open("demofile.txt") as f:
  print(f.readline())

# or

f=open("demofile.txt")
print(f.readline())
f.close()

# Read two lines of the file:

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

# or 

f=open("demofile.txt")
print(f.readline())
print(f.readline())
f.close()
# Loop through the file line by line:

with open("demofile.txt") as f:
  for x in f:
    print(x)

# or

f=open("demofile.txt")
for x in f:
  print(x)
f.close()
