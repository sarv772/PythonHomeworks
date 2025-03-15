#1. Age Calculator
#Write a Python program to ask for a user's name and year of birth, 
#then calculate and display their age.

name = input("What is your name? \n")
print(f'My name is {name}')

year = int(input("When were you born: "))
print(f'My age is {year}')

import datetime
birthdate = "01-01-1991"
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print(f"Calculated age is {age} years.")

#2. Extract Car Names
#Extract car names from the following text:

txt = 'LMaasleitbtui'
print(txt[0:13:2])
print(txt[1:13:2])

#3. Extract Car Names
#Extract car names from the following text:

txt = 'MsaatmiazD'
print(txt[0:10:2])
print(txt[-1] + txt[7] + txt[5] + txt[3] + txt[1])

#4. Extract Residence Area
#Extract the residence area from the following text:

txt = "I'am John. I am from London"
print(txt.rsplit()[-1])

#5. Reverse String
#Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("  ")
print(user_input[::-1])

#6. Count Vowels
#Write a Python program that counts the number of vowels in a given string.

Input_text = input()
counter = Counter(Input_text.lower())
vowels = 'aeiou'
vowel_count = {vowel: counter[vowel] for vowel in vowels if vowel in counter}
print(vowel_count)

#7. Find Maximum Value
#Write a Python program that takes a list of numbers as input and prints the maximum value.

Input_values = input("Write values: ")
Maximum_Input_values = max(Input_values)
print(Maximum_Input_values)

#8. Check Palindrome
#Write a Python program that checks if a given word is 
#a palindrome (reads the same forward and backward).

Check_polindrome = input("Write to check: \n")
rev = ''.join(reversed(Check_polindrome))
if Check_polindrome == rev:
    print("Yes")
else:
    print("No")

#9. Extract Email Domain
#Write a Python program that extracts and prints
#the domain from an email address provided by the user.

Type_email = input("Enter your email address: ")
try:
    domain = Type_email.split('@')[1]
    print("The domain of your email is:", domain)
except IndexError:
    print("Invalid email address. Please include '@' in your input.")

#10. Generate Random Password
#Write a Python program to generate a random password 
#containing letters, digits, and special characters.

import random
import string
create_password = input("Type password: \n")
print(create_password)
