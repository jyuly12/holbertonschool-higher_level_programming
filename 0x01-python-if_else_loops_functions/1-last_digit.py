#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
print("Last digit of {} is {} and is".format(number, lastdigit), end=' ')
if lastdigit > 5:
    print("greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print("less than 6 and not 0")
else:
    print("0")
