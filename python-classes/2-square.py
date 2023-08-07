"""
 classes project;
 """
class Square:
    """
After updating the class function, size and its value to an integer, raised a type and value error 
to validate that size value is an integer before assigning size to the private instance attribute.
In here we defined a public instance method that returns the current square area of the class function (size).
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