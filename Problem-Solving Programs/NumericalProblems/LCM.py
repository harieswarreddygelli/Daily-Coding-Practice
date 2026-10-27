def compute_lcm_loop(x, y):
    # Choose the greater number
    greater = max(x, y)
    
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
        
    return lcm


a=int(input("Enter first number: "))
b=int(input("Enter Second Number: "))

print(f"The LCM of two numbers is {compute_lcm_loop(a,b)}")
