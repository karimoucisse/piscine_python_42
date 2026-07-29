import matplotlib.pyplot as plt
import numpy as np

def plot_with_loss(x, y, theta):
    one_array = np.ones((x.shape[0], 1))
    x_2d = x.reshape(x.shape[0], 1)
    x_2d = np.hstack((one_array, x_2d))

    y_hat = x_2d.dot(theta)
    div = 1/(2*len(x))
    j =  sum(div * pow(y_hat - y,2)) * 2
    j_string = f"cost : {j:.6f}"
    
    plt.scatter(x,y)
    plt.plot(x, y_hat)
    plt.vlines(x, y, y_hat, linestyles ="dashed", colors ="r")
    plt.title(j_string)
    plt.show()
    


def main():
    x= np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    # Example 1:
    theta1= np.array([18,-1])
    plot_with_loss(x, y, theta1)

    # # Example 2:
    # theta2 = np.array([14, 0])
    # plot_with_loss(x, y, theta2)

    # # Example 3:
    # theta3 = np.array([12, 0.8])
    # plot_with_loss(x, y, theta3)


if __name__ == "__main__":
    main()
