#Number guessing game

import random

num=random.randint(1,100)
count=0
guess=7
while guess!=num:
    guess=int(input("Guess a Number between 1 and 100: "))
    if guess>num:
        print("Too high!")
        count+=1
    elif guess<num:
        print("Too low!")
        count+=1
    else:
        print(f"Correct! You Win You took {count+1} attempts to guess")
        break

    