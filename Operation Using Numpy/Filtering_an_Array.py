import numpy as np

#Basic Filtering :
arr_1=np.array([1,2,3,4,5,6,7,8,9,10])
print("<--------------------------------------------------------->")
print("ARRAY 1D :",arr_1)
even_arr1=arr_1[arr_1 % 2==0]   #will visit each element and check if the condition arr_1%2==0 is true or not.
print("EVEN ELEMENTS IN THE ARRAY :",even_arr1)
odd_arr1=arr_1[arr_1 % 2 != 0]  ##will visit each element and check if the condition arr_1%2!=0 is true or not.
print("ODD ELEMENTS IN THE ARRAY :",odd_arr1)

#Filtering using mask in numpy :
#In short , mask is just a varibale which stores a expression which can be executed on any array using numpy
arr_2=np.array([1,2,3,4,5,6,7,8,9,10])
print("<--------------------------------------------------------->")
mask=arr_2 % 2==0
print("EVEN ELEMENTS IN THE ARRAY :",arr_2[mask])
mask1=arr_2>5
print("ELEMENTS GREATER THAN 5 IN THE ARRAY :",arr_2[mask1])
mask2=arr_2%2!=0
print("ODD ELEMENTS IN THE ARRAY :",arr_2[mask2])


