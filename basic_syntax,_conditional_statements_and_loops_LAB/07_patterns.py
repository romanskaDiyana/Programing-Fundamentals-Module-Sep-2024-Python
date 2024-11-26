# Write a program that receives a number and creates the following pattern. The number represents the largest
# count of stars on one row.

number = int(input())

for n in range(1, number + 1):
    print('*' * n)

for j in range(number - 1, 0, -1):
    print('*' * j)

