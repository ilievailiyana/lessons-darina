"""
Create in Python the program Exercise1.13.py that calculates the number of seconds 
corresponding to a unit of time given in days, hours, minutes and seconds. The program must 
therefore:

ask for the number of days
ask for the number of hours
ask for the number of minutes
ask for the number of second
"""

days = int(input("Enter the number of days: ")) # "24" -> 24
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = seconds + 60 * minutes + 60 * 60 * hours + 24 * 60 * 60 * days

print("Total number of seconds is:", total_seconds)