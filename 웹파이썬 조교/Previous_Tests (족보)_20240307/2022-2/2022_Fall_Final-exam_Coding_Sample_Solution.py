# Problem 1 (55%)
def function01(S):
    total = 0
    for i in S:
        if i%2==1:
            total += i
    return total

# Problem 1 
def function01(**kwargs):
    total = 0
    for i in list(kwargs.values())[0]:
        if i%2==1:
            total += i
    return total

# Problem 2 (68%)
def function02(s):
    if s.lower()==s.lower()[::-1]:
        return True
    else:
        return False

# Problem 3 (76%)
def function03(*args):
    total = 0
    for i in args:
        if i%2==0:
            total += i
    return total

# Problem 4 (51%)
def function04(a, b):
    try:
        return a/b
    except:
        return None

# Problem 5 (68%)
class Person:
    def __init__(self):
        self.name = "Park"
        self.height = 160
    def change_name(self, name):
        self.name = name
    def change_height(self, height):
        self.height = height

# Problem 5 
class Person:
    name = "Park"
    height = 160
    def change_name(self, name):
        self.name = name
    def change_height(self, height):
        self.height = height

# Problem 6 (77%)
class Animal:
    def cry(self):
        return "Cry"

class Dog(Animal):
    def cry(self):
        return "Woof"

# Problem 7 (53%)
class Human:
    def __init__(self, name="Park", age=20):
        self.name = name
        self.age = age

# Problem 8 (49%)
class Number:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    def __sub__(self, other):
        return self.number - other.number

# Problem 9 (62%)
class Student:
    def __init__(self, student_number):
        self.student_number = student_number
    def __eq__(self, other):
        return self.student_number == other.student_number

# Problem 10 (55%)
class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        self.balance -= money
