"""
classes project;   
"""
class Square:
    """
    The class function in this code defines a square by a private instance attribut called size. 
    The attribute is made private so, the class builder (author) can easily control the type and value of this attribute.
    """
    def __init__(self, size):
        def __init__(self, size =0):
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
