import numpy as np

def add_intercept(x):
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    ones_list = np.ones((x.shape[0], 1))
    res = np.hstack((ones_list,x))
    return res
    

def main():
    # Example 1:
    x = np.arange(1,6)
    print(add_intercept(x), "\n")
    # Output:
    # array([[1., 1.],
    # [1., 2.],
    # [1., 3.],
    # [1., 4.],
    # [1., 5.]])
    
    # Example 2:
    y = np.arange(1,10).reshape((3,3))
    print(add_intercept(y))
    # Output:
    # array([[1., 1., 2., 3.],
    # [1., 4., 5., 6.],
    # [1., 7., 8., 9.]])


if __name__ == "__main__":
    main()
