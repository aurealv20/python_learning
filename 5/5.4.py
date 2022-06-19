from fileinput import close
import os

my_dict = {1: "один", 2:"два", 3 : "три", 4: "четыре"}

folder_path = r"J:\prog\python\2\5"
my_file = open(os.path.join(folder_path, "4.txt"), 'r')
out_file = open(os.path.join(folder_path, "4_out.txt"), 'w')

for lines in my_file:
    print(lines[:-1])
    print(lines.split('-')[1][:-1])
    print(my_dict.get(int(lines.split(' - ')[1][:-1])),"-", lines.split(' - ')[1][:-1])
    out_file.write(my_dict.get(int(lines.split(' - ')[1][:-1]))+" - "+ lines.split(' - ')[1][:-1]+ '\n')
my_file.close()
out_file.close()
