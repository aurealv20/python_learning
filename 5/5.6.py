from ntpath import join
import os

out_dict = {}

folder_path = r"J:\prog\python\2\5"
#my_file = open(os.path.join(folder_path, "6.txt"), 'w')

with open(os.path.join(folder_path, "6.txt")) as in_file:
    for lines in in_file:
        pred_list = lines.split()
        
        hrs_count = 0
        print(pred_list)
        for i in pred_list[1:]:
            hrs_count+=int(i.split('(')[0])

        out_dict.update({pred_list[0]: hrs_count})

for i in out_dict:
    print(i, ':', out_dict.get(i))
        

