#Harry Derouich
#17/10/14
#Iteration Class Exercises - Revision 6

counter = float(1)
kilos = float(2.2 * counter)


print("|Pounds|Kilos|")
while counter <= 10:
    print("|  {0}   | {1} |".format(counter, kilos))
    counter = counter + 1
    kilos = 2.2 * counter
while 10 < counter <= 20:
    print("|  {0}  | {1} |".format(counter, kilos))
    counter = counter + 1
    kilos = 2.2 * counter
    
