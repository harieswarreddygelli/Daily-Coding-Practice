# 1. Using the 'with' statement 
with open("output.txt", "a") as f:
    f.write("Hello, Python!\n")


# 2. Using traditional open() and close()
# Open in append mode to add text
f = open("notes.txt", "a")
f.write("Hello, this is a new line of text!\n")
f.close()  # Close it so the changes are saved

# Open it again in READ mode to view the updated content
f = open("notes.txt", "r")
content = f.read()  # Now you can read it!
print(content)      # This will print the content!
f.close()
