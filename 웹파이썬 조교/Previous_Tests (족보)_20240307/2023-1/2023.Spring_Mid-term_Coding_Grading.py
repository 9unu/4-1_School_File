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
    if (module.function1(1, 4, 5) == 10) and \
        (module.function1(0, 3, -9) == -6) and \
        (module.function1(-3, -2, 5) == 0) and \
        (module.function1(0, 999, 1) == 1000) and \
        (module.function1(-1, -2, -3) == -6):
        score['function1'] = 1
    else:
        score['function1'] = 0
except AttributeError as e:
    score['function1'] = 'Error'
except Exception as e:
    score['function1'] = f'Error: {e}'

try:
    # function2
    if (module.function2([1, 2, 3]) == 4) and \
        (module.function2([]) == 0) and \
        (module.function2([1, 2, 3, 4]) == 4) and \
        (module.function2([-3, 1, 3, 2, 100]) == 1) and \
        (module.function2([2, 4, 6, 8, 10]) == 0) and \
        (module.function2([-1, -3, -5, 0, 1]) == -8):
        score['function2'] = 1
    else:
        score['function2'] = 0
except AttributeError as e:
    score['function2'] = 'Error'
except Exception as e:
    score['function2'] = f'Error: {e}'

try:
    # function3
    if (module.function3([]) == 0) and \
        (module.function3([-99]) == -99) and \
        (module.function3([3, 1, 2, 0]) == 2) and \
        (module.function3([99, 2, -1, 100]) == 99) and \
        (module.function3([-1, -3, -2, 0]) == -1) and \
        (module.function3([0, 1, -2]) == 0) and \
        (module.function3([100]) == 100):
        score['function3'] = 1
    else:
        score['function3'] = 0
except AttributeError as e:
    score['function3'] = 'Error'
except Exception as e:
    score['function3'] = f'Error: {e}'

try:
    # function4
    if (module.function4("Hello") == "hellO") and \
        (module.function4("PyTHON") == "pythoN") and \
        (module.function4("abc") == "abC") and \
        (module.function4("ClasS") == "clasS") and \
        (module.function4("park") == "parK"):
        score['function4'] = 1
    else:
        score['function4'] = 0
except AttributeError as e:
    score['function4'] = 'Error'
except Exception as e:
    score['function4'] = f'Error: {e}'

try:
    # function5
    if (module.function5('todayis0425') == '2.75') and \
        (module.function5('h2a0p2p3y') == '1.75') and \
        (module.function5('A1B2C3') == '2.0') and \
        (module.function5('pyt0hon') == '0.0') and \
        (module.function5('0000') == '0.0') and \
        (module.function5("ab1234CD") == "2.5"):
        score['function5'] = 1
    else:
        score['function5'] = 0
except AttributeError as e:
    score['function5'] = 'Error'
except Exception as e:
    score['function5'] = f'Error: {e}'

try:
    # function6
    if (module.function6(6, 10) == {1, 2}) and \
        (module.function6(2, 3) == {1}) and \
        (module.function6(24, 12) == {1, 2, 3, 4, 6, 12}) and \
        (module.function6(11, 121) == {1, 11}) and \
        (module.function6(2, 2) == {1, 2}) and \
        (module.function6(5, 10) == {1, 5}):
        score['function6'] = 1
    else:
        score['function6'] = 0
except AttributeError as e:
    score['function6'] = 'Error'
except Exception as e:
    score['function6'] = f'Error: {e}'

try:
    # function7
    if (module.function7({"math": 90, "english": 25, "korean": 30}) == 55) and \
        (module.function7({"math": 80, "ai": 38, "python": 80}) == 118) and \
        (module.function7({"korean": 90, "python": 73}) == 163) and \
        (module.function7({"math": 0, "computer": 20, "ai": 99}) == 119) and \
        (module.function7({"python": 88, "statistics": 12}) == 100) and \
        (module.function7({"game": 5, "bio": 3, "robot": 2}) == 10) and \
        (module.function7({"math": 0, "data": 100}) == 100):
        score['function7'] = 1
    else:
        score['function7'] = 0
except AttributeError as e:
    score['function7'] = 'Error'
except Exception as e:
    score['function7'] = f'Error: {e}'

try:
    # function8
    if (module.function8([4,1,2,1,2]) == 4) and \
        (module.function8([1]) == 1) and \
        (module.function8([2, 2, -1]) == -1) and \
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
    if (module.function9(1, 2) == 13) and \
        (module.function9(1, 2, 3) == 6) and \
        (module.function9(-9, -1) == 0) and \
        (module.function9(10, 20, -30) == 0) and \
        (module.function9(0, -1) == 9) and \
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
    if (module.function10(1, 2, a=10, b=7) == 14) and \
        (module.function10(-1, n=10, k=20) == 31) and \
        (module.function10(age=20, height=175) == 195) and \
        (module.function10(1, 2, 3, 4) == -10) and \
        (module.function10() == 0) and \
        (module.function10(10) == -10) and \
        (module.function10(a=22) == 22):
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
print("None means Error.")
print("0 means Wrong.")
print("1 means Correct.")
print("==================")

for problem, point in score.items():
    print(f'- {problem}: {point}')

total_score = 0
for point in score.values():
    if type(point)==int:
        total_score += point

print("==================")
print(f'Your total score is {total_score} / 10 points.')
print("There will be additional penalty points if you used input()/print(), or if your file are not sccuessfully imported.")
