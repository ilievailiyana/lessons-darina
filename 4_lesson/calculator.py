# Use a while loop to print even numbers from 2 to 20.

num = 50
# ako chisloto se deli na 2 bez ostatuk - e even
# operator % - vzima ostatuka
remainder = num % 2
print("Ima ostatuk:", remainder)
if remainder == 0:
    print("Even number:", num)


num = 2
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1