# Read Only Parts of the File

with open("demofile.txt") as f:
  print(f.read(5))

# or

f = open("demofile.txt")
print(f.read(5))
f.close()
