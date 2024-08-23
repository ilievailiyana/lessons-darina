password = "n"

# kogato imame cikul while True, trqbwa vutre v loop-a da prekusnem loop-a pri opredeleno uslovie za da ne stane infinite loop
while True:
    entered_pass = input("Enter your password: ")
    if password == entered_pass:
        print("You logged in.")
        break #prekusva loop-a vednaga i nikakuw kod nadolu v loop-a ne se izpulnqva
    print("Wrong password. Try again.") # nqma nujda ot else, tui kato ako sme wlezli w gorniq if, shte sme izlezli ot break-a

print("Broke the loop!")
