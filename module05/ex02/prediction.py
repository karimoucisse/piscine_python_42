import numpy as np

def simple_predict(x, theta): # y = thata1 + theta0 * x 
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    m = x.shape[0]
    # res = np.ones(m)
    # for i in range(m):
    #     res[i] = theta[0] + theta[1] * x[i]
    return theta[0] + theta[1] * x



def main():
    x = np.arange(1,6)
    # Example 1:
    theta1 = np.array([5, 0])
    print(simple_predict(x, theta1)) # Ouput: array([5., 5., 5., 5., 5.])

    # Example 2:
    theta2 = np.array([0, 1])
    print(simple_predict(x, theta2)) # Output: array([1., 2., 3., 4., 5.])

    # Example 3:
    theta3 = np.array([5, 3])
    print(simple_predict(x, theta3)) # Output: array([ 8., 11., 14., 17., 20.])

    # Example 4:
    theta4 = np.array([-3, 1])
    print(simple_predict(x, theta4)) # Output: array([-2., -1., 0., 1., 2.])

if __name__ == "__main__":
    main()
