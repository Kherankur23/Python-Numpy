import numpy as np

#THERE ARE MANY METHODS THROUGH WHICH WE CAN CREATE ARRAYS FROM SCRATCH
#FEW METHODS ARE DISCUSSED BELOW :

# 1) THE ZERO METHOD:
arr_zero=np.zeros([3,4])  #This creates a zero matrix of 3 rows and 4 coloumns
print("\nZERO MATRIX OF 3 Row and 4 Coloumn :\n",arr_zero) 

# 2) THE ONES METHOD:
arr_one=np.ones([3,4]) #This creates a singular matrix of 3 rows and 4 coloumns
print("\nSINGULAR MATRIX OF 3 Row and 4 Coloumn :\n",arr_one) 

# 3) THE CONSTANT METHOD:

arr_const=np.full((3,4),9) #This creates a matrix of 3 rows and 4 coloumns where each element is 9
print("\nMATRIX OF 3 Row and 4 Coloumn with each element as 9(constant) :\n",arr_const) 

# 4) THE RANDOM METHOD :

arr_random=np.random.random((3,4))
print("\nMATRIX OF 3 Row and 4 Coloumn With Random Element :\n",arr_random) 

# 5) THE SEQUENCE METHOD :
#        SYNTAX --->  arr_sequence=np.arange(n,n+1,step)
#               --->n= starting value, n+1=ending value ex when n=10, range=(0,9) n step=step value

arr_sequence=np.arange(0,10,2)
print("\nARRAY With Sequence :\n",arr_sequence) 


