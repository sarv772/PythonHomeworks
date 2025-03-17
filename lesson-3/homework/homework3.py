#Homework: List and Tuple Exercises
#1. Create and Access List Elements
#Create a list containing five different fruits and print the third fruit.

list = ['apple', 'banana', 'ananas', 'kiwi', 'strawberry']
print(list[2])

#2. Concatenate Two Lists
#Create two lists of numbers and concatenate them into a single list.

list1 = [1, 2, 3, 4, 5]
list2 = [9, 8, 7, 6, 5]
list1.extend(list2)
print(list1)

#3. Extract Elements from a List
#Given a list of numbers, extract the first, middle, and last elements and store 
# them in a new list.

list3 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = len(list3)
print(num1)
first = list3[0]
middle = list3[len(list3) // 2]
last = list3[-1]
list4 = [first] + [middle] + [last]
print(list4)

#4. Convert List to Tuple
#Create a list of your five favorite movies and convert it into a tuple.

list5 = ["mechanic", "beekeeper", "terminator", "avengers", "ip-man"]
my_tuple = tuple(list5)
print(my_tuple)

#5. Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.

list6 = ["Nukus", "New-York", "London", "Paris", "Tokio"]
print("Paris is in the list6." if "Paris" in list6 else "Paris is not in the list6") 

#6. Duplicate a List Without Using Loops
#Create a list of numbers and duplicate it without using loops.

list7 = [9, 4, 3, 2, 7]
list8 = list7.copy
print(list8)

#7. Swap First and Last Elements of a List
#Given a list of numbers, swap the first and last elements.

list9 = [11, 22, 33, 44, 55]
list9[0], list9[-1] = list9[-1], list9[0]
print(list9)

#8. Slice a Tuple
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple1[3:7])

#9. Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.

list10 = ['blue', 'green', 'red', 'yellow', 'blue', 'black']
print(list10.count('blue'))

#10. Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".

my_tuple2 = ('monkey', 'donkey', 'horse', 'giraffe', 'lion', 'tiger')
print(my_tuple2.index('lion'))

#11. Merge Two Tuples
#Create two tuples of numbers and merge them into a single tuple.

my_tuple3 = (12, 23, 34, 45)
my_tuple4 = (67, 78, 89, 90)
merged_tuples = my_tuple3 + my_tuple4
print(merged_tuples)

#12. Find the Length of a List and Tuple
#Given a list and a tuple, find and print their lengths.

list11 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_tuple5 = (21, 32, 43, 54, 65, 76, 98)
lenth_list11 = len(list11)
lenth_my_tuple5 = len(my_tuple5)
print(lenth_list11)
print(lenth_my_tuple5)

#13. Convert Tuple to List
#Create a tuple of five numbers and convert it into a list.

my_tuple6 = (98, 87, 76, 65, 54)
list12 = list[my_tuple6]
print(list12)

#14. Find Maximum and Minimum in a Tuple
#Given a tuple of numbers, find and print the maximum and minimum values.

my_tuple7 = (12, 54, 23, 4, 78)
max_my_tuple7 = max(my_tuple7)
print(max_my_tuple7)
min_my_tuple7 = min(my_tuple7)
print(min_my_tuple7)

#15. Reverse a Tuple
#Create a tuple of words and print it in reverse order.

my_tuple8 = (10, 20, 30, 40, 50)
reverse_my_tuple8 = my_tuple8[::-1]
print(reverse_my_tuple8)
