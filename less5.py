import random

range = [1,2,3,4,5,6,7,8,9,10]
secret = random.choice(range)
guess = int(input("Guess a number between '1 and 10': ")) 
if guess == secret:
    print("Congratulations! You guessed the secret number!")
elif guess > secret and guess < 11:
    print("Too high!")
elif guess < secret:
    print("Too low!")
else:
    print("Try again")
    