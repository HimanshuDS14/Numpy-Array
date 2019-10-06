import numpy as np



arr1 = np.ones((5,5))


count = 1
for i in range(0,5):
    for j in range(0,5):
       arr1[i , j] = count
       count = count+1

print(arr1)