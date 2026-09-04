def isomorphic(s, t):
    if len(s) != len(t):
        return False
    return len(dict(zip(s, t))) == len(set(s)) == len(set(t))
    
a=input("Enter a String: ")
b=input("Enter b String: ")
if isomorphic(a,b):
    print("Given String are isomorphic.")
else:
    print("Given String are not isomorphic.")
