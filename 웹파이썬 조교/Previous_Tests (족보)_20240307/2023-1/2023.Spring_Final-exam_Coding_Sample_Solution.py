def function1(n):
    total = 0
    while n!=1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        total += n
    return total



def function2(*args):
    total = 0
    for arg in args:
        if arg.find("@")!=-1 and arg.find(".")!=-1 and (arg.find(".")>arg.find("@")):
            total +=1
    return total



def function3(sign, num):
    total = 0
    for i in range(len(sign)):
        if sign[i]=="+":
            total += num[i]
        else:
            total -= num[i]
    return total


def function4(n):
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit)
    if n%total==0:
        return True
    else:
        return False



def function5(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "ZeroDivisionError"
    except:
        return "Error"



class Anonymizer:
    def __init__(self, name):
        """Initializer"""
        self.name = name
    def get_anonymized_name(self, n):
        if n>len(self.name):
            n = len(self.name)
        anonymized_name = "*"*n + self.name[n:]
        return anonymized_name



class Account:
    def __init__(self, balance):
        """Initializer: balance can be negative."""
        self.balance = balance
    
    def deposit(self, money):
        """Deposit the given money to self's balance."""
        self.balance += money
    
    def withdraw(self, money):
        """Withdraw the given money from self's balance."""
        self.balance -= money

    def transfer(self, money, other):
        """Transfer the given money from self's balance to other's account."""
        self.balance-=money
        other.balance+=money

    def __eq__(self, other):
        """Return True if the given two balances are equal, False otherwise.""" 
        return self.balance==other.balance



class NonStrNameError(Exception):
    def __init__(self):
        super().__init__("NonStrNameError")



class Integer:
    def __init__(self, number):
        """Initializer: assume that the number is always int value"""
        self.number = number
    def __add__(self, other):
        """Return a new instance of Integer 
           which number attributes is self.number+other.number.
        """
        return Integer(self.number+other.number)
    def __sub__(self, other):
        """Return a new instance of Integer 
           which number attributes is self.number-other.number.
        """
        return Integer(self.number-other.number)



class University:
    maximum_score = 4.5
    def __init__(self, score):
        """Initializer:
           assume that score is float type, 0.0 <= score <= 4.5."""
        self.score=score

    def get_percentile(self):
        """get a percentile of self's score based on the maximum_score"""
        return f"{int(self.score/self.maximum_score*100)}%"

    @classmethod
    def set_maximum_score(cls, score):
        cls.maximum_score = score

class KyungheeUniversity(University):
    def __init__(self, score):
        super().__init__(score)
        


student1 = University(4.0)
student2 = KyungheeUniversity(4.0)
print(student1.get_percentile())
print(student2.get_percentile())
KyungheeUniversity.set_maximum_score(4.3)
print(student1.get_percentile())
print(student2.get_percentile())
University.set_maximum_score(4.0)
print(student1.get_percentile())
print(student2.get_percentile())
