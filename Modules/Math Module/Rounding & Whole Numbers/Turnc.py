import math # Use import math to export math Modules

def Turnc():
    N=float(input("Enter a Number: ")) #Take an input from the User in a Float 
    print(N,type(N)) # Print the Number and it's Type
    k=math.trunc(N) # Use math.trunc To Remove the Decimal Part
    print(k,type(k)) # Print The changed Number and it's type
    
if __name__=="__main__":
    Turnc()
