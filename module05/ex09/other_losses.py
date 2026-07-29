import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

def mse_(y, y_hat):
    inv_m = 1/len(y)
    y_pow_n_diff = pow(y_hat - y, 2) 
    res = inv_m * y_pow_n_diff
    return (np.sum(res))

def rmse_(y, y_hat):
    return sqrt(mse_(y, y_hat))

def mae_(y, y_hat):
    inv_m = 1/len(y)
    y_diff = np.sum(abs(y_hat - y))
    res = inv_m * y_diff
    return (res)

def r2score_(y, y_hat):
    n = np.sum(pow(y_hat - y, 2))
    d = np.sum(pow(y - np.mean(y), 2))
    return  float(1 - n / d)

def main():
    # Example 1:
    x = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
    y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
    # x = np.array([[1], [2], [3]])
    # y = np.array([[1.2], [1.9], [2.9]])

    # Mean-squared-error
    # your implementation
    print(mse_(x,y))
    # Output:
    # 4.285714285714286

    ## sklearn implementation
    print(mean_squared_error(x,y))
    ## Output:
    # 4.285714285714286

    # Root mean-squared-error
    # your implementation
    print(rmse_(x,y))
    # Output:
    # 2.0701966780270626

    ## sklearn implementation not available: take the square root of MSE
    print(sqrt(mean_squared_error(x,y)))
    ## Output:
    # 2.0701966780270626

    # Mean absolute error
    # your implementation
    print(mae_(x,y))
    # Output:
    # 1.7142857142857142

    ## sklearn implementation
    print(mean_absolute_error(x,y))
    # Output:
    # 1.7142857142857142
    
    # R2-score
    ## your implementation
    print(r2score_(x,y))
    ## Output:
    # 0.9681721733858745

    # ## sklearn implementation
    print(r2_score(x,y))
    # ## Output:
    # # 0.9681721733858745


if __name__ == "__main__":
    main()
