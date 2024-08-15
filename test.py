import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)
reshape_arr = arr.reshape(-1,1)
print(reshape_arr.shape)
new_reshape_arr = reshape_arr.reshape(-1)
print(new_reshape_arr.shape)