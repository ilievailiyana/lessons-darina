# Pass Break Continue - loops

# Break
# Kogato imame break - loop-a vednaga prikluchva, bez da izpulnqva sledvasht kod v loop-a
for i in range(0, 10, 1):
    if i == 5:
        break
    print("Did not break yet, i is:", i)

# Continue
# Produlji s loop-a no otnachalo otgore pri proverkata
for i in range(0, 10, 1):
    if i == 5:
        continue
        print("After continue")
    print("After if statement, i is:", i) # nqma da printirame i = 5 zaradi continue

# vse edno go nqma pass-a, code-a si raboti kakto obiknoveno
for i in range(0, 5, 1):
    if i == 3:
        pass # do nothing
        print("After pass")
    print("After if statement, i is:", i)