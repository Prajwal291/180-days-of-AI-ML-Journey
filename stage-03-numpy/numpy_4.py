#Broadcasting

import numpy as np  


'''Your broadcasting task

Try these without loops:

a = np.array([10, 20, 30, 40])

Calculate:

1.

Add 5 to every element.

Expected:

[15 25 35 45]
2.

Multiply every element by 2.

3.

Subtract 10 from every element.

4. 🔥 Slightly harder

Create:

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

Add:

[10, 20, 30]

to the matrix.

Expected:

[[11 22 33]
 [14 25 36]
 [17 28 39]]

No loops.'''

a = np.array([10, 20, 30, 40])
print(a+5)

print(a*2)

print(a-10)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix+[10,20,30])