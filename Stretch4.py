#Harry Derouich
#02/11/14
#Iteration Class Exercises - Stretch 4
tally = 1
phrase = input("Please enter a phrase: ")

for count in(phrase):
      if count == " ":
            tally = tally + 1

print("The number of words is: {0}".format(tally))
