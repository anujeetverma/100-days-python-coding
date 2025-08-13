import random
import art
print(art.logo)
acc_no = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
level=input("Choose the difficulty, Type 'easy' or 'hard': ").lower()
attempts=10
if level == 'easy':
    attempts=10
elif level == 'hard':
    attempts=5
else:
    print("Enter a valid option")
    print("Entering easy mode")


while attempts>0:
    print(f"You have {attempts} attempts remaining in the game")
    guess = input("Make a guess: ")
    guess= int(guess)
    if guess>acc_no:
        print("Too High")
        attempts-=1
    elif guess<acc_no:
        print("Too Low")
        attempts -= 1
    elif guess == acc_no:
        print(f"You got it! The answer was {acc_no}")
if attempts==0:
    print("You Loose :(")




