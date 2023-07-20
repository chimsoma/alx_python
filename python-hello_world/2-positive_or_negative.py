#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    is_negetive = number -10
    print(" {} is negetive" .format(number))
else:
    is_positive = number % 10
    print(" {} is positive" .format(number))
if number == 0:
    print(" {} is zero" .format(number))