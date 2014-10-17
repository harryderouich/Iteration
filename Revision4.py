#Harry Derouich
#17/10/14
#Iteration Class Exercises - Revision 4

number = int(input("Please enter a number between 10 and 20: "))
counter = 10
while number < 10 or number > 20:
    number = int(input("That number is not between 10 and 20. Please enter a number between 10 and 20: "))

print("Your number is between 10 and 20")
