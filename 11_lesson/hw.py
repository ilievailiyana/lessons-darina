"""
Create in Python the program Exercise4.5.py to generate a specified number of lottery tickets. 

In particular, the program must:

ask the user how many winning lottery tickets they want to generate
randomly generate the number of tickets requested, considering that each ticket is composed of:
    7 digit (starting from the number 1,000,000)
    2 letters: “AX” if the generated number is lower than 3,000,000, 
    “FH” if the number is between 4,500,000 and 5,500,000 (both inclusive), “MJ” in all other cases
show on screen the requested winning tickets
"""
# Hint
str1 = "Hello "
str2 = "world"
msg = str1 + str2
print(msg)

"""
Task: write a program for rolling a dice where the computer has already rolled and 
the user is prompted to roll too,
the game stops when the user's roll is greater than the computer's roll and prints:
"Your roll is greater than the computer's roll. You won!"
Otherwise, keep prompting the user to roll again.
If the user enters invalid dice value (other than 1 to 6), then stop the game as well.
"""

"""
Implement a simple password checker program. You know that the correct password is "secretpass". 
Keep prompting the user for a password until they enter the correct one.
"""

"""
Task: Write a function guess_the_number that generates a random number between 1 and 100. 
Ask the user to guess the number and provide feedback on whether their guess is too high, too low, or correct. 
Repeat until the user guesses correctly.
"""

"""
Write a function sum_odd_numbers to calculate and return the sum of all odd numbers
from 1 to a given number. Write a program that takes a number from the user and uses the sum_odd_numbers
function and prints the result.
"""


# Write a function sum_odd_numbers to calculate and return the sum of all odd numbers from 1 to a given number
def sum_odd_numbers(final_number):
    sum = 0
    # calculate sum of all odd numbers from 1 to final_number
    # step e i = i + step
    for i in range(1, final_number + 1, 2):
        # if i % 2 == 0: # Tova go pravim ako step sme slojili da e 1
        #     # chetno chislo shtom nqma ostatuk pri delenie na 2
        #     continue
        sum = sum + i
    return sum

# Write a program that takes a number from the user and uses the sum_odd_numbers function and prints the result.
number = int(input("Please enter a number: "))
print(f"Result of sum of all odd numbers up to {number}: {sum_odd_numbers(number)}")

# sum_odd_numbers(10)
# izvikai funkciqta kato:
# a = 1
# b = 10
# final_number = 10