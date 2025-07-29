#Dictionary Exercises
#1. Sort a Dictionary by Value
my_dict = {'qovun': 10, 'tarvuz': 5, 'cherry': 20}

# Ascending
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", ascending)

# Descending
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", descending)


#2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print(d)  

#3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
print(result)

#4. Generate a Dictionary with Squares (up to n)

n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)

#5. Dictionary of Squares (1 to 15)

squares = {x: x*x for x in range(1, 16)}
print(squares)

#Set Exercises
#1. Create a Set

my_set = {1, 2, 3, 4, 5}
print(my_set)

#2. Iterate Over a Set
my_set = {"olma", "gilos", "uzum"}
for item in my_set:
    print(item)

#3. Add Member(s) to a Set

my_set = {1, 2, 3, 4, 5, 6}
my_set.add(7)
my_set.update([8, 9])
print(my_set)

#4. Remove Item(s) from a Set

my_set = {1, 2, 3, 4}
my_set.remove(3)  
print(my_set)

#5. Remove an Item if Present in the Set

my_set = {1, 2, 3}
my_set.discard(2)  
print(my_set)
