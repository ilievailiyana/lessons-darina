"""
Write a function that accepts a list as a parameter 
and checks if the list contains only negative numbers 
and return a boolean accordingly (True / False).
"""

"""
Create a dictionary to store some grocery items and their quantity. Ask the user for an item and display the quantity of this item if it is in the dictionary.
Example dictionary:
"""
items = {'apple': 5, 'banana': 25, 'milk': 20}

"""
Create a function, called smart_sum, to sum the numbers contained in a generic list received as input. 
Since the sum function cannot be applied if a list contains non-numeric elements, 
the smart_sum function must:

try to apply the sum function to add all elements of the given list
if the sum cannot be applied, the function must go through all elements of the list 
    and sum only the numeric ones (int and float types)
print the sum on the screen (no output must be returned by the function)
"""

"""
create a Python custom function named multiply that:
has a sequence with a series of numbers as a mandatory parameter
multiplies, using a loop controlled by a counter, all the elements of the sequence different from zero
returns the result of the multiplication
"""
def multiply(seq):
    counter=0
    lenght_list=len(seq)
    # zapazvame multiplication-a v:
    product=1
    # s loop-a iskame da minem prez vseki element,
    # edin po edin, za da moje da proverim dali element-a e razlichen ot 0
    # i da go umnojim ako e taka
    # counter-a realno minava po index-ite na lista seq
    while counter < lenght_list:
        # za da vzemem element ot list-a pishem:
        # imeto na lista[index-a]
        seq_current_element = seq[counter]
        if seq_current_element != 0:
            # trqbva da go multiply-nem
            product = product * seq_current_element
        # vinagi kogato imame while koito ne e while True, trqbva da si update-vame counter-a
        # za da ne runva loop-a do bezkrainost
        counter = counter + 1
    return product

print(multiply([1, 2, 3, 0, 4]))