class Stationery:
    title = "none"

    def __init__(self) -> None:
        pass
    
    def __init__(self, name) -> None:
        self.title = name

    def draw(self):
        if self.title != "none":
            print(f"draw with {self.title}")
        else:
            print("draw with something")

class Pen(Stationery):
    def draw(self):
        print("draw with pen")

class marker(Stationery):
    def draw(self):
        if self.title != "none":
            print(f"draw with {self.title} marker")
        else:
            print("draw with marker")

a = Stationery("aaa")
p = Pen("")
m = marker("")
m1 = marker("white")

a.draw()
p.draw()
m.draw()
m1.draw()

