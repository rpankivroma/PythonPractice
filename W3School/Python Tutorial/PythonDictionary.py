"""
Request: Give me one practice task on topic Python Dictionaries including subtopics in one tast: 
    - Python Dictionaries 
    - Access Items 
    - Change Items 
    - Add Items 
    - Remove Items 
    - Loop Dictionaries 
    - Copy Dictionaries 
    - Nested Dictionaries 
    based on: https://www.w3schools.com/python/python_dictionaries.asp

GPT Practice Task: Python Dictionaries
You are managing a dictionary that stores information about students and their details.
Follow the steps below carefully:
Task Instructions
1. Create a dictionary called student with the following key-value pairs:
    student = {
        "name": "Alice",
        "age": 17,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    }
2. Access Items
    - Print the student’s name and grade using both square brackets and the get() method.
3. Change Items
    - Change "age" to 18.
    - Update "grade" to "A+".
4. Add Items
    - Add a new key "city" with value "London".
    - Add another key "year" with value 2025.
5. Remove Items
    - Remove the "city" key using pop().
    - Remove the last inserted item using popitem().
6. Loop Dictionaries
    - Loop through the dictionary and print:
        - All keys
        - All values
        - All key-value pairs
7. Copy Dictionaries
    - Create a copy of the student dictionary called student_copy.
    - Change the "name" in the copy to "Bob".
    - Print both dictionaries to confirm they’re different.
8. Nested Dictionaries
    - Create a new dictionary called students that contains two students:
        students = {
            "student1": {
                "name": "Alice",
                "age": 18
            },
            "student2": {
                "name": "Bob",
                "age": 19
            }
        }
    - Print the name and age of both students.
"""

# Answer:

#-----------------------------------------------------------------
# 1. Create a dictionary
#-----------------------------------------------------------------

student = {
        "name": "Alice",
        "age": 17,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    }

#-----------------------------------------------------------------
# 2. Access Items
#-----------------------------------------------------------------

print(student["name"])
print(student["grade"])
print(student.get("name"))
print(student.get("grade"))

#-----------------------------------------------------------------
# 3. Change Items
#-----------------------------------------------------------------

student["age"] = 18
student.update({"grade" : "A+"})

#-----------------------------------------------------------------
# 4. Add Items
#-----------------------------------------------------------------

student["City"] = "London"
student["Year"] = 2025

print("Updated atusent:")
for i in student.items():
    print(i)

#-----------------------------------------------------------------
# 5. Remove Items
#-----------------------------------------------------------------

student.pop("City")
student.popitem()

#-----------------------------------------------------------------
# 6. Loop Dictionaries
#-----------------------------------------------------------------

print("Keys:")
for i in student.keys():
    print(i)

print("Values:")
for i in student.values():
    print(i)

print("Keys-Value Pairs:")
for i in student.items():
    print(i)

#-----------------------------------------------------------------
# 7. Copy Dictionaries
#-----------------------------------------------------------------

student_copy = student.copy()
student_copy["name"] = "Bob"

print("Original student", student)
print("Copied student", student_copy)

#-----------------------------------------------------------------
# 8. Nested Dictionaries
#-----------------------------------------------------------------

students = {
    "student1": {
        "name": "Alice",
        "age": 18
    },
        "student2": {
        "name": "Bob",
        "age": 19
    }
}

print("First student:", students["student1"]["name"], students["student1"]["age"])
print("Second student:", students["student2"]["name"], students["student2"]["age"])

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonDictionary.py
Alice
A
Alice
A
Updated atusent:
('name', 'Alice')
('age', 18)
('grade', 'A+')
('subjects', ['Math', 'Science', 'English'])
('City', 'London')
('Year', 2025)
Keys:
name
age
grade
subjects
Values:
Alice
18
A+
['Math', 'Science', 'English']
Keys-Value Pairs:
('name', 'Alice')
('age', 18)
('grade', 'A+')
('subjects', ['Math', 'Science', 'English'])
Original student {'name': 'Alice', 'age': 18, 'grade': 'A+', 'subjects': ['Math', 'Science', 'English']}
Copied student {'name': 'Bob', 'age': 18, 'grade': 'A+', 'subjects': ['Math', 'Science', 'English']}
First student: Alice 18
Second student: Bob 19
"""