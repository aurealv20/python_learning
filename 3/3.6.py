def int_func(ss):
    s2 = []
    for i in str(ss).split():
        i = i.capitalize()
        s2.append(i)
        print(i)
    print(s2)
    return s2

s = input(">> ")
s1 = int_func(s)
print(type(s1))
s3 = " ".join(s1)
print(s3)

