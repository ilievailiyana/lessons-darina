"""
Create in Python the program Exercise2.9.py to determine 
the type of data contained in a variable defined directly within the program. 
Specifically, the program must:

value the test variable

use the type() function to check the nature of the test variable, 
each time verifying equality with the built-in transformation function 
in that type of data (int, float, … written without the ending round brackets)

show on the screen the message “The variable ‘test’ contains XXX so it is of type YYY”, 
where YYY indicates the corresponding type of data (whole number, decimal number, Boolean value 
or string)

Also provide for a control that allows you to manage all cases in which 
the tested value does not correspond to one of the types listed above.

Test the program by trying to assign different types of data to the test variable.
"""

x = 10
y = 10

# print bigger number
if x > y:
    print(x)
else:
    print("Else", y)

num = 6

if num > 5:
    print("Positive number")
elif num < 7: # Ако и двете са True, само първото ще се изпълни, ако тук сме използвали elif
    print("Negative number")
else:
    print("Zero")

