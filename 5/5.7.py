import os
from random import randint


folder_path = r"J:\prog\python\2\5"
my_file = open(os.path.join(folder_path, "7.txt"), 'w')

def gen_firm(n):
    res_list = [f"firm_{n}"]
    res_list.append("OOO")
    res_list.append(str(randint(10000, 100000)))
    res_list.append(str(randint(10000, 100000)))
    print(res_list)
    return res_list

for i in range(10):
    l1 = gen_firm(i)

    out_string = ' '.join(l1)
    print(out_string)
    print(type(out_string))
    my_file.write(out_string + '\n')

my_file.close()



