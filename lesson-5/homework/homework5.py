#1.
def is_leap_year(year: int) -> bool:
    """
    Determines whether a given year is a leap year.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2023))  # False

#2.
def check_weird(n: int):
    """
    Determines whether a given number is "Weird" or "Not Weird"
    based on the specified conditions.

    Parameters:
    n (int): The integer to be checked.

    Returns:
    None: Prints "Weird" or "Not Weird".
    """
    if n % 2 == 1:  # Odd number
        print("Weird")
    elif 2 <= n <= 5:  # Even and in range 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:  # Even and in range 6 to 20
        print("Weird")
    else:  # Even and greater than 20
        print("Not Weird")

# Example usage
n = int(input().strip())  # Read input
check_weird(n)

#3.
def check_weird(n: int):
    """
    Determines whether a given number is "Weird" or "Not Weird"
    based on the specified conditions.

    Parameters:
    n (int): The integer to be checked.

    Returns:
    None: Prints "Weird" or "Not Weird".
    """
    if n % 2 == 1:  
        print("Weird")  # Odd numbers are always Weird
    elif n in range(2, 6):  
        print("Not Weird")  # Even numbers between 2 and 5 (inclusive)
    elif n in range(6, 21):  
        print("Weird")  # Even numbers between 6 and 20 (inclusive)
    else:  
        print("Not Weird")  # Even numbers greater than 20

# Example usage
n = int(input().strip())  
check_weird(n)
