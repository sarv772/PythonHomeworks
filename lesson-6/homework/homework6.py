#1.
def modify_string(txt: str) -> str:
    """
    Inserts an underscore (_) after every third character in the string.
    If a character is a vowel or already has an underscore, the underscore shifts to the next position.
    
    Parameters:
    txt (str): The input string.

    Returns:
    str: The modified string with underscores.
    """
    vowels = "aeiouAEIOU"
    result = []
    count = 0  # Counter to track non-vowel, non-underscore characters

    for i, char in enumerate(txt):
        result.append(char)
        if char not in vowels and char != "_":  
            count += 1  # Only count non-vowel, non-underscore characters
        
        if count == 3:  # Time to insert an underscore
            if i + 1 < len(txt) and (txt[i + 1] in vowels or txt[i + 1] == "_"):
                result.append(txt[i + 1])  # Shift underscore placement
                count = 1  # Reset count as one character is already placed
            result.append("_")
            count = 0  # Reset counter after inserting an underscore

    # Ensure no underscore at the end
    if result[-1] == "_":
        result.pop()

    return "".join(result)

# Test cases
print(modify_string("hello"))  # "hel_lo"
print(modify_string("assalom"))  # "ass_alom"
print(modify_string("abcabcabcdeabcdefabcdefg"))  # "abc_abc_abcd_abcd_abcdef"

#2.
def print_squares(n: int):
    """
    Prints the squares of all non-negative integers i where 0 <= i < n.

    Parameters:
    n (int): The upper limit (exclusive).

    Returns:
    None
    """
    for i in range(n):
        print(i ** 2)

# Read input from user
n = int(input().strip())
print_squares(n)

#3.
#Exercise 1
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
  
#Exercise 2
n = 5  # The maximum number for the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Exercise 3
n = int(input("Enter number: "))
sum_numbers = sum(range(1, n + 1))
print(f"Sum is: {sum_numbers}")

#Exercise 4
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i, end=" ")

#Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number % 25 == 0:
        print(number, end=" ")

#Exercise 6
num = int(input("Enter a number: "))
count = len(str(abs(num)))  # Taking absolute to handle negative numbers
print(f"Output: {count}")

#Exercise 7
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Exercise 8
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item, end=" ")

#Exercise 9
for i in range(-10, 0):
    print(i, end=" ")

#Exercise 10
for i in range(5):
    print(i, end=" ")
print("Done!")

#Exercise 11
start = 25
end = 50

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [n for n in range(start, end + 1) if is_prime(n)]
print("Prime numbers between 25 and 50:", " ".join(map(str, prime_numbers)))

#Exercise 12
terms = 10
fib_series = [0, 1]
while len(fib_series) < terms:
    fib_series.append(fib_series[-1] + fib_series[-2])
print("Fibonacci sequence:", " ".join(map(str, fib_series)))

#Exercise 13
n = int(input("Enter a number: "))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"{n}! = {factorial(n)}")

#Exercise 4
def uncommon_elements(list1, list2):
    return [item for item in list1 + list2 if item not in list1 or item not in list2]

# Test cases
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # Output: [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # Output: [2, 2, 5]
