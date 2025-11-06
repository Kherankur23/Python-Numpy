import numpy as np
#Array Compatibility is the most imp part as its plays a major role on performing operations on array
#It allows us to check if the given two array are of the same size or not by which we can perform further operations
#Lets take an example :
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9,10])
d=np.array([10,11,12,13])
print("ARRAY 1 :",a)
print("\n")
print("ARRAY 2 :",b)
print("\n")
print("ARRAY 3 :",c)
print("\n")
print("ARRAY 4 :",d)
print("\n")
print("ARRAY 1 AND ARRAY 2 ARE COMPAIBLE OR NOT ? - ",a.size == b.size)
print("ARRAY 1 AND ARRAY 3 ARE COMPATIBLE OR NOT ? - ",a.size == c.size)
print("ARRAY 1 AND ARRAY 4 ARE COMPAIBLE OR NOT ? - ",a.size == d.size)
print("ARRAY 2 AND ARRAY 3 ARE COMPAIBLE OR NOT ? - ",b.size == c.size)
print("ARRAY 2 AND ARRAY 4 ARE COMPATIBLE OR NOT ? - ",b.size == d.size)
print("ARRAY 3 AND ARRAY 4 ARE COMPAIBLE OR NOT ? - ",c.size == d.size)


