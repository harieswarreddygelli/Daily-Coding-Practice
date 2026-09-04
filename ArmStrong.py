def isAmstrong(a):
    temp1=a 
    k=0
    while temp1:
        k+=1
        temp1//=10
    temp=a
    s=0
    while temp:
        m=temp%10
        s+=m**k
        temp//=10
    return s==a

a=int(input("Enter a number: "))
print("It is a Armstrong number" if isAmstrong(a) else "It is not a Armstrong number")
