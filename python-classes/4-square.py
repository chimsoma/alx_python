"""
classes project;
"""
class Square:
    """
    In this code the public instance method (def my_print(self):)
    was used which prints which prints in stdout the square with the character #.
    """
    def __init__(self, size = 0):
        self.__size = size
        if type(size) is not int:
                    raise TypeError("size must be an integer")
        elif size < 0:
                    raise ValueError("size must be >= 0")
        else:
                self.__size = size

    def area(self):
        return self.__size * self.__size
    
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

def my_print(self):
    if self.__size == 0:
        print()
    else:
        for row in range(self.__size):
            for colum in range(self.__size):
                print("#", end ="")
        else:
            print("\n")