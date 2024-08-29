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
