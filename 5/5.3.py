my_file = open(r"J:\prog\python\2\5\2.txt", 'r')
mid_sal = 0
l_count = 0
for lines in my_file:
    l_sal = int(lines.split()[1])
    if l_sal > 0:
        l_count +=1
        mid_sal += l_sal
        if l_sal <20000:
            print(lines)

my_file.close()
print("mid_sal ", mid_sal/l_count)

    
