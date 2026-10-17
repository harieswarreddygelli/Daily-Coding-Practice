# -- read() is used to read the content in a file
# Using the with keyword:
with open("demofile.txt") as f:
  print(f.read())


f = open("demofile.txt")
print(f.read())

# Open a file on a different location:

f = open("D:\\myfiles\welcome.txt")
print(f.read())
# or

# AN open need be closed using close()
f = open("demofile.txt")
print(f.readline())
f.close()
