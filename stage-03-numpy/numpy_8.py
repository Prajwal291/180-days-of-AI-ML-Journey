import numpy as np

'''data=([[10,20,30],
       [40,50,60],
       [70,80,90]])

print(np.sum(data))
print(np.mean(data))
print(np.max(sum))

print(np.sum(data,axis=0))
print(np.sum(data,axis=1))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))'''

'''Your final NumPy exercise

Create:

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

Calculate:

1.

Total sum

np.sum(data)
2.

Mean of all elements

np.mean(data)
3.

Sum of each column

Use axis=...

Expected:

[120 150 180]
4.

Sum of each row

Expected:

[60 150 240]
5. 🔥 Bonus

Find the mean of each column.

Expected:

[40. 50. 60.]
6. 🔥 Bonus

Find the maximum value of each row.

Expected:

[30 60 90]

Use NumPy—no loops.'''

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#1
print(np.sum(data))
#2
print(np.mean(data))
#3
print(np.sum(data,axis=0))
#4
print(np.sum(data,axis=1))
#5
print(np.mean(data,axis=0))
#6
print(np.max(data,axis=1))