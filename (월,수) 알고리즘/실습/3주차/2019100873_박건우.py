def bs(data, item, low, high):
    
    if(low>high):
        return -1
    else:
        mid_idx= (low+high)//2
        if(item==data[mid_idx]):
            return mid_idx
        elif item<data[mid_idx]:
            return bs(data, item, low, mid_idx-1)
        else:
            return bs(data, item, mid_idx+1, high)
            
         

data=[1,3,5,6,7,9,10,14,17,19]
n=10
location=bs(data,17,0,n-1)
print(location)


def mergeSort(n,s):
    h=n//2  # 중간 인덱스
    m=n-h   # 왼쪽에 들어가고 남은 요소 개수
    if(n>1):
        u=s[:h]
        v=s[h:]
        mergeSort(h,u)  # 재귀  (왼쪽)
        mergeSort(m,v)  # 재귀  (오른쪽)
        merge(h,m,u,v,s)    # 1차 재귀가 끝을 찍고 돌아가기 시작 
                            # -> merge 함수 안에서 두개 리스트안의 요소를 비교
                            # ->작은것부터 s리스트 (원본)의 요소들을 순서대로 교정

def merge(h,m,u,v,s):
    i=j=k=0 # i = 왼쪽 리스트 인덱스
            # j = 오른쪽 리스트 인덱스
            # k = 원본 리스트를 수정할 때 사용하는 인덱스
    while i<h and j<m:
        if u[i]<v[j]:   # 왼쪽 리스트의 값으로 업데이트
            s[k]=u[i]
            i+=1
        else:           # 오른쪽 리스트의 값으로 업데이트
            s[k]=v[j]
            j+=1
        k+=1            # 원본 리스트에서의 업데이트 대상 인덱스 +1
        
    while i<h:          # 위의 루프가 끝났다는건, 왼쪽 or 오른쪽 리스트 중 하나의 값이 전부 들어갔다는 것
        s[k]=u[i]       # 이때 i<h라는건 왼쪽 리스트에 값이 남아있다는 것
        i+=1            # 왼쪽 리스트에 남은 값들을 전부 넣어줌
        k+=1
    
    while j<m:          # 반대오 오른쪽 리스트에 값이 남아 있는 것
        s[k]=v[j]
        j+=1
        k+=1

s=[3,5,2,9,10,14,4,8]
mergeSort(8,s)
print(s)