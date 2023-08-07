"""
classes project;   
"""
class Square:
    """
Updating the class function, size and its value to an integer and also raising a type and value error 
to validate that size value is an integer before assigning size to the private instance attribute.
"""
    def __init__(self, size = 0):
        self.__size = size
        if type(size) is not int:
                    raise TypeError("size must be an integer")
        elif size < 0:
                    raise ValueError("size must be >= 0")
        else:
                self.__size = size

               