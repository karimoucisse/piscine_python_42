import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("spacecraft_data.csv")

    # X = np.array(data[['Age']])
    # Y = np.array(data[['Sell_price']])
    # myLR_age = MyLR(thetas = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 1000000)
    # myLR_age.fit_(X, Y)
    # y_pred = myLR_age.predict_(X)

    # X = np.array(data[['Thrust_power']])
    # myLR_thrust = MyLR(thetas = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 1000000)
    # myLR_thrust.fit_(X, Y)
    # y_pred = myLR_thrust.predict_(X)

    # X = np.array(data[['Terameters']])
    # myLR_distance = MyLR(thetas = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 1600000)
    # myLR_distance.fit_(X, Y)
    # y_pred = myLR_distance.predict_(X)

    # plt.scatter(X, Y, label='Sell price')
    # plt.scatter(X, y_pred, label='Predicted sell price')
    # plt.ylabel('y: sell price (in keuros)')
    # plt.xlabel('x1: age (in years)')
    # plt.grid()
    # plt.legend()
    # plt.show()

    X = np.array(data[['Age','Thrust_power','Terameters']])
    Y = np.array(data[['Sell_price']])
    age = np.array(data[['Age']])
    thrust = np.array(data[['Thrust_power']])
    terameters = np.array(data[['Terameters']])
    my_lreg = MyLR(thetas=[[1.0], [1.0], [1.0], [1.0]], alpha=9e-5, max_iter=500000)

    # # # Example 0:
    # print(my_lreg.mse_(Y, my_lreg.predict_(X)))
    # # # Output:
    # # # 144044.877...

    # # Example 1:
    my_lreg.fit_(X, Y)
    print(my_lreg.thetas)
    y_pred = my_lreg.predict_(X)
    print(y_pred)
    # # Output:
    # # array([[367.28849...]
    # # [-23.69939...]
    # # [ 5.73622...]
    # # [ -2.63855...]])

    # # Example 2:
    # print(my_lreg.mse_(Y, my_lreg.predict_(X)))
    # # Output:
    # # 435.9325695...

    plt.scatter(terameters, Y, label='Sell price')
    plt.scatter(terameters, y_pred, label='Predicted sell price')
    plt.show()




if __name__ == "__main__":
    main()
