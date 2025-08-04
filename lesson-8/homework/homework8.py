#Python Exception Handling: Exercises
#1 Handle ZeroDivisionError

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
#2 Raise ValueError if input is not an integer

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")
#3 Handle FileNotFoundError

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
#4 Raise TypeError if inputs are not numbers

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    raise TypeError("Inputs must be numbers.")
#5 Handle PermissionError when opening a file

try:
    with open("/root/protected.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Error: Permission denied.")
#6 Handle IndexError in list operation

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")
#7 Handle KeyboardInterrupt when user cancels input

try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
#8 Handle ArithmeticError in division

try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")
#9 Handle UnicodeDecodeError when reading file

try:
    with open("file_with_encoding_issue.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Unicode decoding failed.")
#10 Handle AttributeError in list operation

my_list = [1, 2, 3]
try:
    my_list.upper()  # Invalid for list
except AttributeError:
    print("Error: List object has no attribute 'upper'.")

#Python File Input/Output: Exercises: For these, assume you have a sample file called sample.txt

#1 Read entire text file

with open("sample.txt", "r") as file:
    print(file.read())

#2 Read first n lines of a file

n = 3
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")

#3 Append text and display

with open("sample.txt", "a+") as file:
    file.write("\nAppended line.")
    file.seek(0)
    print(file.read())

#4 Read last n lines of a file

n = 2
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(''.join(lines[-n:]))

#5 Read file into a list (line by line)

with open("sample.txt", "r") as file:
    lines = file.readlines()
print(lines)

#6 Read entire file into a variable

with open("sample.txt", "r") as file:
    data = file.read()
print(data)

#7 Read into an array

with open("sample.txt", "r") as file:
    arr = [line.strip() for line in file]
print(arr)

#8 Find longest word(s)

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

#9 Count lines in a file
with open("sample.txt", "r") as file:
    print("Line count:", sum(1 for _ in file))

#10 Count frequency of words

from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().split()
    freq = Counter(words)
    print(freq)

#11 Get file size in bytes

import os
print("File size:", os.path.getsize("sample.txt"), "bytes")

#12 Write a list to a file

items = ['apple', 'banana', 'cherry']
with open("output.txt", "w") as f:
    for item in items:
        f.write(item + "\n")

#13 Copy file contents

with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

#14 Combine lines from two files

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())
