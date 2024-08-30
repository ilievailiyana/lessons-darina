names = ["Alice", "Bob", "Charlie", "David"]
# name_to_remove = input(f"Which name do you want to remove from the list: {names}? ")
# if name_to_remove in names:
#     names.remove(name_to_remove)
#     print("List after removing the name you specified: ", names)
# else:
#     print("Sorry, no such name in the list.")

# change_name = input(f"Which name would you like to change: {names}? ")
# if change_name in names:
#     new_name = input("Please enter the new name: ")
#     # change the value of the name the user said
#     index_of_change_name = names.index(change_name) # vzimame index-a t.e. nomera na elementa v lista za da moje da go promenim na novo value 
#     names[index_of_change_name] = new_name # promenqme na novo value kato trqbva da kajem v koq kutiika ili na koi index da smenim value-to
#     print("Updated list:", names)
# else:
#     print("Please try with a valid name.")


# znaem che ima 'b' v lista no ne znaem na koq poziciq
# i za da smenim 'b' na drugo value/element, trqbva da znaem index-a
numbers = ['a', 'b', 'f', 'r']
index_of_b = numbers.index(1)
# smenqme 'b' na 'c'
numbers[index_of_b] = 'c'
print("First update:", numbers)

# ako znaem index-a, pravim:
# imeto na lista [ index-a na elementa koito iskame da smenim ] = new value
numbers[1] = 'z'
print("Second update:", numbers)