import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

# def mse_(y, y_hat):
#     inv_m = 1/len(y)
#     y_pow_n_diff = (y_hat - y) ** 2
#     res = inv_m * y_pow_n_diff
#     return (np.sum(res))


def loss_elem_(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    loss_array = pow(y_hat - y, 2)
    return loss_array

def loss_(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    div = 1/(2*y.shape[0])
    res = loss_elem_(y, y_hat) * div
    return res

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

    # print(linear_model1.mse_(Yscore, Y_model1))
    # # 57.60304285714282
    # print(mean_squared_error(Yscore, Y_model1))
    # # # 57.603042857142825
    # print(linear_model1.mse_(Yscore, Y_model2))
    # # # 232.16344285714285
    # print(mean_squared_error(Yscore, Y_model2))
    # # 232.16344285714285


    # linear_model = MyLR(np.array([[1.0], [1.0]]))  # init quelconque
    # linear_model.fit_(Xpill, Yscore)
    # theta0_opt = float(linear_model.thetas[0][0])
    # theta1_opt = float(linear_model.thetas[1][0])
    # q1 = np.linspace(theta1_opt - 20, theta1_opt + 20, 1000)
    # q0 = np.linspace(theta0_opt - 10, theta0_opt + 10, 6)

    # for x in q0:
    #     test = []
    #     for n in q1:
    #         m = MyLR(np.array([[x], [n]]))
    #         Y_model = m.predict_(Xpill)
    #         loss = m.mse_(Yscore, Y_model)
    #         test.append(float(loss))
    #     plt.plot(q1, test, label=f'θ0 = {x:.1f}')
    # plt.show()



if __name__ == "__main__":
    main()
