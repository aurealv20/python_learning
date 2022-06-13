n = int(input("enter num "))
labels = {"name", "cost", "Qty"}
l = []
for i in range(1,n+1):
    
    dc = {}
    for j in labels:
        print(j)
        dc.update({j: input(" ")})
        
    templist = (i, dc)
    l.append(templist)

print(l)
for i in l:
    print(i)


