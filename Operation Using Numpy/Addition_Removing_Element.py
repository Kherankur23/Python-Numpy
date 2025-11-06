import numpy as np

arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
arr_3=np.array([[1,2,3],[3,4,6]])
arr_4=np.array([90,42,12,423,1231])
print("ARRAY 1 :",arr_1)
print("ARRAY 2 :",arr_2)
print("ARRAY 3 :",arr_3)
print("ARRAY 4 :",arr_4)
addition_of_two_array=arr_1+arr_2  #adds each and every element.
print("ARRAY 1 + ARRAY 2(addition of each element) :\n",addition_of_two_array)

combination_of_two_array=np.concatenate((arr_1,arr_2)) #creates a combined array containing all the elements
print("ARRAY 1 + ARRAY 2 AS A COMBINED ARAAY  :\n",combination_of_two_array)

new_row=np.array([7,8,9])
with_new_row=np.vstack((arr_1,new_row)) #vstack() allows us to add new row into an array
print("ADDITION OF A ROW IN THE ARRAY 1 :\n",with_new_row)

new_coloumn=np.array([[8],[7]]) 
with_new_col=np.hstack((arr_3,new_coloumn))  #hstack() allows us to add new coloumn into the array
print("ADDITION OF A COLOUMN IN THE ARRAY 3 :\n",with_new_col)

#To delete an array we can :
deleted_element=np.delete(arr_4,2)  # ---> THIS WILL DELETE THE ELEMENT PRESENT AT THE 2ND INDEX OF ARRAY 4
print("THE DELETED ELEMENT AT THE INDEX 2 OF ARRAY 4 IS :",deleted_element)

