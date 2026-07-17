import numpy as np

class Vector:

    def __init__(self, values):
        self.values = np.array(values)
        self.shape = np.shape(values)

    # def .dot (self):

    # def .T(self):

    def __mul__(self, other):
        if isinstance(other, int):
            return self.values * other

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.values / other
