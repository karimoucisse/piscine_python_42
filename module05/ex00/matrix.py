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
    
    def __rsub__(self, other_m): # other - self
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
    def __truediv__(self, val):
        if not isinstance(val, (int, float)):
            raise Exception("Scalars is not an integer")
        if val == 0:
            raise Exception("Number can't be devided by 0")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] / val)
            res.append(row)
        return Matrix(res)

        
    def __rtruediv__(self, val): # raise exception
        if not isinstance(val, (int, float)):
            raise Exception("Scalars is not an integer")
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                if self.data[i][j] == 0:
                    raise Exception("Number can't be devided by 0")
                row.append(val / self.data[i][j])
            res.append(row)
        return Matrix(res)


    
    # # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # # returns a Vector if we perform Matrix * Vector mutliplication.
    def mul_matrix_vector(self, v):
        res = list()
        for i in range(0, self.shape[0]):
            row = list()
            for j in range(0, self.shape[1]):
                row.append(self.data[i][j] * v.data[j][0])
            res.append(sum(row))
        return res
        # return [[self.data[i][j] + v.data[j][0] for i in range(self.shape[0])]
        #         for j in range(self.shape[1])]
    
    def __mul__(self, data):
        isScalars = isinstance(data, (int, float))
        isMatrix = type(self) == Matrix
        if not isScalars and not isMatrix:
            raise Exception("The value is not valide")
        isVector = isMatrix and data.shape[0] == 1 or data.shape[1] == 1
        if isScalars:
            res = list()
            for i in range(0, self.shape[0]):
                row = list()
                for j in range(0, self.shape[1]):
                        row.append(self.data[i][j] * data)
                res.append(row)
            return Matrix(res)
        elif isMatrix and not isVector:
            if self.shape[0] != data.shape[1]:
                raise Exception("impossible operations between 2 matrix of imcompatible shape")
            res = list()
            for j in range(0, data.shape[1]):
                row = list()
                for i in range(0, data.shape[0]):
                    row.append([data.data[i][j]])
                res.append(self.mul_matrix_vector(Vector(row)))
            return Matrix(res).T()
        else : # matrix n of shape (m, n) have to match vector [n, 1] it will return a result of demension [m, 1]
            if self.shape[1] != data.shape[0]:
                raise Exception("impossible operations between matrix and vector") # don't have the same column size
            return [self.mul_matrix_vector(data)]

            
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
        return f"{type(self).__name__}({self.data})"
    def __repr__(self):
        return str(self.data)


class Vector(Matrix):
    def __init__(self, data):
        if len(data) != 1 and len(data[0]) != 1:
            raise Exception("Value is not a vector")
        super().__init__(data)

    def __mul__(self, other):
        matrix = super().__mul__(other)
        return (Vector(matrix.data))

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
            return sum(res)
        else:
            res = list()
            for i in range(0, self.shape[0]):
                res.append(self.data[i] * v.data[i])
            return sum(res)
