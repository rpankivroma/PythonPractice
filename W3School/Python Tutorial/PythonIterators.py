"""
Task: Build and Use Custom Iterators

Part 1 — Simple Iterator with iter() and next()
Create a list of 10 numbers (your choice).
Get an iterator from that list using iter().
Print the first 5 values using next() manually.
➡️ This tests basic use of iter() and next(). 
W3Schools

Part 2 — Loop Through Iterator
Modify your solution so it loops through the whole iterator and prints each element (one per line), 
without using next() manually — use a loop (for) instead.
➡️ This checks that you understand how a for loop uses the iterator behind the scenes. 
W3Schools

Part 3 — Custom Iterator Class
Create your own iterator class called EvenNumbers, which will generate even numbers 
starting from 2 up to (and including) a user-given limit.

Your class must:
✔ implement __iter__()
✔ implement __next__()
✔ raise StopIteration when the next even number would be greater than the limit

Example usage:

evens = EvenNumbers(10)

for v in evens:
    print(v)


Expected output:
2
4
6
8
10
"""

# Answer

print(" ---------------- Part 1 — Simple Iterator with iter() and next() ----------------------")

ListOfNambs = list(range(10))
myit = iter(ListOfNambs)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print(" -------------------------- Part 2 — Loop Through Iterator -----------------------------")

for i in ListOfNambs:
    print(i)

print(" --------------------------- Part 3 — Custom Iterator Class ----------------------------")


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  if x % 2 == 0:
    print(x)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonIterators.py"
 ---------------- Part 1 — Simple Iterator with iter() and next() ----------------------
0
1
2
3
4
 -------------------------- Part 2 — Loop Through Iterator -----------------------------
0
1
2
3
4
5
6
7
8
9
 --------------------------- Part 3 — Custom Iterator Class ----------------------------
2
4
6
8
10
12
14
16
18
20
"""