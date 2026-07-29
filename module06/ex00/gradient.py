import numpy as np


def prevision(x, theta):
    ones_array = np.ones((x.shape[0], 1))
    new_x = np.hstack((ones_array, x))
    y_hat = new_x.dot(theta)
    return y_hat
def simple_gradient(x, y, theta):
    y_hat = prevision(x, theta)
    _m = 1/len(x)
    j = _m * (y_hat - y)
    j1 = _m * (y_hat - y) * x
    print(np.array([np.sum(j), np.sum(j1)]))
def main():
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
    # Example 0:
    theta1 = np.array([2, 0.7]).reshape((-1, 1))
    simple_gradient(x, y, theta1)
    # Output:
    # array([[-19.0342574], [-586.66875564]])

    # Example 1:
    theta2 = np.array([1, -0.4]).reshape((-1, 1))
    simple_gradient(x, y, theta2)
    # Output:
    # array([[-57.86823748], [-2230.12297889]])


if __name__ == "__main__":
    main()
