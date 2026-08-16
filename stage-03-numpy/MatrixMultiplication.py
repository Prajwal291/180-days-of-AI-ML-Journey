#Matrix Multiplication

import numpy as np

A=np.array([[10,20,30],
            [40,50,60],
            [70,80,90]])

B=np.array([[11,22],
            [33,44],
            [55,66]])

C=np.array([[1,2,3],
            [4,5,6]])

mat1=A @ B

mat2=mat1 @ C  #To multiply A X B X C

print(mat1)

print(A.shape)

print(B.shape)

print(mat1.shape)


print(mat2)

print(mat1.shape)

print(C.shape)

print(mat2.shape)
