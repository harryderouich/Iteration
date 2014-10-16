#Harry Derouich
#14/10/14
#Iteration Class Exercises - Revison 3

number = int(input("Please enter the number of numbers you want average: "))
avg_total = 0
counter = 1
while counter < (number + 1):
    avg_number = int("Please enter number {0} in the sequence".format(counter))
    avg_total = avg_total + avg_number
    counter = counter + 1

avg = avg_total / number

print(avg)
