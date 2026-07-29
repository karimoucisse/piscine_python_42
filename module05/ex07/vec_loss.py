import numpy as np


def loss_(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    div = 1/(2*len(y))
    res = sum(pow(y_hat - y, 2) * div)
    return res



def main():
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    # Example 1:
    print(loss_(X, Y))
    # Output:
    # 2.142857142857143

    # Example 2:
    print(loss_(X, X))
    # Output:
    # 0.0


if __name__ == "__main__":
    main()
