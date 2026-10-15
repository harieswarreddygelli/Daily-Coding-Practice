# Syntax: with open("filename.txt", "r") as f:
with open("notes.txt", "r") as f:
  content = f.read()
  print(content)
  # or
f=open("notes.txt","r")
print(f)
