def Quicksort(a):
  if len(a) <= 1:
    return a
  p = a[-1]
  L = [x for x in a[:-1] if x <= p]
  R = [x for x in a[:-1] if x > p]

  L = Quicksort(L)
  R = Quicksort(R)

  return L + [p] + R

a = list(map(int, input("Enter Elements separated by Spaces: ").split()))
print("The elements after Quick Sort:", Quicksort(a))
