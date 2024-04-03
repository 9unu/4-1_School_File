import random
import time
import numpy as np
import matplotlib.pyplot as plt

"""1번"""
# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]: # 더 작은 수를 찾으면 min_idx 업데이트
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Merge Sort
def merge_sort(arr):
    # 요소가 한개 이하면 그대로 반환
    if (len(arr)<=1):
        return arr
    
    # 중간 인덱스
    mid=len(arr)//2

    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])

    # 재귀가 끝을 찍고, 병합되기 시작
    merged_arr=[]

    i=j=0
    while i<len(left_arr) and j<len(right_arr):
        if(left_arr[i]<right_arr[j]):
            merged_arr.append(left_arr[i])
            i+=1
        else:
            merged_arr.append(right_arr[j])
            j+=1

    # 왼쪽, 오른쪽 중 하나는 끝남 -> 못들어가고 남은 애들을 뒤에 붙여주기
    merged_arr+=left_arr[i:] 
    merged_arr+=right_arr[j:]     

    return merged_arr


"""2번"""   
print("2번",'\n',"-"*20) 
n_list=[5000, 10000, 15000,20000, 30000, 40000, 80000]
# A 알고리즘 소요 시간 기록
A_time={}
print("알고리즘 A (selection_sort) 소요 시간")
for n in n_list[:-1]:
    print("-"*10)
    arr=[random.randint(1, 1000) for _ in range(n)]
    print("n:",n)
    # print(arr[:10])
    start_time=time.time()
    selection_sort(arr)
    end_time=time.time()
    # print(selection_sort(arr)[:10])
    elapsed_time=(end_time - start_time)
    A_time[n]=elapsed_time
    print(elapsed_time, "초")


print("알고리즘 B (merge_sort) 소요 시간")
# B 알고리즘 소요 시간 기록
B_time={}
for n in n_list:
    print("-"*10)
    arr=[random.randint(1, 1000) for _ in range(n)]
    print("n:",n)
    # print(arr[:10])
    start_time=time.time()
    merge_sort(arr)
    end_time=time.time()
    # print(merge_sort(arr)[:10])
    elapsed_time=(end_time - start_time)
    B_time[n]=elapsed_time
    print(elapsed_time, "초")

"""3번"""
print("3번",'\n',"-"*20)
double_list=[]
triple_list=[]
quad_list=[]
for i in n_list[:-1]:
    print("*"*20)
    print(f"n({i}):",A_time[i])


    if(i*2 in A_time.keys()):
        print(f"2배(n:{i*2}):",A_time[i*2])
        double_list.append(A_time[i*2]/A_time[i])

    
    if(i*3 in A_time.keys()):
        print(f"3배(n:{i*3}):",A_time[i*3])
        triple_list.append(A_time[i*3]/A_time[i])
    
    if(i*4 in A_time.keys()):
        print(f"4배(n:{i*4}):",A_time[i*4])
        quad_list.append(A_time[i*4]/A_time[i])
    

print(np.mean(double_list))
print(np.mean(triple_list))
print(np.mean(quad_list))

double_list=[]
triple_list=[]
quad_list=[]
for i in n_list[:-1]:
    print("*"*20)
    print(f"n({i}):",B_time[i])


    if(i*2 in B_time.keys()):
        print(f"2배(n:{i*2}):",B_time[i*2])
        double_list.append(B_time[i*2]/B_time[i])

    
    if(i*3 in B_time.keys()):
        print(f"3배(n:{i*3}):",B_time[i*3])
        triple_list.append(B_time[i*3]/B_time[i])
    
    if(i*4 in B_time.keys()):
        print(f"4배(n:{i*4}):",B_time[i*4])
        quad_list.append(B_time[i*4]/B_time[i])

print(np.mean(double_list))
print(np.mean(triple_list))
print(np.mean(quad_list))

"""4번"""
print("4번",'\n',"-"*20)
print("n=40,000일 때 A 알고리즘 수행시간:", A_time[40000])
seconds=A_time[40000]*pow((50000000/40000),2)
years=seconds/(365 * 24 * 60 * 60)
print(seconds,"초")
print(years,"년")


"""5번"""
print("5번",'\n',"-"*20)
x = list(B_time.keys())
y = list(B_time.values())

plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('time')
plt.title('B Algorithm')
plt.show()

x = list(B_time.keys())
y = list(B_time.values())

a_list=[]
for i in range(6):
    a_list.append(y[i]/(x[i]*np.log2(x[i])))
print(a_list)
a=np.mean(a_list)
print(a)


"""6번"""
print("6번",'\n',"-"*20)
n=1000000
while True:
    if(a*n*np.log2(n)>=60):
        break
    n+=1000000
print(n)
print(a*n*np.log2(n))

while True:
    if(a*n*np.log2(n)<=60):
        break
    n-=1
print(n)
print(a*n*np.log2(n))