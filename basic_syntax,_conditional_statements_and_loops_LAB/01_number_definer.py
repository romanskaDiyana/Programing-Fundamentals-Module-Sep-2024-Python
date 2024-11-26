# Write a program that reads a floating-point number and:
#     • prints "zero" if the number is zero
#     • prints "positive" or "negative"
#     • adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000

from math import fabs

number = float(input())

if number == 0:
    print('zero')

if number < 0:
    if abs(number) < 1:
        print('small negative')
    elif number < -1000000:
        print('large negative')
    else:
        print('negative')

if number > 0:
    if abs(number) > 1 and number <= 1000000:
        print('positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('small positive')
