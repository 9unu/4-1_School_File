def function1(a, b, c):
    return a+b+c


def function2(L):
    total = 0
    for number in L:
        if number%2==1:
            total += number
    return total


def function2(L):
    return sum([i for i in L if i%2==1])


def function3(L):
    if len(L)==0:
        return 0
    elif len(L)==1:
        return L[0]
    else:
        L.sort()
        return L[-2]


def function3(L):
    if len(L)==0:
        return 0
    elif len(L)==1:
        return L[0]
    else:
        return sorted(L)[-2]


def function4(s):
    return s[:-1].lower() + s[-1].upper()


def function5(s):
    digits = []
    for letter in s:
        if letter.isdigit():
            digits.append(int(letter))
    
    total_sum = 0
    for digit in digits:
        total_sum+=digit
    
    result = total_sum/len(digits)
    return str(result)


def function5(s):
    digits = [int(i) for i in s if i.isdigit()]
    
    return str(sum(digits)/len(digits))
    

def function6(a, b):
    # a's factors
    a_factors = set()
    for i in range(1, a+1):
        if a%i==0:
            a_factors.add(i)

    # b's factors
    b_factors = set()
    for i in range(1, b+1):
        if b%i==0:
            b_factors.add(i)

    common_factors = a_factors.intersection(b_factors)
    return common_factors


def function7(D):
    math_scores = []
    for key, value in D.items():
        if key!="math":
            math_scores.append(value)
    
    sum_math_scores = 0
    for score in math_scores:
        sum_math_scores += score

    return sum_math_scores


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


def function9(a, b, c=10):
    return a+b+c

def function9(*args):
    if len(args)==2:
        return sum(args)+10
    elif len(args)==3:
        return sum(args)
    else:
        # impossible cases
        pass

def function10(*args, **kwargs):

    # calculate sum of positoinal arguments
    positional_arguments = []
    for n in args:
        positional_arguments.append(n)
    
    total_positional_argument = 0
    for i in positional_arguments:
        total_positional_argument+=i

    # calculate sum of keyword arguments' values
    keyword_arguments = []
    for n in kwargs.values():
        keyword_arguments.append(n)

    total_keyword_argument = 0
    for i in keyword_arguments:
        total_positional_argument+=i
    
    return total_keyword_argument - total_positional_argument


def function10(*args, **kwargs):

    # calculate sum of positoinal arguments
    positional_sum = sum(args)

    # calculate sum of keyword arguments' values
    keyword_sum = sum(kwargs.values())
    
    return keyword_sum - positional_sum

