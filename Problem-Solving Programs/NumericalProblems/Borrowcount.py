def Borrowcount(a, b):
    bc = 0
    borrow = 0
    while a > 0 or b > 0:
        digit_a = (a % 10) - borrow
        digit_b = b % 10
        
        if digit_a < digit_b:
            bc += 1
            borrow = 1      # Set borrow for the next column
            digit_a += 10   # Account for the borrow in this column (optional for count, but keeps logic sound)
        else:
            borrow = 0      # Reset borrow if no borrow needed for next column
            
        a //= 10
        b //= 10
    return bc

a = int(input("Enter a Number: "))
b = int(input("Enter b Number: "))
print("Total Borrows Required: ", Borrowcount(a, b))
