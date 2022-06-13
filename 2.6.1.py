l =[(1, {'name': 'aaa', 'cost': '11', 'Qty': '1'}),
(2, {'name': 'bbb', 'cost': '22', 'Qty': '2'}),
(3, {'name': 'ccc', 'cost': '33', 'Qty': '3'})]

print(l)
print(l[0])
print(l[0][1])
dc = dict(l[0][1])

for j in dc.keys():
    #print(j)
    l2 = []
    for i in l:
        #dc2 = dict(i[1])
        l2.append(dict(i[1]).get(j))
    print(j, l2)
        

    
#print(dc.keys())