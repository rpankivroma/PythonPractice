"""
Request: Give me one practice task on topic Python Tuples including subtopics in one tast:
    - Python Tuples 
    - Access Tuples 
    - Update Tuples 
    - Unpack Tuples 
    - Loop Tuples 
    - Join Tuples 
    based on: https://www.w3schools.com/python/python_tuples.asp

GPT Practice Task: Python Tuples
You are working with information about fruits stored in tuples.
Follow the steps below using Python tuples:
1. Create a tuple called fruits containing these items:
    - "apple", "banana", "cherry", "mango", "orange"
2. Access Tuples:
    - Print the first and last fruit from the tuple.
    - Print the second to fourth fruits using slicing.
3. Update Tuples:
    - Convert the tuple to a list, add "kiwi" and "grape", then convert it back to a tuple.
    - Print the new tuple.
4. Unpack Tuples:
    - Unpack the tuple into variables:
       first, second, *middle, last = fruits
    - Print first, middle, and last separately.
5. Loop Tuples:
    - Loop through the fruits tuple and print each item in uppercase.
6. Join Tuples:
    - Create another tuple called exotic_fruits = ("dragonfruit", "papaya").
    - Join it with your fruits tuple to form a new tuple called all_fruits.
    - Print the all_fruits tuple and its total length.
"""

# Answer:

# --------------------------------------------------------
# 1. Create a tuple called fruits containing these items
# --------------------------------------------------------

fruits = ("apple", "banana", "cherry", "mango", "orange")

# --------------------------------------------------------
# 2. Access Tuples
# --------------------------------------------------------

print("The first and last fruit: ", fruits[0], fruits[-1])
print("The second to fourth fruits: ", fruits[1:4])

# --------------------------------------------------------
# 3. Update Tuples
# --------------------------------------------------------

list_fruits = list(fruits)
list_fruits.append("kiwi")
list_fruits.append("grape")
fruits = tuple(list_fruits)
print("The updated tuple: ", fruits)

# --------------------------------------------------------
# 4. Unpack Tuples
# --------------------------------------------------------

first, second, *middle, last = fruits
print("The unpacked tuple: ")
print("First: ", first)
print("Middle: ", middle)
print("Last: ", last)

# --------------------------------------------------------
# 5. Loop Tuples
# --------------------------------------------------------

for i in range(len(fruits)):
  print("One of the printed item: ",fruits[i])

# --------------------------------------------------------
# 6. Join Tuples
# --------------------------------------------------------

exotic_fruits = ("dragonfruit", "papaya")
all_fruits = fruits + exotic_fruits
print(f"All fruits is: {all_fruits}. There are {len(all_fruits)} items in the tuple array.")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonTuples.py
The first and last fruit:  apple orange
The second to fourth fruits:  ('banana', 'cherry', 'mango')
The updated tuple:  ('apple', 'banana', 'cherry', 'mango', 'orange', 'kiwi', 'grape')
The unpacked tuple:
First:  apple
Middle:  ['cherry', 'mango', 'orange', 'kiwi']
Last:  grape
One of the printed item:  apple
One of the printed item:  banana
One of the printed item:  cherry
One of the printed item:  mango
One of the printed item:  orange
One of the printed item:  kiwi
One of the printed item:  grape
All fruits is: ('apple', 'banana', 'cherry', 'mango', 'orange', 'kiwi', 'grape', 'dragonfruit', 
'papaya'). There are 9 items in the tuple array.
"""