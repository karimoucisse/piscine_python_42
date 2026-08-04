import numpy as np

def gradient(x, y, theta):
    ones_array = np.ones((x.shape[0], 1))
    x_new = np.hstack((ones_array, x))
    y_thetas = x_new.dot(theta)
    x_transpo = x_new.T
    j = x_transpo.dot(y_thetas - y) / len(x)
    return j

def main():
    x = np.array([
    [ -6, -7, -9],
    [ 13, -2, 14],
    [ -7, 14, -1],
    [ -8, -4, 6],
    [ -5, -9, 6],
    [ 1, -5, 11],
    [ 9, -11, 8]])

    y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
    theta1 = np.array([0, 3, 0.5, -6]).reshape((-1, 1))

    # Example :
    print(gradient(x, y, theta1))
    # Output:
    # array([[ -33.71428571], [ -37.35714286], [183.14285714], [-393.]])

    # Example :
    theta2 = np.array([0, 0, 0, 0]).reshape((-1, 1))
    print(gradient(x, y, theta2))
    # Output:
    # array([[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]])


if __name__ == "__main__":
    main()
