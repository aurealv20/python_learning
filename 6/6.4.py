from turtle import speed


class Car:
    name = "none"
    color = "none"
    speed = "none"
    isPolice = False

    def go(self):
        print("car is moving")

    def stop(self):
        print("car stopped")

    def turn(self, side):
        print(f"car turn to {side}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"speed {self.speed} is to high")
        else:
            return super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"speed {self.speed} is to high")
        else:
            return super().show_speed()

class PoliceCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.isPolice = True

a = TownCar()
a.speed = 50
a.show_speed()
a.speed = 90
a.show_speed()
print(a.isPolice)

b = PoliceCar()
b.speed = 100
b.show_speed()
b.go()
b.turn("right")
print(b.isPolice)
