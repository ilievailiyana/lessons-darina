num = 1 # 1 e start
while num <= 10: # 10 e stop
    # print(num)
    num += 1 # step


# for variable_name in range(start (inclusive), stop(exclusive), step)
# i = 1 - nqma nujda da definirame i, i priema stoinostta na start
# By default:
    # start is 0
    # step is 1   

# printing uneven numbers
for i in range(1, 11, 2):
    print(i)

# print the numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

sum = 0
for i in range(1, 6, 1):
    sum = sum + i
print("Sum:", sum)