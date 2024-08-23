# 'or' operator

num = 50

# with 'or' operator, only one side of the operator is enough to be True for the whole
# expression to be True
if num < 10 or num > 100: # if True or False -> True
    print(num*num)
else:
    print(num)


# eligible for discount < 12 or elderly > 65
age = 10
if age < 12 or age >= 65:
    print("You get a discount!")
else:
    print("Not eligible for discount, sorry")