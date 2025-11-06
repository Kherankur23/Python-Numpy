import numpy as np

arr_1=np.arange(12)   #creates an array having numbers from 0 to 12(12 not included).
print("\n Original ARRAY :",arr_1)

r1=arr_1.reshape((3,4))  #converts the array into a 3 row and 4 coloumn matrix
print("\n Resized ARRAY :",r1)

f1=r1.flatten()  #converts the matrix into a single row array
print("\n Flattened Matrix :",f1)  #back to original form

raveled=f1.ravel() #ravel() --> returns the view of the array instead of a copy
print("\n Raveled ARRAY :",raveled)

transpose=r1.T    #.T --> returns the transpose of a given matrix.
print("\n Transpose of a given Matrix :",transpose)