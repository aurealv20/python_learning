import json
import os

folder_path = r"J:\prog\python\2\5"
firm_profit_dict = {}
firm_count = 0
av_profit = 0
with open(os.path.join(folder_path, "7.txt")) as in_file:
    for lines in in_file:
        firm = lines.split()
        firm_prof = int(firm[2]) - int(firm[3])
        if firm_prof >=0:
            firm_count += 1
            av_profit += firm_prof
        firm_profit_dict.update({firm[0]: firm_prof})

print(firm_profit_dict)
print(av_profit/firm_count)

res_list = [firm_profit_dict, {"av_profit": av_profit/firm_count}]

with open(os.path.join(folder_path, "7_out.json"), "w") as out_f:
    json.dump(res_list, out_f)
