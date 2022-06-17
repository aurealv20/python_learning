from functools import reduce


def mltp(a, b):
    return a*b

s = (i for i in range(100,1001) if not(i%2))
print(reduce(mltp, [i for i in s]))