def fctr(f):
    res = 1
    for i in range(1,f+1):
        res *= i
        yield res

for i in fctr(6):
    print(i)