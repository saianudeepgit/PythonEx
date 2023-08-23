import numpy as np
zeroarray = np.array(30)
zeroarray1=np.array(200)
resularray=zeroarray+zeroarray1

addarray=zeroarray+zeroarray1
subarray=zeroarray-zeroarray1
mularray=zeroarray*zeroarray1
divarray=zeroarray/zeroarray1
floordivarray=zeroarray//zeroarray1

print("the addithion of two zero array is:",addarray)
print("the subtraction of two zero array is:",subarray)
print("the multification of two zero array is:",mularray)
print("the division of two zero array is:",divarray)
print("the floar division of two zero array is:",floordivarray)

print("the resultarray dimension array dimension is:",resularray.ndim)
print("the zero dimension array is:",zeroarray)
print("the zero dimension array dimansion is:",zeroarray.ndim)
print("the number of elements in zero dimension array is:",zeroarray.size)
print("the dimension array shape is:",zeroarray.shape)


