import numpy as np

a = np.ones((2,3))
print(a)

b = np.full((3,2) , 2)
print(b)

#min value
arre = np.array([1,2,3,6])
print(np.min(arre))

#maximun value
print(np.max(arre))


#matrix multiplcation
print(np.matmul(a,b))

#mean
arr = np.array([1,2,3])
print(np.mean(arr))

#median
arrb = np.array([1,2,3,4,5,7])
print(np.median(arrb))
