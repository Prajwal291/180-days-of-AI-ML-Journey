#Matrix Multipplication

import numpy as np

a=np.array([1,2,3])
b=np.array([3,4,5])
print(a*b)

a1=np.array([[1,2],
             [3,4]])
b1=np.array([[3,4],
             [5,6]])
print(a1@b1)

'''
Your task

Create:

A = np.array([
    [1, 2],
    [3, 4]
])


B = np.array([
    [5, 6],
    [7, 8]
])

Then calculate:

1. Element-wise multiplication
A * B
2. Matrix multiplication
A @ B
3. Check their shapes
A.shape
B.shape
(A @ B).shape
4. 🔥 Bonus

Create:

C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

and:

D = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

Calculate:

C @ D

Before running it, predict its resulting shape.

Hint:

(2, 3) @ (3, 2)

What should the result shape be?

Try it yourself. No loops. 💪'''

A = np.array([
    [1, 2],
    [3, 4]
])


B = np.array([
    [5, 6],
    [7, 8]
])


print(A * B)

d=A @ B
print(d)

print(A.shape)

print(B.shape)

print(d.shape)


C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


D = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

#C=(2,3) D=(3,2)  C@D=(2,2)  ==> shapes

m=C @ D
print(m)
print(m.shape) 