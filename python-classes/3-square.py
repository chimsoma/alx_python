"""
class project;
"""
class Square:
    """
In this code we introduced the setter and property decorator so we can easily access our private variable(size).
In the property decorator a function (retrival method) was used which takes a single parameter(self), which returns the private instance attribute.
In the setter decorator(size), which takes two values(self, value). value=value that'll be passed in.
A type and value error was raised and a public instance method which returns the value of a square.
"""
def __init__(self, size = 0):
    self.__size = size

@property
def size(self):
    return self.__size

@size.setter
def size(self, value):
    if type(value) is not int:
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = value
    
def area(self):
    return self.__size ** 2