import numpy as np
a=np.random.randint(1000,10000)
print(f"The Generated otp: {a}")
b=int(input("Enter otp: "))
if a==b:
    print("OTP Sucessful")
else:
    print("Invalid")
