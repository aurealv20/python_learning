
from unittest.util import _MAX_LENGTH


class coat:
    def __init__(self, size) -> None:
        self.size = size
        self.mat_len = self.size/6.5 + 0.5
    def __str__(self) -> str:
        return f"coat, size {self.size}"

class suit:
    def __init__(self, height) -> None:
        self.height = height
        self.mat_len = self.height*2 + 0.3
    def __str__(self) -> str:
        return f"suit, height {self.height}"
    def __setattr__(self, attr, value) -> None:
        if attr == "height":
            self.__dict__[attr] = value
            #object.__setattr__(self, self.mat_len, self.height*2 + 0.3)
            self.mat_len = self.height*2 + 0.3
        if attr == "mat_len":
            self.__dict__[attr] = value
        else:
            object.__setattr__(self, attr, value)

class clothes:
    def __init__(self, type, size) -> None:
        if type == coat:
            self.type = coat(size)
        elif type == suit:
            self.type = suit(size)
    def __str__(self) -> str:
        return f"{self.type}, requires {self.type.mat_len} of material"
        


ss = clothes(suit, 1.80)
cc = clothes(coat, 45)

#print(cc.type.mat_len%2)

#print(ss.type.mat_len)
#print(ss.type)
#print(ss.type.height)
#print(cc.type)
#print(cc)
print(ss)
ss.type.height = 1.60
print(ss)



