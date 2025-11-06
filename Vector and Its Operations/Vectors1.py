import numpy as np
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

#Vector Addition
print("Vector addition: ", vector1 + vector2)

#Vector Multiplication
print("\n Multiplication vector", vector1 * vector2)

#Vector Dot product
print("\nDot Product :", np.dot(vector1, vector2))

#Angle between two vectors
angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)

#lets take another example :
#Making the element(string) in an array in UpperCase
restraunt_types=np.array(['Biryani','chinese','pizza','Burger'])
vecrized_operation=np.vectorize(str.upper)
print("\nVectorized UpperCase Array :\n",vecrized_operation(restraunt_types))