import numpy as np

def add_intercept(x):
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    ones_list = np.ones((x.shape[0], 1))
    res = np.hstack((ones_list,x))
    return res

def predict_(x, theta):
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    new_x = add_intercept(x)
    return new_x.dot(theta)


def loss_elem_(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    loss_array = np.ones((y.shape[0], 1))
    for i in range(y.shape[0]):
        loss_array[i] = pow(y_hat[i] - y[i], 2)
    return loss_array

def loss_(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    div = 1/(2*y.shape[0])
    res = sum(loss_elem_(y, y_hat))[0] * div
    return res

def main():
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

    # Example 1:
    print(loss_elem_(y1, y_hat1))
    # Output:
    # array([[0.], [1], [4], [9], [16]])

    # Example 2:
    print(loss_(y1, y_hat1))
    # Output:
    # 3.

    x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
    theta2 = np.array(np.array([[0.], [1.]]))
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)

    # Example 3:
    print(loss_(y2, y_hat2))
    # Output:
    # 2.142857142857143

    # Example 4:
    print(loss_(y2, y2))
    # Output:
    # 0.0


if __name__ == "__main__":
    main()
