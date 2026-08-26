def rotateString(s,goal):
    if len(s) != len(goal):
        return False
    return goal in s + s
a=input("Enter the  String: ")
t=input("Enter String you want to see is rotation: ")
print("The string is rotation of other" if rotateString(a,t) else "The string is not rotatopn of other")
