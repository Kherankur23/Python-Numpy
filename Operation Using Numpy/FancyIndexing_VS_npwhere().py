# FANCY INDEXING V/S np.where() clause:

import numpy as np


#Fancy Indexing :
arr_1=np.array([1,2,3,4,5,6,7,8,9,10])
indices=[0,1,3,5,2]
print("ARRAY 1:",arr_1)
print("THE ELEMENTS PRESENT ON THE INDICES [0,1,3,5,2] ARE using fancy indexing :",arr_1[indices])


#where() clause :
arr_2=np.array([1,2,3,4,5,6,7,8,9,10])
print("<------------------------------------------------------------------------------------>")
print(" ARRAY 2:",arr_2)
where_condition=np.where(arr_2>5)
print("ARRAY WHERE ELEMENTS ARE GREATER THAN 5 ARE using where() clause :",arr_2[where_condition])


#Using the where() clause to create any array which satisfy the given condition :

arr_3=np.array([1,2,3,4,5,6,7,8,9,10])
print("<------------------------------------------------------------------------------------>")
print("ARRAY 3 :",arr_3)
condition1=np.where(arr_3>5,arr_3*5,arr_3)
#THE ABOVE LINE IS EQUIVALENT TO THE GIVEN CODE :
 #     if (arr_3>5):    -->If the number in the array is greater than 5 then:
 #        arr_3*5       --> Multiply the number by 5
 #     else:            -->If not then just return the number as usual
 #       arr_3
print("THE ARRAY WHICH THE CONDITION BECOMES :",condition1)



arr_4=np.array([1,2,3,4,5,6,7,8,9,10])
print("<------------------------------------------------------------------------------------>")
print("ARRAY 4 :",arr_4)
condition2=np.where(arr_4>5,"True","False")
#THE ABOVE LINE IS EQUIVALENT TO THE GIVEN CODE :
 #     if (arr_3>5):    -->If the number in the array is greater than 5 then:
 #        arr_3*5       --> The number is True
 #     else:            -->If not then the number in the array is false
 #       arr_3
print("THE ARRAY WHICH THE CONDITION BECOMES :",condition2)