from lab_python_oop.figure import figuresh
from lab_python_oop.colorcl import colorofshape


class rectangle(figuresh):
    name = "rectangle"

    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__color = colorofshape(color).color

    def square(self):
        return self.__width * self.__height

    def __repr__(self):
        return (f"name: {self.name} | width : {self.__width} | height: {self.__height} | color : {self.__color} | square : {self.__width * self.__height}")


