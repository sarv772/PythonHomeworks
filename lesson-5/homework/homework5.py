#1 Function to Check for Leap Year

def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Yil butu sonda berilsin.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#2 Conditional Statements Exercise – “Weird” or “Not Weird”

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#3 Find Even Numbers Between Two Integers (inclusive)

def even_numbers_if_else(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start > end:
        return []
    return list(range(start, end + 1, 2))
