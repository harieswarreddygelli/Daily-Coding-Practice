def table(n):
    print("--- Multiplication Table for ",n," ---")
    for i in range(1, 11):
        result = n * i
        print(num,"x",i,"=",result)

n = int(input("Enter a number for its table: "))
table(n)
