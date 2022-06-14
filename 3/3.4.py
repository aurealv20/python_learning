def otrpow(nu, po):
    nn =1
    if po>=0:
        print("GTFO")
        return

    for i in range(0,po, -1):
        nn*=nu
    return 1/nn

n = float(input("enter num "))
p = int(input("enter power"))

print(otrpow(n,p))
