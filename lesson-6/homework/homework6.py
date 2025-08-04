#1 Modify String with Underscores

def insert_underscores(txt):
    result = []
    count = 0
    vowels = 'aeiouAEIOU'
    i = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            if i + 1 < len(txt) and (txt[i + 1] in vowels or txt[i + 1] == '_'):
                count = 0
            elif i + 1 < len(txt):
                result.append('_')
                count = 0
        i += 1
    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)

#2 Integer Squares Exercise

n = int(input())
for i in range(n):
    print(i ** 2)

#3 Loop-Based Exercises
i = 1
while i <= 10:
    print(i)
    i += 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 <= num <= 200 and num % 5 == 0:
        print(num)

num = int(input("Enter number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

for i in range(-10, 0):
    print(i)

for i in range(5):
    print(i)
print("Done!")

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

n_terms = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b

num = int(input("Enter number: "))
factorial = 1
for i in range(2, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")

#4 Return Uncommon Elements of Lists

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for item in c1:
        if item not in c2:
            result.extend([item] * c1[item])
    for item in c2:
        if item not in c1:
            result.extend([item] * c2[item])
    return result
