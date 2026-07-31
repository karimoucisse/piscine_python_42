import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def mse_(y, y_hat):
    inv_m = 1/len(y)
    y_pow_n_diff = (y_hat - y) ** 2 
    res = inv_m * y_pow_n_diff
    return (np.sum(res))

def main():
    data = pd.read_csv("are_blue_pills_magics.csv")
    Xpill = np.array(data['Micrograms']).reshape(-1,1)
    Yscore = np.array(data['Score']).reshape(-1,1)
    linear_model1 = MyLR(np.array([[89.0], [-8]]))
    linear_model2 = MyLR(np.array([[89.0], [-6]]))
    Y_model1 = linear_model1.predict_(Xpill)

    Y_model2 = linear_model2.predict_(Xpill)
    # plt.plot(Xpill, Y_model1, linestyle="dotted", color='g')
    # plt.scatter(Xpill, Yscore)
    # plt.scatter(Xpill, Y_model1, color='g')
    # plt.show()
    

    # print(mse_(Yscore, Y_model1))
    # # 57.60304285714282
    # print(mean_squared_error(Yscore, Y_model1))
    # # # 57.603042857142825
    # print(mse_(Yscore, Y_model2))
    # # # 232.16344285714285
    # print(mean_squared_error(Yscore, Y_model2))
    # # 232.16344285714285



if __name__ == "__main__":
    main()
