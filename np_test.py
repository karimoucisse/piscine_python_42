import numpy as np
from numpy import dtype

v1 = range(10)
print(list(v1))
# ndim => get dimension
# [row_index, column_index] => to get a specific index
# [row_index, :] get a row
# [:, column_index] get a column

# ([1, 2, 3 ,4, 5, 6, 7] , [8, 9,10, 11, 12, 13, 14])
# [starIndex:EndIndex:Stepsize] [0, 1:6:2] => 2, 4, 6

# np.zeros(5) => [0., 0., 0., 0., 0.]
# np.ones(5, dtype("int32")) => [1., 1., 1., 1., 1.]
# np.full(5, 99) => [99 99 99 99 99]
# np.random.rand(row, col) => float
# np.random.randint(min, max, size=(row, col)) => int
# np.random.random_sample(a.shape) => random from a shape
# np.repeat() => repeat an array
# a.astype("int32")  => convert


# Create an array with 3 integers, starting from the default integer 0.
# b = np.arange(3)
# Create an array that starts from the integer 1, ends at 20, incremented by 3.
# np.arange(1, 20, 3)
# Return a new array of shape 3, without initializing entries.
# empt_arr = np.empty(3)
# lin_spaced_arr = np.linspace(0, 100, 5)

# Multidimensional array using reshape()
# multi_dim_arr = np.reshape(
#                 one_dim_arr, # the array to be reshaped
#                (2,3) # dimensions of the new array
#               )

# Dimension of the 2-D array multi_dim_arr
# multi_dim_arr.ndim

# Shape of the 2-D array multi_dim_arr
# Returns shape of 2 rows and 3 columns
# multi_dim_arr.shape

# Size of the array multi_dim_arr
# Returns total number of elements
# multi_dim_arr.size
# Stack the arrays vertically
# vert_stack = np.vstack((a1, a2))
# Stack the arrays horizontally
# horz_stack = np.hstack((a1, a2))
# x = np.linalg.solve(A, b)
# d = np.linalg.det(A)
# np.linalg.inv(A)
# np.linalg.pinv(A)
# np.mean(a)
# np.sum(a, axis=0)
# np.std(a)
# np.max(a) and np.min(a)
# np.c_[A, B]
# np.r_[A, B]
# np.where(condition, x, y)

# a.T (attribut) : Transpose la matrice (inverse les lignes et les colonnes, $X^T$).

# a multiplication between two matrix can be done if shape n are the same:
    # shape(m, n) * shape(n, o) = shape(m, o)
