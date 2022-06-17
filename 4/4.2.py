from random import Random, randint, random


my_list = [randint(0,100) for i in range(0,20)]

print(my_list)
l2 = (i for i in my_list[1:])
#print(l2)
#out_list = []
#for i in range(1,len(my_list)):
#    if my_list[i] > my_list[i-1]:
#        out_list.append(my_list[i])
out_list = (my_list[i] for i in range(1,len(my_list)) if my_list[i]>my_list[i-1])

for k in out_list:
    print(k)

#print(out_list)
