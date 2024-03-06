print("*****Welcome The Guessing Game*****")
import random
number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("Enter Guess:-"))
    if(guess<number):
        print("Guess higher!")
    elif(guess>number):
        print("Guess lower!")
    else:
        print("** Congraulation You Won!**")