import math # Use import math to export math Modules

def ceil():
    N=float(input("Enter a Number: ")) #Take an input from the User in a Float 
    print(N,type(N)) # Print the Number and it's Type
    k=math.ceil(N) # Use math.ceil To Always rounds up to the next whole number 
    print(k,type(k)) # Print The changed Number and it's type
    
if __name__=="__main__":
    ceil()
