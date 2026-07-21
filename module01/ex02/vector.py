
class Vector:

    def __init__(self, values):
        row = len(values)
        col = len(values[0])
        self.values = values
        self.shape = (row, col)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)

    def dot (self, other):
        res = list()
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(self.values[0][i] * other.values[0][i])
        else:
            for i in range(len(self.values)):
                res.append(self.values[i][0] * other.values[i][0])
        return sum(res)

    def T(self):
        res = list()

        if self.shape[0] == 1:
            for i in self.values[0]:
                res.append([i])
        else:
            for i in self.values:
                res.append(i[0])
        self.shape = (self.shape[1], self.shape[0])
        return res


    def __add__(self, other):
        res = list()
        if self.shape != other.shape:
            return NotImplemented
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(self.values[0][i] + other.values[0][i])
        else:
            for i in range(len(self.values)):
                res.append(self.values[i][0] + other.values[i][0])
        return res
    __radd__ = __add__

    def __sub__(self, other):
        res = list()
        if self.shape != other.shape:
            return NotImplemented
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(self.values[0][i] - other.values[0][i])
        else:
            for i in range(len(self.values)):
                res.append(self.values[i][0] - other.values[i][0])
        return res

    def __rsub__(self, other):
        res = list()
        if self.shape != other.shape:
            return NotImplemented
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(other.values[0][i] - self.values[0][i])
        else:
            for i in range(len(self.values)):
                res.append(other.values[i][0] - self.values[i][0])
        return res

    def __truediv__(self, num):
        assert num != 0, "division by zero."
        res = list()
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(self.values[0][i] / num)
        else:
            for i in range(len(self.values)):
                res.append(self.values[i][0] / num)
        return res

    def __rtruediv__(self, num):
        res = list()
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                assert self.values[0][i] != 0, "division by zero."
                res.append(num / self.values[0][i])
        else:
            for i in range(len(self.values)):
                assert self.values[i][0] != 0, "division by zero."
                res.append(num / self.values[i][0])
        return res

    def __mul__(self, num):
        res = list()
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                res.append(self.values[0][i] * num)
        else:
            for i in range(len(self.values)):
                res.append(self.values[i][0] * num)
        return res
    __rmul__ = __mul__

