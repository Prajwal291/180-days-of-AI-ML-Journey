#Arrays + dtypes

import numpy as np


print(np.__version__)
numbers=np.array([10,20,30,40,50])
print(type(numbers))

a=np.array([1,2,3,4])
print(a*2)

print(a)
print(type(a))
print(a.dtype)
print(a.shape)

b=np.array([1.2,2.3,3.4])
print(b.dtype)
print(type(b))

c=np.array([1,2,3,4],dtype=float)
print(c)
print(c.dtype)

#1d array
mat=np.array([9,8,7])
print(mat)
print(mat.shape)
mat2=np.array([[1,2,3],[4,5,6]])
print(mat2)
print(mat2.shape)

'''Your first NumPy task

Don't just copy my examples. Build this yourself.

Create:

Array 1

A 1D NumPy array:

[10, 20, 30, 40, 50]

Print:

The array
Its type
Its dtype
Its shape
Array 2

Create this 2D array:

1 2 3
4 5 6
7 8 9

Print:

The array
Its dtype
Its shape'''

array1=np.array([10,20,30,40,50])
print(array1)
print(type(array1))
print(array1.dtype)
print(array1.shape)

array2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)
print(array2.dtype)
print(array2.shape)



