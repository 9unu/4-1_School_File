"""
1. 순차검색 알고리즘
문제: n개의 키로 구성된 배열 S에 키 x가 있는가?
입력: 양의 정수 n, 1에서 n까지의 첨자를 가진 키의 배열 S, 그리고 x
출력: S안에 x의 위치를 가리키는 location(S안에 x가 없으면 0)
"""
def seqsearch(s,x):
    for i in range(len(s)):
        if(s[i]==x):
            p=i
        else:
            p=-1
    
    return p

s=[3,5,2,1,7,9]
loc=seqsearch(s,4)
print(int(loc))




"""
2. 배열의 수 더하기
문제: n개의 수로 된 배열 S에 있는 모든 수를 더하라
입력: 양의 정수 n, 수의 배열 S(첨자는 1부터 n)
출력: S에 있는 수의 합, sum
"""


def sum1(s):
    result=0
    for a in s:
        result+=a
    return result
        
answer=sum1(s)
print(answer)


def sum2(s):
    result=0
    for i in range(len(s)):
        result+=s[i]
        
    return result


answer=sum2(s)
print(answer)

"""
3. 교환정렬
문제: 비내림차순(nondecreasing order)으로 n개의 키를 정렬하라
입력: 양의 정수 n, 키의 배열 S(첨자는 1부터 n)
출력: 키가 비내림차순으로 정렬된 배열 S
"""

s=[3,2,5,7,1,9,4,6,8]

n=len(s)

for i in range(0, n-1):
    for j in range(i+1, n):
        # 다음거가 더 작으면 뒤에거랑 앞에거의 값을 바꾸기
        if(s[j]<s[i]):
            change=s[j]
            s[j]=s[i]
            s[i]=change

print(s)