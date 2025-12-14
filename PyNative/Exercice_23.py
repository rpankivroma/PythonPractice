"""
Exercise 23: Create a simple countdown timer using a while loop.
Write a code to create a simple countdown timer of 5 seconds using a while loop.

Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

Expected Output:

Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!
"""

# Answer:

import time

def countdown_timer(seconds):
  
  while seconds > 0:
    print(f"Time remaining: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

  print("Time's up!")

duration = 5
countdown_timer(duration)

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_23.py
Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!
"""