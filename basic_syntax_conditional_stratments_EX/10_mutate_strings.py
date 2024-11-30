# You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first one. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

# bubble gum
# turtle hum

# tubble gum
# turble gum
# turtle gum
# turtle hum

first_sting = input()
second_string = input()
last_string = first_sting

for char in range(len(first_sting)):
    left_part = second_string[:char + 1]
    right_part = first_sting[char + 1:]

    new_string = left_part + right_part

    if last_string != new_string:
        print(new_string)
        last_string = new_string
