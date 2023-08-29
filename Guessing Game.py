

from random import randint

guessnumber = int(input(" Enter the guess number between 1 to 5 : "))
randomnumber = randint(1,5)

for x in range(1,6):

  if guessnumber == randomnumber:
    print("You Have Won the Game")

  else:
         print("You Have Loss the Game ")
         print("Your random number : ",randomnumber)
