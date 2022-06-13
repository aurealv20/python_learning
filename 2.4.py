mystring  = input("enter string ")
l = mystring.split( )
n = 1
for i in l:
    print(n, i[:10])
    n+=1