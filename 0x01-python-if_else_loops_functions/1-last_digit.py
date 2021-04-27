#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
msg1 = "Last digit of"
if last_digit > 5:
    print(msg1, "{} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print(msg1, "{} is {} and is 0".format(number, last_digit))
else:
    print(msg1, "{} is {} and is less than 6 and not 0"
          .format(number, last_digit))
