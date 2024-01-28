from lab_python_oop.rectanglecl import rectangle
from lab_python_oop.colorcl import colorofshape


class squareshape(rectangle):
    name = "square"

    def __init__(self, width, color):
        self.__width = width
        self.__color = colorofshape(color).color

    def __repr__(self):
        return (f"name: {self.name} | width : {self.__width}  | color : {self.__color} | square : {self.__width ** 2}")

    def square(self):
        return self.__width ** 2
