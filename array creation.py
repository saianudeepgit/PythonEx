import numpy as np
firstarray = np.array([1,5,6])
print("the array is : \n",firstarray)
firstarray = np.arange(1,6,2)
print("The a-range function is : \n",firstarray)

onesarray = np.ones((1,3,2),dtype=int)
print("The ones array is : \n",onesarray)
zerosarray = np.zeros((3,2),dtype=float)
print("The zeros array is :\n",zerosarray)
myarray = np.linspace(5,20,20)
print("The lin-space matrix is :\n",myarray)
randomarray = np.random.random(4)
print("The random array is :\n",randomarray)
#newarray = np.random.random(2,20,8)
oneslikearray = np.ones_like((1,2,3),dtype=int)
rangearray =np.arange(2,14,5)
#rangearray[0][5]=int(20)
print("the elements of the array are of type:",rangearray.dtype)
print("the range array represents:\n",rangearray)
print("the range array size and shape are:",rangearray.size,"&&",rangearray)
myshapearray=np.reshape(rangearray,(3,1))
myshapearray[2,0]=1400
print("the reshaped array from 1*6 to 2*3:\n",myshapearray)
print("the ones like array is:",oneslikearray)
print("the dimension of random array is:",randomarray.ndim)
print("the random generated array:",randomarray)
print("the array created with linspace:",myarray)
print("the created array had elements of size:",myarray.size)

print("my first zeroarray:\n",zerosarray)
print("the ones array is:\n",zerosarray)
print("the ones array dimension is:",zerosarray.ndim)
print("the shape of the ones array is:",zerosarray.shape)
print("my first array:\n",firstarray)
print("the ones array is:\n",onesarray)
print("the ones array dimension is :",onesarray.ndim)
print("the shape of the ones array is:",onesarray.shape)
sortedarray = np.sort(randomarray)
print("the sorted random array is :",sortedarray)



