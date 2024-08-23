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

test = 5.5

if type(test) == int:
    print(f"The variable ‘test’ contains {test} so it is of type integer")
    print("hello")
    if test > 0: #This is also in the above if statement
        print("Positive number")
elif type(test) == float:
    print(f"The variable ‘test’ contains {test} so it is of type float")
elif type(test) == bool:
    print(f"The variable ‘test’ contains {test} so it is of type Boolean")
elif type(test) == str:
    print(f"The variable ‘test’ contains {test} so it is of type string")
else:
    print(f"The variable ‘test’ contains {test} which is an unknown type")

# 5 != 6 -> True

# 5 == 5 -> True

# 5 >= 5 -> True
# 5 > 5 -> False 