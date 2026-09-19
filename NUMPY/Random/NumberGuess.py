import numpy as np
n=int(input("Enter in between how many numbers you want to guess:"))
def numguess():
    a=np.random.randint(1,n)
    attempts=0
    while True:
        b=int(input("Enter The Number : "))
        if a==b:
            attempts+=1
            print(f"Sucessful You found the number {a} in {attempts} attempts ")
            k=int(input("Do you want to play again \n1.Play\n2.Exit\n"))
            if k==1:
                numguess()
            break
            
        elif a>b:
            print("Enter a Large Number")
            attempts+=1
        elif a<b:
            print("Enter a Smaller Number") 
            attempts+=1
print("="*10,"Welcome to Number Guess Game","="*10)      
numguess()
print("="*10,"Thanks for playing","="*10)      
