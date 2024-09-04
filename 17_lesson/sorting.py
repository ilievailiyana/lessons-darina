# Reverse string
my_string = "hello world"
reversed_my_string = my_string[::-1]
print(f"Reverse string: {reversed_my_string}")

# List Sorting
my_list = [10, 2, 30, 4, 5]

# Sort it in ascending order (returning new list)
sorted_list = sorted(my_list)
print("Sorted new list:", sorted_list)
print("Original list remains unchanged:", my_list)

# Sort it in ascending order - ot nai malko kym nai-golqmo
my_list.sort()
print("Sorted list in-place: ", my_list)

# Sort in descending order - ot nai golqmo kym nai-malko 
my_list.sort(reverse=True)
print("Sorted list in descending order (in-place):", my_list)

# Alternative to sort in descending order
my_list.sort()
my_list.reverse()

# List Reversing
my_list = [10, 40, 5, 20, -1]
my_list.reverse()
print("Reversed list:", my_list)

# Reversing and returning new list
my_list = [10, 40, 5, 20, -1]
reversed_list = my_list[::-1]
print("Reversed list (new list):", reversed_list)

# Functions for finding max and min in a list
print(max(my_list))
print(min(my_list))

