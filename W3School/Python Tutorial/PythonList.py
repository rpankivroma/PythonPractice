"""
Request: Give me one practice task on topic Python Lists including subtopics in one tast: 
    - Python Lists 
    - Access List Items 
    - Change List Items 
    - Add List Items 
    - Remove List Items 
    - Loop Lists 
    - List Comprehension 
    - Sort Lists 
    - Copy Lists 
    - Join Lists 
    based on: https://www.w3schools.com/python/python_lists.asp

GPT Practice Task: Python Lists
You are managing a list of students and their scores.
Follow the steps below using Python lists:
1. Create a list called students with the following names:
    "Anna", "Bob", "Clara", "David", "Eva"
2. Access list items:
    - Print the first and last student in the list.
3. Change list items:
    - Replace "Bob" with "Ben".
4. Add list items:
    - Add "Frank" to the end of the list.
    - Insert "Grace" at the second position.
5. Remove list items:
    - Remove "Clara" from the list.
    - Remove the last student using pop().
6. Loop lists:
    - Print each student’s name in uppercase using a for loop.
7. List comprehension:
    - Create a new list called short_names that includes only the names with 4 or fewer letters.
8. Sort lists:
    - Sort the students list alphabetically.
9. Copy lists:
    - Create a copy of students called students_copy.
10. Join lists:
    - Create another list called new_students = ["Henry", "Ivy"]
    - Combine it with the main students list.
"""

#Answer:

#-----------------------------------------------
# 1. Create a list called students
#-----------------------------------------------

students = ["Anna", "Bob", "Clara", "David", "Eva"]

#-----------------------------------------------
# 2. Access list items
#-----------------------------------------------

print("First student: ", students[0])
print("Second student: ", students[-1])

#-----------------------------------------------
# 3. Change list items
#-----------------------------------------------

students[1] =  "Ben" 

#-----------------------------------------------
# 4. Add list items
#-----------------------------------------------

students.append("Frank")
students.insert(1, "Grace")

#-----------------------------------------------
# 5. Remove list items
#-----------------------------------------------

students.remove("Clara")
students.pop()

#-----------------------------------------------
# 6. Loop lists
#-----------------------------------------------

print("\nStudents in uppercase:")
for s in students:
    print(s.upper())

#-----------------------------------------------
# 7. List comprehension
#-----------------------------------------------

short_names = []

for i in students:
  if len(i) <= 4:
    short_names.append(i)
    print("\nShort names (4 or fewer letters):", short_names)

#-----------------------------------------------
# 8. Sort lists
#-----------------------------------------------

students.sort()
print("\nSorted students:", students)

#-----------------------------------------------
# 9. Copy lists
#-----------------------------------------------

students_copy = students.copy()
print("Copied list:", students_copy)

#-----------------------------------------------
# 10. Join lists
#-----------------------------------------------

new_students = ["Henry", "Ivy"]

all_students = students + new_students
print("\nJoined list:", all_students)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonList.py
First student:  Anna
Second student:  Eva

Students in uppercase:
ANNA
GRACE
BEN
DAVID
EVA

Short names (4 or fewer letters): ['Anna']

Short names (4 or fewer letters): ['Anna', 'Ben']

Short names (4 or fewer letters): ['Anna', 'Ben', 'Eva']

Sorted students: ['Anna', 'Ben', 'David', 'Eva', 'Grace']
Copied list: ['Anna', 'Ben', 'David', 'Eva', 'Grace']

Joined list: ['Anna', 'Ben', 'David', 'Eva', 'Grace', 'Henry', 'Ivy']

"""