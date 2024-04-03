def function01(a, b):
    return a+b


def function02(sequence):
    total = 0
    for i in sequence:
        total += i
    return total


def function03(a, b):
    total = 0
    for i in range(a+1, b):
        total += i
    return total


def function04(sequence):
    total = 0
    for i in sequence:
        if i%2==0:
            total += i
    return total


def function05(s):
    return s[0].upper() + s[1:].lower()


def function06(s):
    return s.upper()==s[::-1].upper()


def function07(sequence):
    total = 0
    for i in set(sequence):
        total += i
    return total


def function08(*args):
    total = 0
    for i in args:
        if i%2==0:
            total += i
    return total


def function09(*args, **kwargs):
    if len(kwargs)==0:
        return -1
    else:
        maximum = sorted(kwargs.values())[-1]
        return maximum


def function10(N):
    fibonacci = [1, 1]
    if N==1 or N==2:
        return fibonacci[N-1]
    else:
        i = 2
        while i<N:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
            i+=1
        return fibonacci[-1]
