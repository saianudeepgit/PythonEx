import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("the array is:\n",array)
identitymatrix = np.eye(3,dtype=int)
print("the identity matrix is:\n",identitymatrix)
add = array + identitymatrix
print("the addition of the resulted array:",add)
multiplication = array * identitymatrix
print("the multiplication of the resulted array:",multiplication)
onesmatrix=np.ones((3,3),dtype=int)
print("the ones matrix is:",onesmatrix)
add2 = array + onesmatrix
print("addition of the next two matrices is:",add2)
multiplication2 = array * onesmatrix
print("multiplication of the new matrices is:",multiplication2)