from lab_python_oop.figure import figuresh
from lab_python_oop.colorcl import colorofshape
from math import pi


class circle(figuresh):
    name = "circle"

    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = colorofshape(color).color

    def __repr__(self):
        return (
            f"name: {self.name} | radius : {self.__radius}  | color : {self.__color} | square : {int(pi ** 2 * self.__radius)}")

    def square(self):
        return pi ** 2 * self.__radius
