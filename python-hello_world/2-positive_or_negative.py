#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    is_negetive = number -10
    print("number {} is negetive" .format(number))

else:
    is_positive = number % 10
    print("number {} is positive" .format(number))
if number == 0:
    print("number {} is zero" .format(number))