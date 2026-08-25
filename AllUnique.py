def AllUnique(s):
  return len(set(s))==len(s)
s =input("Enter a String: ")
if AllUnique(s):
    print("The String Has Unique Characters." )
else:
    print("The String Has Duplicate Characters." )
        
