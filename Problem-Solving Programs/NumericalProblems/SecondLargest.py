def Secondlargest(arr):
  largest=float('-inf')
  secondlargest=float('-inf')
  for i in arr:
        if i > largest:
            secondlargest = largest  # Shift old largest down
            largest = i              # Update new largest
        elif i > secondlargest and i < largest:
            secondlargest = i
  return secondlargest
arr=list(map(int,input("Enter Numbers: ").split()))
print("The second Largest is:",Secondlargest(arr))
