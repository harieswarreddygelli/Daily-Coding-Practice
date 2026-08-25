def Occurance(s, v):
    c = 0
    for i in s:
        if i == v:
            c += 1
    return c if c>0 else -1
s =input("Enter a String: ")
f=input("Enter the Chacretcer count you want: ")
print(Occurance(s,f))
