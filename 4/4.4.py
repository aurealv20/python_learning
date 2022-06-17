
from random import randint



my_list = [randint(0,10) for i in range(0,15)]
print(my_list)
s = (i for i in my_list if my_list.count(i) == 1)
#s = s.append(i for i in my_list)
l = []
#for i in s:
#    l.append(i)
l.extend(i for i in s)
print(l)
        
    

