#Python Dictionary and Set Exercises
#Dictionary Exercises
#1. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.

d = {"Alfa": 1, "Zetta": 8, "Gamma": 5, "Betta": 9}
asc_order = dict(sorted(d.items(), key=lambda item: item[1]))
print(asc_order)
desc_order = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(desc_order)

#2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.

#Sample Dictionary:

#{0: 10, 1: 20}

#Expected Result:

#{0: 10, 1: 20, 2: 30}

add_dict = {0: 10, 1: 20}
add_dict[2] = 30
print(add_dict)

#3. Concatenate Multiple Dictionaries
#Write a Python script to concatenate the following dictionaries to create a new one.

#Sample Dictionaries:

#dic1 = {1: 10, 2: 20}
#dic2 = {3: 30, 4: 40}
#dic3 = {5: 50, 6: 60}

#Expected Result:

#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dic1.copy()
dic4.update(dic2)
dic4.update(dic3)
print(dic4)

#4. Generate a Dictionary with Squares
#Write a Python script to generate and print a dictionary that contains 
# a number (between 1 and n) in the form (x, x*x).

#Sample Dictionary (n = 5):

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict_squares = dict()
for sq in range(1, 6): #n = 5 berilgan, range 1 dan 6 gacha tanlash zarur ekan. Shunda 5 ni ham olar ekan.
    dict_squares [sq] = sq ** 2
print(dict_squares)

#5. Dictionary of Squares (1 to 15)
#Write a Python script to print a dictionary where the keys are 
# numbers between 1 and 15 (both included) and the values are the square of the keys.

#Expected Output:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 
#10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

dict_squares1 = {}
dict_squares1 = {num: num ** 2 for num in range(1, 16)} #n = 1-15 berilgan, range 1 dan 15 gacha tanlash zarur ekan. Shunda 16 ni ham olar ekan.
print(dict_squares1)

#Set Exercises
#1. Create a Set
#Write a Python program to create a set.

create_set = set()
print(create_set)

#2. Iterate Over a Set
#Write a Python program to iterate over sets.

iterate_set = set(1, 2, 3, 4, 5)
for item in iterate_set:
    print(item)

#3. Add Member(s) to a Set
#Write a Python program to add member(s) to a set.

Add_members = set()
Add_members.add("Perfecto")
Add_members.add("Scudetto")
Add_members.add(78)
print(Add_members)

#4. Remove Item(s) from a Set
#Write a Python program to remove item(s) from a given set.

Given_set = {'Rio', 'Zio', 'Vio', 'Dio'}
Given_set.remove('Zio')
Given_set.remove('Vio')
print(Given_set)

#5. Remove an Item if Present in the Set
#Write a Python program to remove an item from a set if it is present in the set.

Items = {'CPU', 'I/O Module', 'Power Module', 'Interface Module'}
if 'CPU' in Items:
    Items.remove('CPU')
print(Items)
