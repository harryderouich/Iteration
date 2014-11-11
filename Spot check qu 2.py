#Harry Derouich
#11/11/14
#Iteration Spot Check - Question 2

number = int(input("Please enter a number: "))
count = 1
print("Times table for {0}:".format(number))
for count in range(13):
    if count > 0:
        print("{0:^3} * {1:^3} = {2:^6}".format(count, number, count*number))
    
    

