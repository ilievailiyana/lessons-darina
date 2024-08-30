# Create a list
empty_list = []
my_list = [100, 25, 3, 'a', 'hello', True]
print("List:", my_list)
print(type(my_list))

# Using the list constructor to create a list
list_from_constructor = list(range(0, 5, 1))
print(list_from_constructor)

# Access elements
# 0 e index-a na cell-a v pametta, a kakvo ima v neq e element-a
first_element = my_list[0]
print("First element:", first_element)

element_at_index_2 = my_list[2]
print("Third element: ", element_at_index_2)

last_element = my_list[-1]
print("Last element:", last_element)

# Length list
list_length = len(my_list)
print("List length:", list_length)

# Iterating through a list - getting & printing each element
for i in my_list:
    print(i)

# Adding new elements
age = 18
my_list.append("new_element")
my_list.append(123)
my_list.append(age)
print("Updated list:", my_list)

# Adding new elements at a specific position in the list
# Ako ima 6 elementa lista, indexes are: 0 1 2 3 4 5
my_list.insert(2, 'new value')
print("Inserted element at position 2: ", my_list)

# Remove elements
my_list.remove('new_element')
print("List after removing element: ", my_list)

# remove element at specific position
# davame index-a na element-a koito iskame da iztriem
del my_list[2]
print("After delete at specific index:", my_list)

# modify elements
# changing the value at index 1
my_list[1] = 600
print("List after modifying second element:", my_list)

# slicing
# [start index (inc) : stop index (excl)]
# Ako iskam da vzema ot vtoriq do 5tiq element v lista, pisha:
subset_list = my_list[1:5]
print("Sliced new list:", subset_list)
print("Original list remains the same:", my_list)

# adding several elements or concatenating two lists
other_list = ['a', 'b', 'c']
big_list = my_list + other_list
print("Big list:", big_list)

# finding elements in a list
# element value in list name
print("Is 3 in the list?", 3 in my_list)
if 3 in my_list:
    print("Found the number in the list!")

# If we want to find the index of an element
# it returns the index of the first such element found
index = my_list.index('a')
print("First index of the element 'a' is:", index)