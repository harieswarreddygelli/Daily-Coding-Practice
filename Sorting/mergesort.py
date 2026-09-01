def mergesort(a):
  if len(a) <= 1:
    return a
  m = len(a) // 2
  l, r = a[:m], a[m:]

  l = mergesort(l)
  r = mergesort(r)
  L, R = 0, 0
  llen = len(l)
  rlen = len(r)
  sortarr = [0] * len(a)
  i = 0
  while L < llen and R < rlen:
    if l[L] < r[R]:
      sortarr[i] = l[L]
      L += 1
    else:
      sortarr[i] = r[R]
      R += 1
    i += 1
  while L < llen:
    sortarr[i] = l[L]
    L += 1
    i += 1
  while R < rlen:
    sortarr[i] = r[R]
    R += 1
    i += 1
  return sortarr

a = list(map(int, input("Enter Elements separated by spaces: ").split()))
print("The Elements after mergesort", mergesort(a))
