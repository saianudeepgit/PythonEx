import numpy as np
array = np.array([[1,2,3,4],[2,3,5,6],[6,7,2,9]])

unique_valuse,count = np.unique(array,return_counts=True)
unique_val_list=unique_valuse[count==1]
print("the different values are:",unique_val_list)