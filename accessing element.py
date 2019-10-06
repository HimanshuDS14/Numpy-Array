import numpy as np


a = np.array([[1,2,3,4,5,6,7] , [8,9,10,11,12,13,14]])

print(a)

#Accessing specific element[row,column]
print(a[1,3])

#get specific row
print(a[1,:])

#get specific column
print(a[:,3])


#change element
a[1,2] = 32
print(a)


