#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
print("Last digit of {} is {} and is '.format(number, lastnum), end = "")
if lastnum > 5:
    print("greater than 5")
elif lastnum == 0:
    print("0")
else:
    print("less than 6 and not 0")
