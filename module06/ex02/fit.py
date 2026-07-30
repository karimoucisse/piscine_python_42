import numpy as np

def predict(x, theta1):
    ones_array = np.ones((x.shape[0], 1))
    x1 = np.hstack((ones_array, x))
    return (x1.dot(theta1))

def gradient(x, y, theta):
    _m = 1/len(x)
    ones_array = np.ones((x.shape[0], 1))
    x1 = np.hstack((ones_array, x))
    y_theta = x1.dot(theta)
    x1_t = x1.T

    a = _m * x1_t
    b = y_theta - y
    return (a.dot(b))

def fit_(x, y, theta, alpha, max_iter):
    for i in range(max_iter):
        g = gradient(x, y, theta)
        t0 = theta[0] - alpha * g[0]
        t1 = theta[1] - alpha * g[1]
        theta = np.array([t0, t1]).reshape((-1, 1))
    return theta

def main():
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    theta= np.array([1, 1]).reshape((-1, 1))

    # Example 0:
    theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
    # print(theta1)
    # Output:
    # array([[1.40709365],
    # [1.1150909 ]])

    # Example 1:
    print(predict(x, theta1))
    # Output:
    # array([[15.3408728 ],
    # [25.38243697],
    # [36.59126492],
    # [55.95130097],
    # [65.53471499]])


if __name__ == "__main__":
    main()
