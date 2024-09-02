"""
Create in Python the program Exercise4.5.py to generate a specified number of lottery tickets. 

In particular, the program must:

ask the user how many winning lottery tickets they want to generate
randomly generate the number of tickets requested, considering that each ticket is composed of:
    7 digit (starting from the number 1,000,000)
    2 letters: “AX” if the generated number is lower than 3,000,000, 
    “FH” if the number is between 4,500,000 and 5,500,000 (both inclusive), “MJ” in all other cases
show on screen the requested winning tickets
"""
import random

total_tickets = int(input("Enter the winning tickets you want to generate: "))

tickets_list = list()
for i in range(1, total_tickets+1, 1):
    # suzdavame nomerata na vseki bilet koito user-a e poiskal, edin po edin
    ticket_digits = random.randint(1000000, 9999999)
    if ticket_digits < 3000000:
        ticket_letters = "AX"
    elif ticket_digits >= 4500000 and ticket_digits <= 5500000:
        ticket_letters = "FH"
    else:
        ticket_letters = "MJ"
    ticket_number = str(ticket_digits) + ticket_letters
    # print(ticket_number) - tova ako ne polzvame list, tui kato ne sa kazali che iskat list izrichno
    tickets_list.append(ticket_number)

print(tickets_list)