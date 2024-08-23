"""
Create in Python the program Exercise3.5.py to show on screen 
the results of the sum and of the multiplication of a series of numbers. 

In particular, the program must:

ask the user to enter an integer or decimal number
ask the user to enter new numbers until he decides to stop (by answering "n" to the program request)
calculate the sum and product of all numbers entered
show on screen with two different messages the results of the sum and of the product of all the numbers entered
"""

sum_result = 0
product_result = 1

while True:
    user_input = input("Enter a number of enter 'n' to stop: ")
    if user_input == 'n':
        break
    number = float(user_input)
    sum_result += number
    # sum_result = sum_result + number
    product_result *= number
    # 1 * 2 * 3 * 4
    # 1 * 2
    # 2 * 3
    # 6 * 4

print(f"The sum of all numbers entered is: {sum_result}")
print(f"The product of all numbers entered is: {product_result}")