def function1(a, b):
    return float(a+b)


def function2(s):
    total = 0
    for number in s:
        if number.isdigit() and int(number)%2==0:
            total += int(number)
    return total

def function2(s):
    return sum([int(c) for c in s if c.isdigit() and int(c)%2==0])


def function3(s1, s2):
    return s1.lower()==s2.lower()

def function3(s1, s2):
    return s1.upper()==s2.upper()


def function4(L):
    if len(L)<2:
        return -1
    else:
        return sorted(L)[-2]

def function4(L):
    if len(L)<2:
        return -1
    else:
        L.sort()
        return L[-2]


def function5(number):
    return str(number)==str(number)[::-1]


def function6(num1, num2):
    if str(num1)[:4]==str(num2):
        return True
    elif str(num1)[-4:]==str(num2):
        return True
    else:
        return False

def function6(num1, num2):
    start = str(num1)[:4]
    end = str(num1)[-4:]
    num2 = str(num2)
    if (num2==start) or (num2==end):
        return True
    else:
        return False

            
def function7(s1, s2):
    duplicated = s1.intersection(s2)
    return sum(s1)+sum(s2)-(sum(duplicated)*2)

def function7(s1, s2):
    total = 0
    for i in range(1, 11):
        if ((i in s1) and (i not in s2)) or ((i not in s1) and (i in s2)):
            total += i
    return total


def function8(L):
    d = dict()

    for num in L:
        if num in d.keys():
            d[num]+=1
        else:
            d[num]=1
    
    for key, value in d.items():
        if value==1:
            return key

def function8(L):
    for i in L:
        if L.count(i)==1:
            return i


def function9(*args):
    if args:
        return sum(args)
    else:
        return -1


def function10(*args, **kwargs):
    if kwargs: 
        return sorted(kwargs.values())[-1]
    else:
        return 0

def function10(*args, **kwargs):
    if kwargs: 
        return max(kwargs.values())
    else:
        return 0
