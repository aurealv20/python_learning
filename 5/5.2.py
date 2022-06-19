my_file = open(r"J:\prog\python\2\5\1.txt", 'r')
strcount = 0
words = 0
strs = {}
for lines in my_file:
    print(lines[:-1])
    strcount+=1
    strs.update({f"{strcount}" : len(lines.split())})
    #добавляет в словарь пару номер строки: число слов

print(strcount)
print(strs)
    
my_file.close()