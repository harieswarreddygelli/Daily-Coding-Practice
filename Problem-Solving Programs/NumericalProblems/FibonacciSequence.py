def fib(n):
  if n<0:
    return None
  elif n==1:
    return 0
  else:
    a,b=0,1
    for _ in range(n):
      print(a,end=" ")
      a,b=b,a+b
n=int(input("Enter a Number: "))
print("The Fibonacci Sequence upto",n,"is :")
fib(n)
