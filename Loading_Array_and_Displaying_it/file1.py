import numpy as np
import matplotlib.pyplot as plt 

#creating ARRAY:
arr_1=np.array([[1,2,3],[4,5,6]])  
arr_2=np.random.rand(3,3)
arr_3=np.zeros((3,3))
arr_4=np.ones((3,3))

#The np.save() method in NumPy is used to save a NumPy array to a binary file in the .npy format. 
# This format is a standard way to store single NumPy arrays on disk, allowing for efficient loading and saving of numerical data.

'''
np.save("ARRAY1.npy",arr_1)
np.save("ARRAY2.npy",arr_2)
np.save("ARRAY3.npy",arr_3)
np.save("ARRAY4.npy",arr_4)
'''

#Now to load and print the array we can :

loaded_array_1=np.load("D:\One drive\OneDrive\Documents\GitHub\Python-Numpy-Course\Loading_Array_and_Displaying_it\ARRAY1.npy")  #path of the file
print("\nARRAY 1 :\n",loaded_array_1)

