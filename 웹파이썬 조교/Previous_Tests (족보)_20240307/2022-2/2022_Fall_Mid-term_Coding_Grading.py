import _1 as answer

score = {
    'function01': 0,  # 1 point
    'function02': 0,  # 1 point
    'function03': 0,  # 2 points
    'function04': 0,  # 2 points
    'function05': 0,  # 2 points
    'function06': 0,  # 2 points
    'function07': 0,  # 2 points
    'function08': 0,  # 2 points
    'function09': 0,  # 3 points
    'function10': 0,  # 3 points
}

try:
    # function01
    if (answer.function01(1, 2) == 3) and \
        (answer.function01(0, 0) == 0) and \
        (answer.function01(-1, -2) == -3) and \
        (answer.function01(99, 1) == 100) and \
        (answer.function01(5, 5) == 10):
        score['function01'] = 1
except Exception as e:
    score['function01'] = f'Error: {e}'

try:
    # function02
    if (answer.function02([1, 2, 3, 4, 5]) == 15) and \
        (answer.function02((1, 2, -3, 4)) == 4) and \
        (answer.function02([]) == 0) and \
        (answer.function02((-1, 0, 1)) == 0) and \
        (answer.function02([1, 2, 3, 4]) == 10) and \
        (answer.function02((-3, 6, -2, 1)) == 2):
        score['function02'] = 1
except Exception as e:
    score['function02'] = f'Error: {e}'

try:
    # function03
    if (answer.function03(1, 4) == 5) and \
        (answer.function03(0, 3) == 3) and \
        (answer.function03(-3, -1) == -2) and \
        (answer.function03(-3, 3) == 0) and \
        (answer.function03(0, 6) == 15) and \
        (answer.function03(-3, 6) == 12):
        score['function03'] = 2
except Exception as e:
    score['function03'] = f'Error: {e}'

try:
    # function04
    if (answer.function04([1, 2, 3, 4, 5]) == 6) and \
        (answer.function04((1, 3, 2)) == 2) and \
        (answer.function04([]) == 0) and \
        (answer.function04([-2, 0, 1]) == -2) and \
        (answer.function04([1, 2, 3, 4, 5, 6]) == 12) and \
        (answer.function04((-3, 6, -2, 1)) == 4):
        score['function04'] = 2
except Exception as e:
    score['function04'] = f'Error: {e}'

try:
    # function05
    if (answer.function05('hello') == 'Hello') and \
        (answer.function05('heLLO') == 'Hello') and \
        (answer.function05('pythoN') == 'Python') and \
        (answer.function05('AA') == 'Aa') and \
        (answer.function05('abc') == 'Abc') and \
        (answer.function05("webpythonprogramming") == "Webpythonprogramming"):
        score['function05'] = 2
except Exception as e:
    score['function05'] = f'Error: {e}'

try:
    # function06
    if (answer.function06('level') is True) and \
        (answer.function06('levEL') is True) and \
        (answer.function06('mygyM') is True) and \
        (answer.function06('Aa') is True) and \
        (answer.function06('Wow') is True) and \
        (answer.function06('hello') is False) and \
        (answer.function06("pythoN") is False):
        score['function06'] = 2
except Exception as e:
    score['function06'] = f'Error: {e}'

try:
    # function07
    if (answer.function07([1, 2, 2, 3, 3, 3]) == 6) and \
        (answer.function07((2, 2, 1)) == 3) and \
        (answer.function07([-1]) == -1) and \
        (answer.function07((-1, -1, 0, 1)) == 0) and \
        (answer.function07((10, -10, 1, 2, 10)) == 3) and \
        (answer.function07([0, 0, -1, 10]) == 9):
        score['function07'] = 2
except Exception as e:
    score['function07'] = f'Error: {e}'

try:
    # function08
    if (answer.function08() == 0) and \
        (answer.function08(1) == 0) and \
        (answer.function08(1, 2, 3) == 2) and \
        (answer.function08(1, -2, 3, 6) == 4) and \
        (answer.function08(1, 2, 3, 4, 5) == 6) and \
        (answer.function08(-2, -3, 4, -5) == 2):
        score['function08'] = 2
except Exception as e:
    score['function08'] = f'Error: {e}'

try:
    # function09
    if (answer.function09() == -1) and \
        (answer.function09(1, 2, 3) == -1) and \
        (answer.function09(a=1, b=2) == 2) and \
        (answer.function09(1, 2, 7, n1=5, n2=4) == 5) and \
        (answer.function09(1, k=2) == 2) and \
        (answer.function09(-99, n1=100, n2=200) == 200) and \
        (answer.function09(1, n1=-5, n2=5) == 5):
        score['function09'] = 3
except Exception as e:
    score['function09'] = f'Error: {e}'

try:
    # function10
    if (answer.function10(1) == 1) and \
        (answer.function10(2) == 1) and \
        (answer.function10(3) == 2) and \
        (answer.function10(4) == 3) and \
        (answer.function10(5) == 5) and \
        (answer.function10(10) == 55) and \
        (answer.function10(22) == 17711) and \
        (answer.function10(33) == 3524578):
        score['function10'] = 3
except Exception as e:
    score['function10'] = f'Error: {e}'

######################
# Final score
######################
for problem, point in score.items():
    print(f'{problem}: {point}')

total_score = 0
for point in score.values():
    if type(point)==int:
        total_score += point
print(f'Your final score is {total_score} / 20')
