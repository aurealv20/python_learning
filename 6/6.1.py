from time import sleep, time
from turtle import color



class TrafficLight:
    _color = ["red", "yellow", "green"]

    def running(self):
        print(self._color[0])
        sleep(1)
        print(self._color[1])
        sleep(1)
        print(self._color[2])
        sleep(1)

tl1 = TrafficLight()

while True:
    try:
        tl1.running()
    except KeyboardInterrupt():
        break


