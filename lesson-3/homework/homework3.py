#1. Create and Access List Elements

fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[2])  # Third fruit (index starts at 0)

# 2. Concatenate Two Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

#3. Extract Elements from a List

numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)

#4. Convert List to Tuple

favorite_movies = ["Inception", "Matrix", "Interstellar", "Gladiator", "Shrek"]
movies_tuple = tuple(favorite_movies)
print(movies_tuple)

#5. Check Element in a List

cities = ["London", "Berlin", "Paris", "Rome"]
is_paris_in_list = "Paris" in cities
print(is_paris_in_list)

#6. Duplicate a List Without Using Loops

numbers = [1, 2, 3]
duplicated = numbers * 2
print(duplicated)

#7. Swap First and Last Elements of a List

nums = [1, 2, 3, 4, 5]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

#8. Slice a Tuple

numbers_tuple = tuple(range(1, 11))  # (1 to 10)
sliced = numbers_tuple[3:8]  # index 3 to 7
print(sliced)

#9. Count Occurrences in a List

colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(blue_count)

#10. Find the Index of an Element in a Tuple

animals = ("cat", "dog", "lion", "tiger")
index_of_lion = animals.index("lion")
print(index_of_lion)

#11. Merge Two Tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print(merged)

#12. Find the Length of a List and Tuple

my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7)
print(len(my_list))
print(len(my_tuple))

#13. Convert Tuple to List

numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print(numbers_list)

#14. Find Maximum and Minimum in a Tuple

nums = (7, 2, 9, 4, 5)
print(max(nums))
print(min(nums))

#15. Reverse a Tuple

words = ("hello", "world", "python", "tuple")
reversed_words = words[::-1]
print(reversed_words)
