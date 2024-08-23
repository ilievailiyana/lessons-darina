"""
Write a function that takes two numbers and returns the larger one.
"""

"""
Write a function that takes a number and returns True 
if the number is even, and False if it is odd.
Hint: you can get a remainder of division with %
-
"""
y = 7.5 / 2
print(y)
x = 6 % 2
print(x)

def is_even(num):
    # ako remainder e 0, znachi chisloto e chetno
    if num % 2 == 0:
        return True
    return False

print(is_even(5))
print(is_even(6))

"""
Write a program that takes 2 numbers from the user and prints the smallest one.
-
"""
min_num = 1000 # pri uslovie che ni e dadeno che chislata sa do 1000

# num1 = float(input("Enter a number: "))
# if num1 < min_num:
#     min_num = num1

# num2 = float(input("Enter a second number: "))
# if num2 < min_num:
#     min_num = num2

# num3 = float(input("Enter a third number: "))
# if num3 < min_num:
#     min_num = num3

for i in range(1, 4, 1):
    num = float(input("Enter a number: "))
    if num < min_num:
        min_num = num
    print("Current min:", min_num)
    print("Current i:", i)

print(min_num)

i = 1
while i < 4:
    num = float(input("Enter a number: "))
    if num < min_num:
        min_num = num
    print("Current min:", min_num)
    print("Current i:", i)
    i = i + 1 # ako ne update-nem i, vinagi shte stoi na 1 i loop-a shte se povtarq do bezkrai

# if num1 < num2 and num1 < num3:
#     print(num1, "is the smallest number.")
# elif num2 < num1 and num2 < num3:
#     print(num2, "is the smallest one.")
# else:
#     print(num3, "is the smallest one.")    

"""
Write a program that calculates the average student grade. 
The user should be able to enter grades one by one and decide when to stop
and to see the result printed.
"""
sum = 0
counter = 0
while True:
    grade = int(input("Please enter a grade or -1 to exit: "))
    if grade == -1:
        break
    sum = sum + grade
    counter = counter + 1
    # stop = input("Enter stop to exit: ")
    # if stop == "stop":
    #     break
if counter != 0:
    average = sum / counter
    print("The average is", average)
else:
    print("No grades to calculate")