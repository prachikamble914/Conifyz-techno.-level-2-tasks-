print("****NUMBER GUESSER****")
import random
number = random.randint(1,10)
solved = False
print("Guess a number")
while not solved:
    guess = int(input())

    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("correct")
        solved = True