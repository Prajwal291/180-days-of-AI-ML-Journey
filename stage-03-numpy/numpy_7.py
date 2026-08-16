import random
import numpy as np


#Int values
a=np.random.randint(1,11,size=(5))
print(a)

b=np.random.randint(1,10,size=(3,3))
print(b)

#float Values
c=np.random.rand(5)
d=np.random.rand(3,3)
print(c)
print(d)

#Random seed

np.random.seed(42)

a = np.random.randint(1, 100, size=5)

np.random.seed(42)

b = np.random.randint(1, 100, size=5)

print(a)
print(b)

'''Your task

Write your own code to do these four things:

1️⃣

Generate 5 random integers between 1 and 100.

2️⃣

Generate a 3 × 3 matrix of random integers between 1 and 10.

3️⃣

Generate 5 random floats between 0 and 1.

4️⃣

Demonstrate reproducibility:

seed → generate array A
same seed → generate array B

Then check whether they're equal.

💡 Useful function

For the comparison, you can investigate:

np.array_equal(a, b)

Expected:

True

Don't worry about understanding how the random number generator internally works yet.'''

e=np.random.randint(1,100,size=5)
print(e)

f=np.random.randint(1,10,size=(3,3))
print(f)

g=np.random.rand(5)
print(g)

np.random.seed(50)
m=np.random.randint(1,100,size=5)
np.random.seed(50)
n=np.random.randint(1,100,size=5)
print(m)
print(n)

print(np.array_equal(m,n))
