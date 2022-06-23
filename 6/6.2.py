class Road:
    _length = 0
    _width = 0
    __density = 25

    def __init__(self) -> None:
        self._length = 1
        self._width = 1
        

    def __init__(self, length = 0, width = 0) -> None:
        self._length = length
        self._width = width

    def cover_mass(self, thickness):
        return self._width * self._length * self.__density * thickness

a225 = Road(10000, 6)
print(a225.cover_mass(5))

