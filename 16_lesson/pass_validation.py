"""
Task: Password Validation

Ask the user to create a password. Validate the password based on the following 
criteria:
At least 8 characters long
Contains at least one uppercase letter, one lowercase letter, and one digit.
"""

def validate_password(password):
    if len(password) < 8:
        print("Invalid password. Should be at least 8 characters long.")
        return False
    # check for at least one uppercase letter, one lowercase letter, and one digit.
    counter_upper = 0
    counter_lower = 0
    counter_digit = 0
    for char in password:
        if char.isupper():
            counter_upper = counter_upper + 1
        elif char.islower():
            counter_lower = counter_lower + 1
        elif char.isdigit():
            counter_digit = counter_digit + 1
    
    # proverka dali da vurnem true ili false
    if counter_upper >= 1 and counter_lower >= 1 and counter_digit >= 1:
        return True
    return False

print(validate_password("wordword123H"))

word = "abc"
# word = word.upper()
print(word.upper())