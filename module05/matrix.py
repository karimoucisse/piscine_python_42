class Matrix:
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0]))

    # # add : only matrices of same dimensions.
    def __add__(self, other_m):
        if not isinstance(other_m, Matrix):
            raise Exception("Value is not of type Matrix")
        if self.shape != other_m.shape:
            raise Exception("Matrix are not the same shape")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] + other_m.data[i][j])
            res.append(row)
        return Matrix(res)

    __radd__ = __add__
    # # sub : only matrices of same dimensions.
    def __sub__(self, other_m): # self - other
        if not isinstance(other_m, Matrix):
            raise Exception("Value is not of type Matrix")
        if self.shape != other_m.shape:
            raise Exception("Matrix are not the same shape")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] - other_m.data[i][j])
            res.append(row)
        return Matrix(res)
    
    def __sub__(self, other_m): # other - self
        if not isinstance(other_m, Matrix):
            raise Exception("Value is not of type Matrix")
        if self.shape != other_m.shape:
            raise Exception("Matrix are not the same shape")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(other_m.data[i][j] - self.data[i][j])
            res.append(row)
        return Matrix(res)
    
    # # div : only scalars.
    def __truediv__(self, i):
        if not isinstance(i, (int, float)):
            raise Exception("Scalars is not an integer")
        if i == 0:
            raise Exception("Number can't be devided by 0")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] / i)
            res.append(row)
        return Matrix(res)
        
    def __rtruediv__(self, i):
        if not isinstance(i, (int, float)):
            raise Exception("Scalars is not an integer")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                if(self.data[i][j] == 0):
                    raise Exception("Number can't be devided by 0")
                row.append(i / self.data[i][j])
            res.append(row)
        return Matrix(res)

    
    # # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # # returns a Vector if we perform Matrix * Vector mutliplication.
    def __mul__(self, data):
        isScalars = isinstance(data, (int, float))
        isMatrix = type(self) == Matrix
        if not isScalars and not isMatrix:
            raise Exception("The value is not valide")
        isVector = isMatrix and data.shape[0] == 1 or data.shape[1] == 1
        if isMatrix and not isVector:
            if self.shape != data.shape:
                raise Exception("Matrix are not the same shape")
        if not isVector:
            res = list()
            for i in range(0, self.shape[0]):
                row = list()
                for j in range(0, self.shape[1]):
                    if isScalars:
                        row.append(self.data[i][j] * data)
                    if isMatrix:
                        row.append(self.data[i][j] * data.data[i][j])
                res.append(row)
            return Matrix(res)
        else :
            if self.shape[1] != data.shape[0]:
                raise Exception("impossible operations between matrix and vector")
            res = list()
            for i in range(0, self.shape[0]):
                row = list()
                for j in range(0, self.shape[1]):
                    row.append(self.data[i][j] * data.data[j][0])
                res.append([sum(row)])
            return Vector(res)
            
    __rmul__ = __mul__
  
    def T(self):
        res = list()
        for i in range(0, self.shape[1]):
            row = list()
            for j in range(0, self.shape[0]):
                row.append(self.data[j][i])
            res.append(row)
        return Matrix(res)
    
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)


class Vector(Matrix):
    def __init__(self, data):
        if len(data) != 1 and len(data[0]) != 1:
            raise Exception("Value is not a vector")
        super().__init__(data)

    def dot(self, v: Vector):
        if(self.shape != v.shape):
            raise Exception("Operation of different shape is not possible")
        if self.shape[1] == 1:
            res = list()
            for i in range(0, self.shape[0]):
                row = list()
                for j in range(0, self.shape[1]):
                    row.append(self.data[i][j] * v.data[i][j])
                res.append(row)
            return Vector(res)
        else:
            res = list()
            for i in range(0, self.shape[0]):
                res.append(self.data[i] * v.data[i])
            return Vector(res)
