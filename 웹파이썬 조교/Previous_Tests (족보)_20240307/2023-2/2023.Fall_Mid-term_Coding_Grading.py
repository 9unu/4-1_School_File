import _2023123456 as module

score = {
    'function1': None,  # 1 point
    'function2': None,  # 1 point
    'function3': None,  # 1 point
    'function4': None,  # 1 point
    'function5': None,  # 1 point
    'function6': None,  # 1 point
    'function7': None,  # 1 point
    'function8': None,  # 1 point
    'function9': None,  # 1 point
    'function10': None,  # 1 point
}

try:
    # function1
    if ((type(module.function1(1, 2)) == float) and module.function1(1, 2) == 3.0) and \
                        ((type(module.function1(0, -1)) == float) and module.function1(0, -1) == -1.0) and \
                        ((type(module.function1(10, 20)) == float) and module.function1(10, 20) == 30.0) and \
                        ((type(module.function1(20, 0)) == float) and module.function1(20, 0) == 20.0) and \
                        ((type(module.function1(-1, -99)) == float) and module.function1(-1, -99) == -100.0):
        score['function1'] = 1
    else:
        score['function1'] = 0
except AttributeError as e:
    score['function1'] = 'Error'
except Exception as e:
    score['function1'] = f'Error: {e}'

try:
    # function2
    if (module.function2("AB1234CD") == 6) and \
        (module.function2("THREE") == 0) and \
        (module.function2("khu9892") == 10) and \
        (module.function2("1") == 0) and \
        (module.function2("2460") == 12) and \
        (module.function2("102abc") == 2):
        score['function2'] = 1
    else:
        score['function2'] = 0
except AttributeError as e:
    score['function2'] = 'Error'
except Exception as e:
    score['function2'] = f'Error: {e}'

try:
    # function3
    if (module.function3("Hell", "HELL")) and \
        (module.function3("ABC", "abc")) and \
        (not module.function3("ABC", "abcde")) and \
        (module.function3("Name", "nAME")) and \
        (not module.function3("GOOD", "GOLD")) and \
        (module.function3("parK", "PARK")):
        score['function3'] = 1
    else:
        score['function3'] = 0
except AttributeError as e:
    score['function3'] = 'Error'
except Exception as e:
    score['function3'] = f'Error: {e}'

try:
    # function4
    if (module.function4([1, 5, 2]) == 2) and \
        (module.function4([1, 20, 10, 2, 8]) == 10) and \
        (module.function4([7, 9])==7) and \
        (module.function4([ ])==-1) and \
        (module.function4([1])==-1):
        score['function4'] = 1
    else:
        score['function4'] = 0
except AttributeError as e:
    score['function4'] = 'Error'
except Exception as e:
    score['function4'] = f'Error: {e}'

try:
    # function5
    if (module.function5(12321)) and \
        (module.function5(987789)) and \
        (not module.function5(121212)) and \
        (not module.function5(999909)) and \
        (module.function5(1)) and \
        (module.function5(22)):
        score['function5'] = 1
    else:
        score['function5'] = 0
except AttributeError as e:
    score['function5'] = 'Error'
except Exception as e:
    score['function5'] = f'Error: {e}'

try:
    # function6
    if (module.function6(12349992, 1234)) and \
        (module.function6(12349992, 9992)) and \
        (not module.function6(71234562, 2345)) and \
        (not module.function6(88376, 1000)) and \
        (module.function6(111111, 1111)) and \
        (not module.function6(111211, 1111)) and \
        (not module.function6(99211, 1991)) and \
        (module.function6(123456, 3456)):
        score['function6'] = 1
    else:
        score['function6'] = 0
except AttributeError as e:
    score['function6'] = 'Error'
except Exception as e:
    score['function6'] = f'Error: {e}'

try:
    # function7
    if (module.function7({1, 2}, {3, 4}) == 10) and \
        (module.function7({1, 2, 3}, {2, 3, 4}) == 5) and \
        (module.function7({1}, {2, 3}) == 6) and \
        (module.function7({7, 9}, {9, 7}) == 0) and \
        (module.function7({1, 2}, {10}) == 13) and \
        (module.function7({1, 2}, {2, 3}) == 4):
        score['function7'] = 1
    else:
        score['function7'] = 0
except AttributeError as e:
    score['function7'] = 'Error'
except Exception as e:
    score['function7'] = f'Error: {e}'

try:
    # function8
    if (module.function8([3,3,2,1,2]) == 1) and \
        (module.function8([1]) == 1) and \
        (module.function8([2, -2, 2]) == -2) and \
        (module.function8([-1, 1, -1, 99, 1, 2, 2]) == 99) and \
        (module.function8([-100]) == -100) and \
        (module.function8([2, 2, 3, 4, 4, 3, 19]) == 19):
        score['function8'] = 1
    else:
        score['function8'] = 0
except AttributeError as e:
    score['function8'] = 'Error'
except Exception as e:
    score['function8'] = f'Error: {e}'

try:
    # function9
    if (module.function9(1, 2) == 3) and \
        (module.function9() == -1) and \
        (module.function9(-9, -1, 10) == 0) and \
        (module.function9(10, -30) == -20) and \
        (module.function9(40) == 40) and \
        (module.function9(0, 1, -2) == -1):
        score['function9'] = 1
    else:
        score['function9'] = 0
except AttributeError as e:
    score['function9'] = 'Error'
except Exception as e:
    score['function9'] = f'Error: {e}'

try:
    # function10
    if (module.function10(1, 2, 3, a=3, b=4) == 4) and \
        (module.function10(3, n=10, k=20) == 20) and \
        (module.function10(height=175) == 175) and \
        (module.function10(1, 2, 9, 3) == 0) and \
        (module.function10() == 0) and \
        (module.function10(10, a=20) == 20) and \
        (module.function10(a=22, b=1) == 22):
        score['function10'] = 1
    else:
        score['function10'] = 0
except AttributeError as e:
    score['function10'] = 'Error'
except Exception as e:
    score['function10'] = f'Error: {e}'


######################
# Total Score
######################
print("==================")
print("0 means Wrong.")
print("1 means Correct.")
print("==================")

for problem, point in score.items():
    print(f'- {problem}: {point} P')

total_score = 0
for point in score.values():
    if type(point)==int:
        total_score += point

print("==================")
print(f'Your total score is {total_score} / 10 points.')
print("\nThere will be additional penalty points if you used input()/print(), or if your file are not sccuessfully imported.")
