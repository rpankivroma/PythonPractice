"""
Python Modules — Task

Task Description
Build a small Python program that uses modules to organize functionality and perform specific tasks.

Requirements
🧱 1. Create Your Own Module
Create a file named text_utils.py
Inside it, write two functions:

def count_words(text):
    # returns the number of words in text

def count_chars(text):
    # returns number of characters (no spaces) in text

📥 2. Main Program
Create a main file called main.py and do the following:
🟡 a. Import Your Module
Import text_utils in at least two different ways:
Normal import

Using an alias
🟢 b. Use Your Module Functions
Ask the user to enter a sentence
Print the number of words and number of characters using your module’s functions.

Example:

Enter a sentence: Hello Python World
Words: 3
Characters (no spaces): 15

🧠 3. Use a Built-in Module
Import Python’s random module
Randomly shuffle the words of the input sentence and print the result

Example output:

Shuffled: Python Hello World

🆔 4. Aliasing
Import random with an alias (e.g., rnd)
Use the alias to pick a random word from the sentence and print it

Example:

Random word: World

🏁 5. Organized Output
Print a clear summary at the end, for example:
Original text: Hello Python World
Words: 3
Characters (no spaces): 15
Shuffled: Python Hello World
Random word: World
"""
# Answer

import text_utils
import random as rnd

UserString = str(input("Enter a sentence:"))

words = UserString.split()
rnd.shuffle(words)
shuffled_text = " ".join(words)

print("Original text: ", UserString)
print("Words: ", text_utils.count_words(UserString))
print("Characters (no spaces): ", text_utils.count_chars(UserString))
print("Shuffled: ", shuffled_text)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonModules.py"
Enter a sentence:Hello Python World
Original text:  Hello Python World
Words:  3
Characters (no spaces):  16
Shuffled:  World Hello Python
"""