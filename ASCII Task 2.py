#Harry Derouich
#10/10/14
#ASCII and Unicode Task 2

from random import randint

pass_length = int(input("Please enter the pass length"))


character_count = 1
while character_count <= pass_length:
    integer = randint(97,122)
    character = chr(integer)
    password = character
    character_count = character_count + 1
    old_character = character
    integer = randint(97,122)
    character = chr(integer)
    password = password + character
    character_count = character_count + 1

print(password)

