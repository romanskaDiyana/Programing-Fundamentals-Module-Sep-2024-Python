# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive)
# is repeated twice. Note that if you receive the string "SoftUni", you should NOT print it!

while True:
    line = input()
    if line == "End":
        break
    if line != "SoftUni":
        result = ""
        for char in line:
            result += char * 2
        print(result)
