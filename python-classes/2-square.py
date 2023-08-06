"""
 classes project;
 """
class Square:
    """
After updating the class function, size and its value to an integer, raised a type and value error 
to validate that size value is an integer before assigning size to the private instance attribute.
In here we defined a public instance method that returns the current square area of the class function (size).
    """
    def area(self):
        return self.__size * self.__size