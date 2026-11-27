import math # Use import math to export math Modules
def LCM():
    #Take First input from the User in a Integer
    N1=int(input("Enter a Number: ")) 
    #Take Second input from the User in a Integer
    N2=int(input("Enter a Number: ")) 
    # Use math.lcm To Find The Least Common Multiple of Two Numbers
    k=math.lcm(N1,N2)
    # Print The LCM
    print(k)

# Run LCM() only when this file is executed directly (not when imported)
if __name__ == "__main__":
    LCM()