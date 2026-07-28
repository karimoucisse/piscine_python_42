import numpy as np

def add_intercept(x):
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    ones_list = np.ones((x.shape[0], 1))
    res = np.hstack((ones_list,x))
    return res

def predict_(x, theta):
   
    new_x = add_intercept(x)
    return new_x.dot(theta)
    # res = np.ones((x.shape[0], 1))
    # for i in range(x.shape[0]):
    #     res[i] = theta[0] * new_x[i][0] + theta[1] * new_x[i][1]
    # return res 

def main():
    x = np.arange(1,6)
    theta1 = np.array([[5], [0]])
    print(predict_(x, theta1))
    # Ouput:
    # array([[5.], [5.], [5.], [5.], [5.]])

    # Example 2:
    theta2 = np.array([[0], [1]])
    print(predict_(x, theta2))
    # Output:
    # array([[1.], [2.], [3.], [4.], [5.]])

    # Example 3:
    theta3 = np.array([[5], [3]])
    print(predict_(x, theta3))
    # Output:
    # array([[ 8.], [11.], [14.], [17.], [20.]])

    # Example 4:
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))
    # Output:
    # array([[-2.], [-1.], [ 0.], [ 1.], [ 2.]])



if __name__ == "__main__":
    main()
