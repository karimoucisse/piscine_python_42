import numpy as np

def predict_(x, theta):
    ones_array = np.ones((x.shape[0], 1))
    new_x = np.hstack((ones_array, x))
    return new_x.dot(theta)

def gradient(x, y, theta):
    ones_array = np.ones((x.shape[0], 1))
    x_new = np.hstack((ones_array, x))
    y_thetas = x_new.dot(theta)
    x_transpo = x_new.T
    j = x_transpo.dot(y_thetas - y) / len(x)
    return j

def fit_(x, y, theta, alpha, max_iter):
    for i in range(max_iter):
        j = gradient(x, y, theta)
        theta = theta - alpha * j
    return theta

def main():
    x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
    theta = np.array([[42.], [1.], [1.], [1.]])

    # Example 0:
    theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
    print(theta2)
    # Output:
    # array([[41.99..],[0.97..], [0.77..], [-1.20..]])

    # Example 1:
    print(predict_(x, theta2))
    # Output:
    # array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])


if __name__ == "__main__":
    main()
