"""
Create in Python the program Exercise5.5.py containing the grades_average function 
to calculate the average grade of university exams.

In particular, the function must:

ask the user one grade (integer) at a time until an empty value is entered
show the message "Error: the grade must be between 18 and 31" if the user enters 
    an integer less than 18 or greater than 31
return the average grade, rounded to the second decimal place. 
It is recommended to use the built-in round function
"""

def grades_average():
    # promenliva za natrupvane na sum v loop-a
    sum = 0
    # promenliva za broq na ocenkite - za da izchislim average
    count = 0

    # da vzema vsichki ocenki
    while True:
        # Kogato iskame da pozvolim empty value, ne trqbva da se opitvame da prevrushtame tuk v drugi tipove promenlivi
        user_input = input("Enter a grade or press Enter to finish: ")
        # proverka dali user-a iska da spre
        # grade e = na False ako nqma value v tazi promenliva grade
        if not user_input:
            break

        # prevrushtame input-a ot string v chislo
        grade = float(user_input)
        # ako ocenkata e < 18 or > 31 -> print Error message
        if grade < 18 or grade > 31:
            print("Error: the grade must be between 18 and 31")
        else:
            # dobavqme segashniq grade kum sum
            sum = sum + grade
            # update-vame broq na ocenkite, koito shte polzvame za average-a, samo ako e validna ocenkata
            count = count + 1

    if count == 0:
        return 0
    # promenliva za average
    # average = sum / count
    average = round(sum / count, 2)
    # return average grade
    return average

print(grades_average())