#Harry Derouich
#17/10/14
#Iteration Class Exercises - Revision 6

counter = 1
kilos = 2.2 * counter


print("|{0:^7}|{1:^7}|".format("kilos","pounds"))
while counter <= 20:
        print("|{0:^7}|{1:^7.1f}|".format(counter, kilos))
        counter = counter + 1
        kilos = 2.2 * counter

        

