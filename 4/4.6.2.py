from itertools import cycle
from random import randint


my_list = [randint(0,100) for i in range(0,4)]

print(my_list)
tostop = 15
for b in cycle(my_list):
    print(b)
    tostop-=1
    if tostop<1:
        break
