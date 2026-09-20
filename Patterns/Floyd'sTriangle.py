n=int(input("Enter a number:"))
num=1
for i in range(1, n):  
    for j in range(i):  
        print(num, end=" ")
        num += 1
    print()
