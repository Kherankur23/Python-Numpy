import numpy as np
import time

#List in python V/S array in Numpy:

list_py=[1,2,3,4,5,6,7]
print("LIST MULTIPLIED BY 2 IS :",list_py*2)  #Creates a list having each element Twice
np_array=np.array([1,2,3,4])   
print("ARRAY MULTIPLIED BY 2 IS :",np_array*2)   #Element Wise Multiplication

start=time.time()
list_py=[i*2 for i in range(1000000)]
print("\n List operation time taken :",time.time()-start,"sec")

start=time.time()
np_array=np.arange(1000000)*2
print("\n Numpy operation time taken :",time.time()-start,"sec")



