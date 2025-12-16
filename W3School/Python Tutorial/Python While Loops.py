"""
🐍 Python While Loops — Task
Task Description

Write a Python program that simulates a simple number-guessing game using a while loop.

📋 Requirements

Ask the user to guess a secret number between 1 and 20.

Use a while loop that keeps prompting the user until they guess the secret number correctly.

Inside the loop:

If the guess is too low, print:
Too low — try again!

If the guess is too high, print:
Too high — try again!

If the guess is correct, print:
Correct! You guessed the number!
and then exit the loop using break.

Use a guess_count variable to count how many guesses the user makes.

Add a while … else: block — after the loop ends normally (not by break), print:
Game over — try again another time!

Once the user guesses correctly, and the loop ends with break, print how many guesses it took.

🧠 Example Program Output
Guess the secret number (1–20): 10
Too low — try again!
Guess the secret number (1–20): 18
Too high — try again!
Guess the secret number (1–20): 15
Correct! You guessed the number!
You guessed it in 3 tries!
"""

# Answer
import random

SECRET = random.randint(1, 20)
guess_count = 0
max_guesses = 7

while guess_count < max_guesses:
    guess = int(input("Guess the secret number (1–20): "))
    guess_count += 1

    if guess < SECRET:
        print("Too low — try again!")
    elif guess > SECRET:
        print("Too high — try again!")
    else:
        print("Correct! You guessed the number!")
        print(f"You guessed it in {guess_count} tries!")
        break
else:
    print("Game over — try again another time!")
    print("Corect answer was: ", SECRET)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/Python While Loops.py"
Guess the secret number (1–20): 10
Too low — try again!
Guess the secret number (1–20): 15
Too low — try again!
Guess the secret number (1–20): 19
Too high — try again!
Guess the secret number (1–20): 18
Too high — try again!
Guess the secret number (1–20): 17
Too high — try again!
Guess the secret number (1–20): 16
Correct! You guessed the number!
You guessed it in 6 tries!
"""