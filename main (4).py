'''python program to rearrange an array such that a[i]==i, a[i] != i return -1
using set method'''

def Array(A):
  s = set()
  for i in range(len(A)):
    s.add(A[i])
  for i in range(len(A)):
    if i in s:
      A[i]=i
    else:
      A[i]=-1
  return A

A = [3,4,2,1,5]

print('array after rearrangement:')
print(Array(A))
  