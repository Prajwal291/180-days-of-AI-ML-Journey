#shape + reshape()
import numpy as np

n=np.array([1,2,3,4,5,6])
print(n.shape)
print(n)

print(n.reshape(2,3))
print(n.shape)
print(n)

'''Your task

Create:

a = np.arange(1, 13)

Then:

Print a
Print a.shape
Reshape it into 3 × 4
Print the reshaped array
Print its shape
Reshape it into 4 × 3
Try reshaping it into 5 × 3 and observe the error.
💡 Hint

You already know the syntax:

a.reshape(____, ____)

Don't use loops.'''

a=np.arange(1,13)

print(a)
print(a.shape)
b=a.reshape(3,4)
print(b)
print(b.shape)
c=b.reshape(4,3)
print(c)
print(c.shape)
#d=c.reshape(5,3)  valueError: cannot reshape array of size 12 into shape (5,3)
