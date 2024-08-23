"""
Get a number from the user and check if it is in the range 2 to 102.
"""

"""
Ask the user to enter 3 numbers (one by one) and then find and print
the smallest one and the biggest one.
"""

"""
Ask the user to input a temperature then categorizes the weather based on the temperature:

"Freezing" for temperatures below 0°C
"Cold" for temperatures from 0°C to 10°C (inclusive)
"Cool" for temperatures from 11°C to 20°C (inclusive)
"Warm" for temperatures from 21°C to 30°C (inclusive)
"Hot" for temperatures above 30°C

If the input is not a valid temperature (e.g., below -50°C or above 70°C),
print "Invalid temperature!"
"""

temperature = float(input("Please enter the temperature in Celsius: "))

if temperature < 0 and temperature > -50:
    print("Freezing")
elif 0 <= temperature <= 10:
    print("Cold")
elif 11 <= temperature <= 20:
    print("Cool")
elif 21 <= temperature <= 30:
    print("Warm")
elif temperature > 30 and temperature < 70:
    print("Hot")
else:
    print("Invalid temperature!")

"""
Ask the user for their current game points and the level they are on. 
Allow them to proceed to the next level if they have at least 100 points or 
if they are on level 10. 
Print a message indicating whether they can proceed.
"""

"""
Ask the user to enter the number of books they want to purchase and the total cost. 
If they are buying 
at least 5 books or spending over $50, offer a 10% discount. Print the final cost.
"""

"""
Write a program that takes two numbers as input and checks if they are not equal. 
If they are not equal, print the larger number. 
If they are equal, print "The numbers are equal."
"""