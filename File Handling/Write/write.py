with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())


  # 1. Open in WRITE mode to add text
f = open("notes.txt", "w")
f.write("Hello, this is a new line of text!\n")
f.close()  # Close it so the changes are saved

# 2. Open it again in READ mode to view the updated content
f = open("notes.txt", "r")
content = f.read()  # Now you can read it!
print(content)      # This will print: Hello, this is a new line of text!
f.close()
