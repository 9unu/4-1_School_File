def quickSort(s, low, high):
    if high > low:
        pivotpoint = partition(s, low, high)
        quickSort(s, low, pivotpoint - 1)
        quickSort(s, pivotpoint + 1, high)

def partition(s, low, high):
    pivotitem = s[low]
    j = low
    for i in range(low + 1, high + 1):
        if s[i] < pivotitem:
            j += 1
            s[i], s[j] = s[j], s[i]
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

s=[3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print(s)

import numpy as np

def strassen(n, matrix1, matrix2, C):
    threshold = 2

    if n <= threshold:
        C = np.array(matrix1) @ np.array(matrix2)
    else:
        A11 = np.array([[matrix1[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
        A12 = np.array([[matrix1[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
        A21 = np.array([[matrix1[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
        A22 = np.array([[matrix1[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])
        B11 = np.array([[matrix2[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
        B12 = np.array([[matrix2[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
        B21 = np.array([[matrix2[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
        B22 = np.array([[matrix2[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.zeros((int(n/2), int(n/2)))
        M1 = strassen(int(n/2), (A11+A22), (B11+B22), M1)
        M2 = strassen(int(n/2), (A21+A22), B11, M2)
        M3 = strassen(int(n/2), A11, (B12-B22), M3)
        M4 = strassen(int(n/2), A22, (B21-B11), M4)
        M5 = strassen(int(n/2), (A11+A12), B22, M5)
        M6 = strassen(int(n/2), (A21-A11), (B11+B12), M6)
        M7 = strassen(int(n/2), (A12-A22), (B21+B22), M7)
        c11 = M1 + M4 - M5 + M7
        c12 = M3 + M5
        c21 = M2 + M4
        c22 = M1 - M2 + M3 + M6
        C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return C

n = 4
A = [[1, 2, 0, 2], [3, 1, 0, 0], [0, 1, 1, 2], [2, 0, 2, 0]]
B = [[0, 3, 0, 2], [1, 1, 4, 0], [1, 1, 0, 2], [0, 5, 2, 0]]
C=np.array(A)@np.array(B)
D=np.zeros((n,n))
D = strassen(n, A, B, D)
print(C)
print(D)