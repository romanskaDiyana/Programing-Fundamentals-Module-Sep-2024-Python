# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], print the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.


# n = int(input())
#
# for number in range(1, n + 1):
#     digit_sum = sum(int(digit) for digit in str(number))
#     is_special = digit_sum in [5, 7, 11]
#     print(f"{number} -> {is_special}")

n = int(input())

for number in range(1, n + 1):
    digits_sum = 0
    digits = number

    while digits > 0:
        digits_sum += digits % 10
        digits = int(digits / 10)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
