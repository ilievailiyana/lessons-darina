# get 2 numbers from the user and divide them. Print a message if we can't divide them
def division(num1, num2 = 1):
    if num2 == 0:
        # print("We can't divide by 0.")
        return "We can't divide by 0."
    else:
        result = num1/num2
        # print("Result", result)
        return result

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

print("Result from function:", division(num1, num2))


