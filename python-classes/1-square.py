"""
classes project;
"""
class Square:
 """
Updating the class function, size and its value to an integer and also raising a type and value error 
to validate that size value is an integer before assigning size to the private instance attribute.
"""
def __init__(self, size = 3):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 3:
            raise ValueError("size must be >=  3")
        else:
            self.__size = size