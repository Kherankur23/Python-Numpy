import numpy as np

arr_1D=np.array([1,2,3,4,5,6,7,8,9,10])  #THIS IS A 1D ARRAY

#Basic Slicing : sytax --> arr_1[start index:ending index:step value]
print("<----------------------------------------------------------------->")
print("\n 1D ARRAY:",arr_1D)
print("\n Basic Slicing from index 2 to 7 :",arr_1D[2:7])
print("\n Basic Slicing from index 2 to 7 with step value as 2 :",arr_1D[2:7:2])
print("\n Basic Slicing using Negative Indexing :",arr_1D[-8:-3])
print("\n Basic Slicing using Negative Indexing with step value as 2 :",arr_1D[-8:-3:2])


#Slicing and Indexing in 2D array:
            #    [0,1,2]   ---> Coloumn Number
arr_2D=np.array([[1,2,3],  #---> ROW = 0 WITH INDEXING AS [0,1,2] for the respective element which is present
                 [4,5,6],  #---> ROW = 1 WITH INDEXING AS [0,1,2] for the respective element which is present
                 [7,8,9]]) #--> ROWV= 2  WITH INDEXING AS [0,1,2] for the respective element which is present
print("\n<----------------------------------------------------------------->")
print("\n 2D ARRAY:",arr_2D)
print("ACCESSING SPECIFIC ELEMENT (1st Row and Second Element) :",arr_2D[1,2])   #will return the element that is present in the first row and is the 2nd element 
print("Accessing and printing a entire row :",arr_2D[1]) #will return entire ROW 1
print("Accessing and printing a entire coloumn :",arr_2D[:,2]) #will return entire coloumn 2


