import _2022123456 as m

total = 0

# Problem 1
try:
    if (m.function01(S=[1, 2, 3, 4, 5])==9) and (m.function01(S=(1, 3, 2))==4) and (m.function01(S=[])==0) and (m.function01(S=(-2, 1, 3))==4):
        print("Problem #01. Correct (3)")
        total += 3
    else:
        print("Problem #01. Incorrect")
except Exception as e:
    print(f"Problem #01. Error: {e}")

# Problem 2
try:
    if m.function02("level") and m.function02("levEL") and m.function02("Aa") and (not m.function02("hello")) and (not m.function02("park")):
        print("Problem #02. Correct (3)")
        total += 3
    else:
        print("Problem #02. Incorrect")
except Exception as e:
    print(f"Problem #02. Error: {e}")

# Problem 3
try:
    if (m.function03()==0) and (m.function03(1)==0) and (m.function03(1,2,3)==2) and (m.function03(1,-2,3,6)==4) and (m.function03(0,1,2)==2):
        print("Problem #03. Correct (3)")
        total += 3
    else:
        print("Problem #03. Incorrect")
except Exception as e:
    print(f"Problem #03. Error: {e}")

# Problem 4
try:
    if (m.function04(1, "10") is None) and (m.function04(1, 10)==0.1) and (m.function04(0, 0) is None) and (m.function04("1", 0) is None) and (m.function04(4, 2)==2.0):
        print("Problem #04. Correct (3)")
        total += 3
    else:
        print("Problem #04. Incorrect")
except Exception as e:
    print(f"Problem #04. Error: {e}")


# Problem 5
try:
    p = m.Person()
    if p.name.lower() == "park" and p.height == 160:
        p.change_name("Lee")
        p.change_height(180)
        if p.name.lower() == "lee" and p.height == 180:
            print("Problem #05. Correct (4)")
            total += 4
        else:
            print("Problem #05. Inccorect")
    else:
        print("Problem #05. Inccorect")
except Exception as e:
    print(f"Problem #05. Error: {e}")

# Problem 6
try:
    a = m.Animal()
    d = m.Dog()
    if isinstance(d, m.Animal):
        if a.cry().lower() == "cry" and d.cry().lower() == "woof":
            print("Problem #06. Correct (4)")
            total += 4
        else:
            print("Problem #06. Incorret")
    else:
        print("Problem #06. Incorret")
except Exception as e:
    print(f"Problem #06. Error: {e}")


# Problem 7
try:
    h1 = m.Human()
    h2 = m.Human("Kim", 30)
    if h1.name.lower()=="park" and h1.age==20 and h2.name.lower()=="kim" and h2.age==30:
        print("Problem #07. Correct (5)")
        total += 5
    else:
        print("Problem #07. Incorret")
except Exception as e:
    print(f"Problem #07. Error: {e}")

# Problem 8
try:
    n1 = m.Number(2)
    n2 = m.Number(3.15)
    if ((n1+n2) == 5.15) and ((n1-n2) == -1.15) and (n1.number==2) and (n2.number==3.15):
        print("Problem #08. Correct (5)")
        total += 5
    else:
        print("Problem #08. Incorret")
except Exception as e:
    print(f"Problem #08. Error: {e}")

# Problem 9
try:
    s1 = m.Student(1234)
    s2 = m.Student(5678)
    s3 = m.Student(1234)
    if (s1==s1) and (not (s1==s2) and (s1==s3)):
        print("Problem #09. Correct (5)")
        total += 5
    else:
        print("Problem #09. Incorret")
except Exception as e:
    print(f"Problem #09. Error: {e}")

# Problem 10
try:
    a1 = m.Account(0)
    a1.deposit(20)
    a1.withdraw(10)
    a2 = m.Account(100)
    a2.deposit(100)
    a2.withdraw(200)
    if a1.balance==10 and a2.balance==0:
        print("Problem #10. Correct (5)")
        total += 5
    else:
        print("Problem #10. Incorret")
    
except Exception as e:
    print(f"Problem #10. Error: {e}")

# total points
print(f"Your Final-exam Points : {total} / 40.")
