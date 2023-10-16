import numpy as np
#Generate the matrix
array=np.arange(1,26).reshape(5,5)
print(array)
#slicing
print(array[2:5,1:5])
print(array[0:3,1].reshape(3,1))
#sum
print(array.sum())
#sum of rows
print(array.sum(axis=0))
#sum of columns
print(array.sum(axis=1))