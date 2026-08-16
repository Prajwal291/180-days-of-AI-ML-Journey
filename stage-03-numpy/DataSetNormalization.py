#Part1 ===> Data Set Normalization


import numpy as np

data = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
], dtype=float)

print(data)

print(np.sum(data))

mean=np.mean(data,axis=0)

std=np.std(data,axis=0)

normalized=(data-mean)/std

print(mean)

print(std)

print(normalized)