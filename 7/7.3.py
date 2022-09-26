from audioop import mul


class cell:
    def __init__(self,param) -> None:
        if param <=0:
            print("cell class  can't be init with no subcells")
        self.subcell = int(param)
    def __add__(self, other):
        if type(other) is cell:
            res = self.subcell + other.subcell
            return cell(res)
        else:
            print("wrong argument")
        
    def __sub__(self, other):
        if type(other) is cell:
            res = self.subcell - other.subcell
            if res > 0:
                return cell(res)
            else:
                print("result cell can not be created. sub, subcell <=0")
        else:
             print("wrong argument")

    def __mul__(self, other):
        if type(other) is cell:
            res = self.subcell * other.subcell
            return cell(res)
        else:
            print("wrong argument")
    
    def __truediv__(self, other):
        if type(other) is cell:
            res = self.subcell / other.subcell
            if res > 0:
                del other
                del self
                return cell(res)
            else:
                print("result cell can not be created. div, subcell <=0")
        else:
             print("wrong argument")
    def __str__(self) -> str:
        res = '*'
        for i in range (1, self.subcell):
            if i%5 == 0:
                res += "\n*"
            else:
                res+='*'
        return res

c1 = cell(18)
c2 = cell(16)
c3 = cell(0.5)
print(f"cell3 has {c3.subcell} subcells")

print("add\n")
print((c1+c2).subcell)
print("sub\n")
print((c1-c2).subcell)
print("mul\n")
print((c1*c2).subcell)
print("div\n")
print((c1/c2).subcell)

print(c1)

        