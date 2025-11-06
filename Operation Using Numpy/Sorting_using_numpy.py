import numpy as np

arr_1D=np.array([3,4,5,6,1,2,8,9,7,10])
print("UNSORTED 1D-ARRAY :",arr_1D)
print("SORTED 1D-ARRAY :",np.sort(arr_1D))  #basic sort for one dimensional array
print("<------------------------------------------------>\n")

arr_2D=np.array([[3,1],[1,2],[2,3]])
print("UNSORTED 2D-ARRAY :",arr_2D)
print("SORTED 2D-ARRAY WITH RESPECT TO COLOUMN:",np.sort(arr_2D, axis=0))
print("SORTED 2D-ARRAY WITH RESPECT TO ROW:",np.sort(arr_2D, axis=1))


