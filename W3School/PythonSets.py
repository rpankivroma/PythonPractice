"""
Request: Give me one practice task on topic Python - Set Methods including subtopics in one tast: 
    - Python Sets 
    - Access Set Items 
    - Add Set Items 
    - Remove Set Items 
    - Loop Sets 
    - Join Sets 
    - Frozenset 
    Based on: https://www.w3schools.com/python/python_sets_methods.asp

GPT Practice Task: Python Sets
You are managing a collection of student clubs in a school.
Follow the steps below using Python sets:
1. Create Sets:
    - Create a set named science_club with: "Alice", "Bob", "Clara", "David"
    - Create another set named art_club with: "Eva", "Frank", "Bob", "Grace"
2. Access Set Items:
    - Print all members of science_club using a for loop.
    - Check if "Clara" is in the science_club.
3. Add Set Items:
    - Add "Helen" to the science_club.
    - Add multiple new students "Ian" and "Jack" at once.
4. Remove Set Items:
    - Remove "Bob" from science_club using remove().
    - Use discard() to remove "Zoe" (a student who might not exist).
    - Use pop() to remove one random member from art_club.
    - Print both sets after removals.
5. Loop Sets:
    - Print all current students in both clubs (use a loop for each).
6. Join Sets:
    - Create a new set called all_students that combines both clubs using union().
    - Find students who are in both clubs using intersection().
    - Find students who are only in science_club using difference().
7. Frozenset:
    - Create a frozenset called final_members from the all_students set.
    - Try adding a new name to final_members and observe what happens (it should cause an error because frozensets are immutable).
    - Print the final_members frozenset.
"""

# Answer:

#---------------------------------------
# 1. Create Sets
#---------------------------------------

science_club = {"Alice", "Bob", "Clara", "David"}
art_club = {"Eva", "Frank", "Bob", "Grace"}

#---------------------------------------
# 2. Access Set Items
#---------------------------------------

print("Scinence club Memebers:")
for i in science_club:
    print(i)

print("Is Clara in the science club?", "Clara" in science_club)

#---------------------------------------
# 3. Add Set Items
#---------------------------------------

science_club.add("Helen")
science_club.update(["Ian", "Jack"])

#---------------------------------------
# 4. Remove Set Items
#---------------------------------------

science_club.remove("Bob")
science_club.discard("Zoe")
art_club.pop()

print("Members of the Scinece club after removing:", science_club)
print("Members of the Art club after removing:", art_club)

#---------------------------------------
# 5. Loop Sets
#---------------------------------------

print("Current members of the Science club:")
for i in science_club:
    print(i)

print("Current members of the Art club:")
for i in art_club:
    print(i)

#---------------------------------------
# 6. Join Sets
#---------------------------------------

all_students = science_club.union(art_club)
print("All students:", all_students)

all_students = science_club.intersection(art_club)
print("Students who are in bouth clubs:", all_students)

all_students = science_club.difference(art_club)
print("Student from Scince club:", all_students)

#---------------------------------------
# 7. Frozenset
#---------------------------------------

final_members = frozenset(all_students)

try:
    final_members.add("a new name")
except AttributeError:
    print("Error in 110 line: final_members.adda new name. You cannot modify a frozenset. It is immutable.")

print("Unique names from bouth clubs:", final_members)

"""
Terminal Output: 
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonSets.py
Scinence club Memebers:
Clara
David
Alice
Bob
Is Clara in the science club? True
Members of the Scinece club after removing: {'David', 'Clara', 'Ian', 'Helen', 'Alice', 'Jack'}
Members of the Art club after removing: {'Eva', 'Frank', 'Bob'}
Current members of the Science club:
David
Clara
Ian
Helen
Alice
Jack
Current members of the Art club:
Eva
Frank
Bob
All students: {'David', 'Eva', 'Clara', 'Bob', 'Ian', 'Frank', 'Helen', 'Alice', 'Jack'}
Students who are in bouth clubs: set()
Student from Scince club: {'David', 'Clara', 'Ian', 'Helen', 'Alice', 'Jack'}
Error in 110 line: final_members.adda new name. You cannot modify a frozenset. It is immutable.
Unique names from bouth clubs: frozenset({'Ian', 'David', 'Clara', 'Helen', 'Alice', 'Jack'})
"""

