"""
Mini Project – Number Guessing Game
Objective

Create a simple guessing game.

Requirements
Store a secret number.
secret_number = 7
Ask the user to guess the number.
Compare the guess with the secret number.
Print:
Correct Guess

or

Wrong Guess
Bonus Challenge

Instead of only saying correct or wrong:

Too High
Too Low
Correct Guess

using if elif else.
"""

secret_number = 18
guess_number = int(input("Enter number between 1 to 100 both included : "))
if(guess_number == secret_number):
    print(guess_number,"is Correct Guess")
elif(guess_number <= 17):
    print(guess_number,"Too Low")
elif(guess_number >= 19 and guess_number <= 100):
    print(guess_number,"Too High")
else:
    print("Enter number between 1 to 100")
