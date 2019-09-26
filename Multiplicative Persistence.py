import time

def check(num):                           # check(num) counts the steps needed for num to reach single digit number 
    temp = num                        # it multiplies the digits together and then repeats until a single digit number is acheived 
    prod = 1
    count = 0
    while temp//10 != 0:
        for i in str(temp):
            prod = prod*int(i)                 # 277777788888899 is the record till date for largest number of steps
        temp = prod                             #  it took nearly 11 hours to find  this number 
        prod = 1                              
        count += 1
    return count

x = 1
max_steps = 1

while 1:
    steps = check(x)
    if steps > max_steps:                          # max steps will eventually be 11 for 277777788888899
        print(x, end =" ")
        print("-------", end = " ")
        print(steps, end = " ")
        print(time.process_time())
        max_steps = steps
    x += 1
