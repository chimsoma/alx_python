"""
classes project;
"""
class Square:
    """
    In this code the public instance method (def my_print(self):)
    was used which prints which prints in stdout the square with the character #.
    """
def my_print(self):
    if self.__size == 0:
        print()
    else:
        for row in range(self.__size):
            for colum in range(self.__size):
                print("#", end ="")
        else:
            print("\n")