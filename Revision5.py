#Harry Derouich
#17/10/14
#Iteration Class Exercises - Revision 5

number = 0
total = 0
counter = 1
number_of_numbers = 0
average = 0


while number >= 0:
    number = int(input("Please enter number {0} in the sequence: ".format(counter)))
    counter = counter + 1
    if number >= 0:
        total = total + number
        number_of_numbers = number_of_numbers + 1

average = total / number_of_numbers

print("The average of these numbers is: {0}".format(average))
