"""
Request:Give me one practice task on topic Python Strings including subtopics: 
Python Strings, Slicing Strings, Modify Strings, Concatenate Strings, Format Strings, 
Escape Characters, String Methods, based on https://www.w3schools.com/python/python_strings.asp

GPT Task: Work with Python Strings
Write a Python program that demonstrates the following concepts step by step:

1. Create and Print a String
    - Create a variable text with the value:
        "  Hello, Python World!  "
    - Print the string and its length using len().
2. Slicing Strings
    - Print only the word "Python" using slicing.
    - Print everything from index 2 to the end.
    - Print the first 5 characters.
3. Modify Strings
    - Convert the string to uppercase and lowercase.
    - Remove extra spaces using strip().
    - Replace "Python" with "Coding".
4. Concatenate Strings
    - Create two strings:
        first = "Learning"
        second = "Python"
    - Join them with a space and print the result.
5. Format Strings
    - Create a variable age = 20.
    - Use an f-string to print:
      My name is Roman, and I am 20 years old.
6. Escape Characters
    - Print this exact text (including the quotes):
    - He said, "Python is awesome!"
7. String Methods
    - Use at least five of these methods on your string and print the results:
      .upper(), .lower(), .strip(), .replace(), .split(), .find(), .count(), .startswith(), .endswith()
"""

#Answer:

txt = "  Hello, Python World!  "
print(txt)
print(len(txt))

print(txt[8:15])
print(txt[4:])
print(txt[:5])

print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.replace("Python", "Coding"))

first = "Learning"
second = "Python"
print(first + ' ' + second)

age = 20
print(f"My name is Roman, and I am {age} years old.")

print("He said, \"Python is awesome!\"")

print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.count(","))
print(txt.startswith(" "))
print(txt.endswith(" "))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonStrings.py
  Hello, Python World!  
24
 Python
llo, Python World!
  Hel
  HELLO, PYTHON WORLD!
  hello, python world!
Hello, Python World!
  Hello, Coding World!
Learning Python
My name is Roman, and I am 20 years old.
He said, "Python is awesome!"
  HELLO, PYTHON WORLD!
  hello, python world!
Hello, Python World!
1
True
True
"""