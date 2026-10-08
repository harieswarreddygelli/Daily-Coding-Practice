def Movehash(s):
  a=""
  for i in s:
    if i=='#':
      a+=i
  for i in s:
    if i!='#':
      a+=i
  return a
s=input("Enter a string: ")
b=Movehash(s)
print("After Moving Hash to end:",b)
