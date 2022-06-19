my_file = open(r"J:\prog\python\2\5\2.txt", 'w')
str = input(">> ")
while str != "":
    my_file.write(str+'\n')
    str = input(">> ")
my_file.close()
