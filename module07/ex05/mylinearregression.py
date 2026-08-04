import numpy as np

class MyLinearRegression:
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def gradient(self, x, y):
        ones_array = np.ones((x.shape[0], 1))
        x_new = np.hstack((ones_array, x))
        y_thetas = x_new.dot(self.thetas)
        x_transpo = x_new.T
        j = x_transpo.dot(y_thetas - y) / len(x)
        return j

    def fit_(self, x, y):
        thetas = self.thetas
        for i in range(self.max_iter):
            j = self.gradient(x, y)
            thetas = thetas - self.alpha * j
            self.thetas = thetas

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
        res = np.sum(self.loss_elem_(y, y_hat)) * div
        return res



def main():
    print("Hello from ex03!")


if __name__ == "__main__":
    main()
