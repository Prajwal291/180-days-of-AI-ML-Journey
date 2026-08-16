#vectorized operations

import numpy as np

arr1=np.array([10,20,30,40,50])
print(arr1)
print(arr1*2)
print(arr1+10)
print(arr1-10)
print(arr1/10)
print(arr1%10)
print(arr1//10)

arr2=np.array([60,70,80,90,100])
print(arr2)
print(arr1+arr2)
print(arr2-arr1)
print(arr1*arr2)
print(arr1/arr2)
print(arr1//arr2)
print(arr1%arr2)

'''our task

Create:

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

Without using any loops, calculate:

a + b
a - b
a * b
a / b
a ** 2
Every element of a multiplied by 10
🔥 Bonus

Calculate the average of a without using a loop.

Hint:

np.________(a)'''

a=np.array([10,20,30,40,50])
b=np.array([1,2,3,4,5])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)
print(a*10)

print(np.average(a))
print(np.sum(a)/len(a))
print(np.mean(a))