import numpy as np


output = np.ones((5,5))
print(output)

print("**************************************************")

r = output[1:4,1:4]
#print(r)

zeros = np.zeros((3,3))
zeros[1 ,1] = 9
#print(zeros)


output[1:4,1:4] = zeros

print(output)
