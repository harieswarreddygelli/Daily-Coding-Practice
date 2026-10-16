# use Exclusive (x) when you want to protect an existing file from accidentally being overwritten or modified.
# if Run again it shows errors

# 1. Using the 'with' statement (Recommended for safety and cleanliness)
with open("output.txt", "x") as f:
    f.write("Hello, Python!\n")


# 2. Using traditional open() and close()
# Open in append mode to add text
f = open("notes.txt", "x")
f.write("Hello, this is a new line of text!\n")
f.close()  # Close it so the changes are saved

# Open it again in READ mode to view the updated content
f = open("notes.txt", "r")
content = f.read()  # Now you can read it!
print(content)      # This will print the content!
f.close()
