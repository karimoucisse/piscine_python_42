import matplotlib.pyplot as plt
import numpy as np

def add_intercept(x):
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    ones_list = np.ones((x.shape[0], 1))
    res = np.hstack((ones_list,x))
    return res

def predict_(x, theta):
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    new_x = add_intercept(x)
    return new_x.dot(theta)
def plot(x, y, theta):
   y_prev = predict_(x, theta)
   plt.plot(x, y_prev)
   plt.scatter(x,y)
   plt.show()



def main():
    x = np.arange(1,6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

    # # Example 1:
    # theta1 = np.array([[4.5],[-0.2]])
    # plot(x, y, theta1)

    # # Example 2:
    # theta2 = np.array([[-1.5],[2]])
    # plot(x, y, theta2)

    # # Example 3:
    # theta3 = np.array([[3],[0.3]])
    # plot(x, y, theta3)


if __name__ == "__main__":
    main()
