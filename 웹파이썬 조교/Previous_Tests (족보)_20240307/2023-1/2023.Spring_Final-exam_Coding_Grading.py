import _1234 as m

total = 0


# Problem 1
try:
    if (m.function1(6)==49.0) and \
       (m.function1(4)==3.0) and \
       (m.function1(5)==31.0) and \
       (m.function1(64)==63.0) and \
       (m.function1(8)==7.0):
        print("Problem #01. Correct (4)")
        total += 4
    else:
        print("Problem #01. Incorrect")
except Exception as e:
    print(f"Problem #01. Error: {e}")


# Problem 2
try:
    if (m.function2("admin")==0) and \
       (m.function2("admin@abc.com", "customer@abc.com")==2) and \
       (m.function2("skpark.khu@com", "skpark@khucom")==0) and \
       (m.function2("python@python.org", "sk.park@abccom", "guido@python")==1) and \
       (m.function2()==0):
        print("Problem #02. Correct (4)")
        total += 4
    else:
        print("Problem #02. Incorrect")
except Exception as e:
    print(f"Problem #02. Error: {e}")


# Problem 3
try:
    if (m.function3(["+", "-", "+"], [1, 2, 3])==2) and \
       (m.function3(["-"], [1])==-1) and \
       (m.function3(["+", "+", "-", "+"], [1, 2, 3, 4])==4) and \
       (m.function3(["-", "-", "-"], [1, 2, 3])==-6) and \
       (m.function3(["+", "+", "+"], [2, 3, 4])==9):
        print("Problem #03. Correct (4)")
        total += 4
    else:
        print("Problem #03. Incorrect")
except Exception as e:
    print(f"Problem #03. Error: {e}")
    



# Problem 4
try:
    if m.function4(21) and \
       m.function4(192) and \
       (not m.function4(123)) and \
       m.function4(2024) and \
       (not m.function4(11)) and \
       m.function4(2):
        print("Problem #04. Correct (4)")
        total += 4
    else:
        print("Problem #04. Incorrect")
except Exception as e:
    print(f"Problem #04. Error: {e}")



# Problem 5
try:
    if (m.function5(1, "10")=="Error") and \
       (m.function5(1, 10)==0.1) and \
       (m.function5(0, 0)=="ZeroDivisionError") and \
       (m.function5(99, 99)==1.0) and \
       (m.function5(10, [1, 2, 3])=="Error") and \
       (m.function5(2, 1)==2.0):
        print("Problem #05. Correct (4)")
        total += 4
    else:
        print("Problem #05. Incorrect")
except Exception as e:
    print(f"Problem #05. Error: {e}")


# Problem 6
try:
    a1 = m.Anonymizer("Sangkeun")
    a2 = m.Anonymizer("Kyungheeuniv")
    a3 = m.Anonymizer("N")
    if (a1.name=="Sangkeun") and \
       (a1.get_anonymized_name(1)=="*angkeun") and \
       (a1.get_anonymized_name(2)=="**ngkeun") and \
       (a1.get_anonymized_name(10)=="********") and \
       (a1.get_anonymized_name(7)=="*******n") and \
       (a1.name=="Sangkeun") and \
       (a2.name=="Kyungheeuniv") and \
       (a2.get_anonymized_name(3)=="***ngheeuniv") and \
       (a2.get_anonymized_name(8)=="********univ") and \
       (a2.get_anonymized_name(20)=="************") and \
       (a2.get_anonymized_name(1)=="*yungheeuniv") and \
       (a2.name=="Kyungheeuniv"):
        print("Problem #06. Correct (5)")
        total += 5
    else:
        print("Problem #06. Incorret")
except Exception as e:
    print(f"Problem #06. Error: {e}")


# Problem 7
try:
    a1, a2 = m.Account(0), m.Account(0) 
    if (a1.balance==0) and \
       (a2.balance==0) and \
       (a1==a2):
        a1.deposit(101)
        a2.withdraw(50)
        if (a1.balance==101) and \
           (a2.balance==-50) and \
           (not a1==a2):
            a1.transfer(50, a2)
            a2.deposit(50)
            if (a1.balance==51) and \
               (a2.balance==50) and \
               (not a1==a2):
                a2.transfer(25, a1)
                if (a1.balance==76) and \
                   (a2.balance==25) and \
                   (not a1==a2): 
                    print("Problem #07. Correct (5)")
                    total += 5
                else:
                    print("Problem #07. Incorret")
            else:
                print("Problem #07. Incorret")
        else:
            print("Problem #07. Incorret")
    else:
        print("Problem #07. Incorret")
except Exception as e:
    print(f"Problem #07. Error: {e}")


# Problem 8
try:
    try:
        raise m.NonStrNameError
    except m.NonStrNameError as e:
        if str(e)=="NonStrNameError":
            print("Problem #08. Correct (5)")
            total += 5
        else:
            print("Problem #08. Incorret")
except Exception as e:
    print(f"Problem #08. Error: {e}")


# Problem 9
try:
    n1 = m.Integer(2)
    n2 = m.Integer(3)
    n3 = n1+n2
    n4 = n2-n1
    n5 = m.Integer(10)
    n6 = m.Integer(20)
    n7 = n5+n6
    n8 = n6-n5
    if (n1.number==2) and \
       (n2.number==3) and \
       (n3.number==5) and \
       (n4.number==1) and \
       (type(n1)==type(n4)) and \
       (n5.number==10) and \
       (n6.number==20) and \
       (n7.number==30) and \
       (n8.number==10) and \
       (type(n5)==type(n8)):
        print("Problem #09. Correct (5)")
        total += 5
    else:
        print("Problem #09. Incorret")
except Exception as e:
    print(f"Problem #09. Error: {e}")


# Problem 10
try:        
    try:
        # 학생이 자기 코드에 KyungheeUniversity 구현했으면 그걸 사용
        m.KyungheeUniversity(4.0)
        KyungheeUniversity = m.KyungheeUniversity
    except:
        # 학생이 자기 코드에 구현 안했으면 아래 KyungheeUniversity 사용
        class KyungheeUniversity(m.University):
            def __init__(self, score):
                super().__init__(score)
        
    student1 = m.University(4.0)
    student2 = m.KyungheeUniversity(4.0)
    if (student1.get_percentile()=="88%") and (student2.get_percentile()=="88%"):
        KyungheeUniversity.set_maximum_score(4.3)
        student2 = KyungheeUniversity(4.0)
        if (student1.get_percentile()=="88%") and (student2.get_percentile()=="93%"):
            KyungheeUniversity.set_maximum_score(4.0)
            if (student1.get_percentile()=="88%") and (student2.get_percentile()=="100%"):
                print("Problem #10. Correct (5)")
                total += 5
            else:
                print("Problem #10. Incorret")
        else:
            print("Problem #10. Incorret")
    else:
        print("Problem #10. Incorret")
    
except Exception as e:
    print(f"Problem #10. Error: {e}")

# total points
print(f"Your Final-exam Points : {total} / 45.")
