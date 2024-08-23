"""
Ask the user to enter time between 0 and 24h and print a greeting:
"Good morning!" if the time is between 6am and 12pm
"Good afternoon!" if the time is between 12pm and 5pm
"Good evening!" if the time is between 5pm and 9pm
"Good night!" if the time is between 9pm and 6am

Handle invalid user input (including wrong time e.g. 35)
"""
time = float(input("What time is it? (enter time between 0 and 24): ")) 

# if 6 <= time < 12:
if time >= 6 and time < 12: 
    print("Good morning!")
elif time >= 12 and time <= 17:
    print("Good afternoon!")
elif time > 17 and time < 21:
    print("Good evening!")
elif time >= 21 and time <= 24:
    print("Good night!")
elif time >= 0 and time < 6:
    print("Good night!")
else:
    print("Invalid time!")