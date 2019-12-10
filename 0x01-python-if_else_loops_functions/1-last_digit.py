#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = number
if positive < 0:
    positive = positive * -1
if number < 0:
    last = (positive % 10) * -1
else:
    last = positive % 10
if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last))
elif (last < 0 and last < 5) or (last <= 5 and last != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last))
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, last))
