
from pickle import APPEND


l = input("enter some nums ").split( )

l = sorted(l)
l.reverse()
print(l)

l.extend(input("items to append").split( ))
print(l)

l = sorted(l)
l.reverse()
print(l)

 