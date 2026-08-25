def Adj(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

s = input("Enter a String: ")
print("The String After removing adjacent Characters:", Adj(s))
