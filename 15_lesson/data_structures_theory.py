# Data structures
"""
List: Mutable - you can modify the elements, add, or remove items after creation.
Set: Mutable - you can add or remove items after creation. Sets do no allow duplicate elements.
Tuple: Immutable - once created, you cannot modify, add or remove elements.
Dictionary: Mutable - you can modify, add, remove elements. Unordered collection of key-value pairs.
"""

# Creation / Syntax
"""
List: [] or list()
Set: {} or set()
Tuple: () or tuple()
Dictionary: {key: value, key2: value2}
"""

# Ordering
"""
List: ordered. Elements are stored in the order they were added.
Set: unordered. Elements have no specific order. From python 3.7: Elements are stored in the order they were added.
Tuple: ordreded. Elements are stored in the order they were added.
"""

# Set
my_set = {1, 2, 2, 3, 'a', 'b'}
print("Set - no duplicated elements:", my_set)

# Tuple
my_tuple = ('c', 1, 2, 3, 'a')
print("Tuple: ", my_tuple)

# List
num = 4
my_list = [1, 2, 3, num]
print(my_list[0])

# Dictionary - Keys in dictionary must be unique
my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}

# Access elements in dictionary - by the key
print(my_dictionary['name'] + " is " + str(my_dictionary['age']))
print( f"{my_dictionary['name']} is {my_dictionary['age']}" )

# Modifying elements in dictionary
my_dictionary['age'] = 30
print( f"{my_dictionary['name']} is (new age) {my_dictionary['age']}" )

# Iterating through dictionary
for k, v in my_dictionary.items():
    print(f"Key: {k} and its value: {v}")

# How to check if a key exists
if 'city' in my_dictionary:
    print("'city' is in the dictionary with value:", my_dictionary['city'])