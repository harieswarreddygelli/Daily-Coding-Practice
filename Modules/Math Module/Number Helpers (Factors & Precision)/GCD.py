import math # Use import math to export math Modules

def Gcd():
    #Take First input from the User in a Integer
    N1=int(input("Enter a Number: ")) 
    #Take Second input from the User in a Integer
    N2=int(input("Enter a Number: ")) 
     # Use math.gcd To Find The Greatest Common Divisor of Two Numbers
    k=math.gcd(N1,N2)
    # Print The GCD
    print(k) 
    
# Run Gcd() only when this file is executed directly (not when imported)
if __name__=="__main__":
    Gcd()