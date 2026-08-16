#indexing and slicing

import numpy as np


arr=np.array([10,20,30,40,50])
print(arr)
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[::-1])

matrix=np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print(matrix)
print(matrix[0,1])
print(matrix[2,0])

'''Create this array:

10 20 30 40
50 60 70 80
90 100 110 120

Then use NumPy indexing/slicing to produce:

20
70
The first row
The last row
The first column
The last column
The middle 2×2 matrix:'''

mat=np.array([[10,20,30,40],
              [50,60,70,80],
              [90,100,110,120]])

print(mat)
print(mat[0,1])
print(mat[1,2])
print(mat[0,:])
print(mat[-1,:])
print(mat[:,0])
print(mat[:,-1])

print(mat[1:,1:3])