from ctypes import sizeof
from operator import index



a = [1,2,3,5,22,1488,42]
for i in a:
    print(type(i))
    
l = len(a)
print(type(l))
print(len(a))

for i in range(1,l,2):
    b = a[i]
    a[i] = a[i-1]
    a[i-1] = b

print(a)
