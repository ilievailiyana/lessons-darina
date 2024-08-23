# two numbers from user
# math operator

# If operator is invalid, then stop the program (break the loop)

while True:
    choice = input("Enter 'yes' if you want to calculate: ")
    if choice != 'yes':
        print("Goodbye!")
        break 

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the math operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # '+'
    result = 0 # promenlivata e dostupna na nivoto na koeto e definirana + vsichki drugi mesta nadqsno
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0: # != oznachava razlichno ot, obratnoto na ==
            # Mojem da delim, shtom num2 ne e 0
            result = num1 / num2
        else:
            print("Error. Division by zero is forbidden.")
            continue # spri dotuk, i se kachi obratno do nachaloto na loop-a za nov iteration
    else:
        print("Invalid operator. Please enter +, -, *, /")
        continue

    print(f"Result: {num1} {operator} {num2} = {result}")

