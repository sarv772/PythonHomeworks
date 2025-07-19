#1 Age calculator
name = input()
age = input()
print(f"You're name is {name}, and you are {age} years old")

#2 Extract car names
txt = 'LMaasleitbtui'
car1 = txt[0::2]
print(car1)
car2 = txt[1::2]
print(txt[1::2])

#3 Extract car names
txt = 'MsaatmiazD'
car1 = txt[0::2]
print(car1)
car2 = txt[::-2]
print(car2)

#4 Extract residence area
txt = "I am John. I am from London"
txt.split( )[-1]
txt[-6:]

#5 Reverse string
Please_type = input()
print(Please_type[::-1])

#6 Count Vowels
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
user_input = input("Yozuvni kiriting: ")
vowel_count = count_vowels(user_input)
print("Unlilar soni:", vowel_count)

#7 Find maximum value
my_list = [1, 3, 6, 8, 9]
maximum = max(my_list)
print("Maxsimum qiymat bu:", maximum)

#8 Check palindrome
def is_palindrome(text):
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]
write_word = input("Enter a word: ")
if is_palindrome(write_word):
    print("Bu palindrome so'z.")
else:
    print("Bu palindrome so'z emas.")

#9 Extract e-mail domain
def extract_domain(email):
    at_index = email.find('@')
    if at_index != -1:
        return email[at_index + 1:]
    else:
        return "Xato email address"
email = input("Email addressni kiriting: ")
domain = extract_domain(email)
print("Domain:", domain)

#10 Generate random password
