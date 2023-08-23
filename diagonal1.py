import numpy as np

square_matrix = np.array([[1,2,3],[5,6,7],[9,10,11]])
np.fill_diagonal(square_matrix,1)
print(square_matrix)