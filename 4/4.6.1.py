from itertools import count


a =5
for b in count(a):
    if b>16:
        break
    else:
        print(b)
        