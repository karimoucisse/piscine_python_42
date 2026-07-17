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
