import numpy as np

class MyLinearRegression:
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def gradient(self, x, y):
        _m = 1/len(x)
        ones_array = np.ones((x.shape[0], 1))
        x1 = np.hstack((ones_array, x))
        y_theta = x1.dot(self.thetas)
        x1_t = x1.T

        a = _m * x1_t
        b = y_theta - y
        return (a.dot(b))

    def fit_(self, x, y):
        for i in range(self.max_iter):
            g = self.gradient(x, y)
            t0 = self.thetas[0] - self.alpha * g[0]
            t1 = self.thetas[1] - self.alpha * g[1]
            self.thetas = np.array([t0, t1]).reshape((-1, 1))

    def predict_(self, x):
        ones_array = np.ones((x.shape[0], 1))
        x1 = np.hstack((ones_array, x))
        return (x1.dot(self.thetas))

    def loss_elem_(self, y, y_hat):
        if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
            return None
        if y.size == 0 or y_hat.size == 0:
            return None
        loss_array = pow(y_hat - y, 2)
        return loss_array

    def loss_(self, y, y_hat):
        if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
            return None
        if y.size == 0 or y_hat.size == 0:
            return None
        div = 1/(2*y.shape[0])
        res = sum(self.loss_elem_(y, y_hat))[0] * div
        return res



def main():
    print("Hello from ex03!")


if __name__ == "__main__":
    main()
