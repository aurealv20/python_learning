from ntpath import join
import os
from random import randint

list1 = [randint(0,10) for i in range(0,10)]
folder_path = r"J:\prog\python\2\5"
my_file = open(os.path.join(folder_path, "5.txt"), 'w')
print(list1)
f_string = ''
for i in list1:
    f_string += (str(i)+' ')
print(f_string)
my_file.write(f_string +'\n')
my_file.close()

try:
    with open(os.path.join(folder_path, "5.txt")) as f_gen:
        r_string = f_gen.read()
        r_list = r_string.split(' ')
        sum = 0
        for i in r_list:
            try:
                sum+=int(i)
            except:
                pass
    print(sum)
except IOError:
    print("IO error")

