#1.
print("Task 1: Input and Print a List")
user_list = list(map(int, input("Enter numbers separated by space: ").split()))
print("List entered:", user_list)

#2.
print("\nTask 2: Sum, Max, and Min")
print("Sum:", sum(user_list))
print("Max:", max(user_list))
print("Min:", min(user_list))

#3:
print("\nTask 3: Tuple of Fruits")
fruits = ("apple", "banana", "orange", "banana", "mango")
print("Fruits Tuple:", fruits)
fruit_to_count = input("Enter a fruit to count: ")
print(f"Count of {fruit_to_count}:", fruits.count(fruit_to_count))
fruit_to_find = input("Enter a fruit to find index: ")
if fruit_to_find in fruits:
    print(f"Index of {fruit_to_find}:", fruits.index(fruit_to_find))
else:
    print(f"{fruit_to_find} not found in tuple.")

#4: Convert tuple to list and sort
print("\nTask 4: Convert Tuple to List and Sort")
fruit_list = list(fruits)
fruit_list.sort()
print("Sorted Fruit List:", fruit_list)

# Task 5: Create a set from user input
print("\nTask 5: Create a Set from User Input")
user_set = set(input("Enter elements for set separated by space: ").split())
print("Set created:", user_set)

# Task 6: Union, Intersection, Add and Remove Elements
print("\nTask 6: Set Operations")
set2 = {"apple", "grape", "banana"}
print("Second Set:", set2)
print("Union:", user_set.union(set2))
print("Intersection:", user_set.intersection(set2))
elem_add = input("Enter element to add to set: ")
user_set.add(elem_add)
print("Set after adding:", user_set)
elem_remove = input("Enter element to remove from set: ")
user_set.discard(elem_remove)  # using discard to avoid error if not present
print("Set after removing:", user_set)

# Task 7: Dictionary with name and age
print("\nTask 7: Dictionary with Name and Age")
people = {}
n = int(input("How many people to enter? "))
for _ in range(n):
    name = input("Enter name: ")
    age = int(input(f"Enter age of {name}: "))
    people[name] = age

print("Original Dictionary:", people)

# Add a key-value pair and update a value
new_name = input("Enter name to add: ")
new_age = int(input(f"Enter age of {new_name}: "))
people[new_name] = new_age
update_name = input("Enter name to update age: ")
if update_name in people:
    people[update_name] = int(input(f"Enter new age for {update_name}: "))
else:
    print(f"{update_name} not found.")

# Loop through dictionary
print("\nLooping through dictionary:")
for name, age in people.items():
    print(f"{name} is {age} years old")
