# Syntax:
# with open("filename.txt", "w") as f: 
#   or 
# with open("filename.txt", "wt") as f:

with open("output.txt", "w") as f:
    f.write("Hello, Python!")
  # or
# 1. Open in WRITE mode to add text
f = open("notes.txt", "w")
f.write("Hello, this is a new line of text!\n")
f.close()  # Close it so the changes are saved

# 2. Open it again in READ mode to view the updated content
f = open("notes.txt", "r")
content = f.read()  # Now you can read it!
print(content)      # This will print: Hello, this is a new line of text!
f.close()
