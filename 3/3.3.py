def my_func(a,b,c):
    m = [a,b,c]
    m.sort()
    return m[1] + m[2]

x = (input("enter 3 numbers").split())

print(x)

print(type(x))
print(type(x[0]))
x =list(map(int, x))

print(x)
print(type(x))
print(type(x[0]))
print(my_func(x[0], x[1], x[2]))
