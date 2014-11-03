#Harry Derouich
#01/11/14
#Iteration Class Exercises - Development 4

largest = 0
num = 0
new_num = 0


while new_num >= 0:
    new_num = int(input("Please enter a number: "))
    if new_num > largest:
        largest = new_num

print(largest)
