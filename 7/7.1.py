from random import randint


class Matrix:
    def __init__(self, ls):
        self.mainlist = []
        for row in ls:
            self.mainlist.append(list(row))
    
        
    def __str__(self) -> str:
        outstr = ''
        for i in self.mainlist:
            for j in i:
                outstr += str(j)
                outstr +=' '
            outstr += '\n'
        return outstr
    
    def __add__(self, other):
        res = []
        for i in range(0, len(self.mainlist)):
            r1 = []
            res.append(r1)
            for j in range(len(self.mainlist[0])):
                r1.append(int(self.mainlist[i][j]) + int(other.mainlist[i][j]))
            res[i] = r1
        return Matrix(res)





def gen_list(len = 3):
    return [randint(0, 9) for i in range(len)]


l2 = [gen_list(3) for i in range(3)]
#print(l2)
l1 = [gen_list(3) for i in range(3)]

m1 = Matrix(l1)
m2 = Matrix(l2)

print(m1)
print(m2)
m3 = m1+m2
print(m3)

