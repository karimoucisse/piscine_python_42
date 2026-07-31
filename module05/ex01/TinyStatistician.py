import numpy as np
import math

class TinyStatistician:

    def is_valide(self, x):
        if len(x) == 0:
            return None
        for i in x:
            if type(i) != int and type(i) != float:
                return False
        return True
         
    def mean(self, x):
        if not self.is_valide(x):
            return None
        # return float(sum(x) / len(x))
        res = 0
        for i in x:
            res += i
        return float(res/len(x))

    def median(self, x):
        if not self.is_valide(x):
            return None
        res = 0
        x.sort()
        if len(x) % 2: # impair
            res = x[int(len(x) / 2)]
        else:
            n1 = x[int(len(x) / 2) - 1]
            n2 = x[int(len(x) / 2)]
            res = self.mean([n1, n2])
        return float(res)

    def quartile(self, x):
        if not self.is_valide(x):
            return None
        x.sort()
        q1 = math.ceil(0.25 * len(x)) - 1
        q3 = math.ceil(0.75 * len(x)) - 1
        return [float(x[q1]), float(x[q3])]

    def percentile(self, x, p):
        if not self.is_valide(x):
            return None
        if not isinstance(p, (int, float)):
            return None
        x.sort()
        i = p * (len(x) - 1) / 100
        k = int(i)
        f = i - k 
        x1 = x[k]
        x2 = x[k+1]
        return round(x1 + f * (x2 - x1), 1)        
        # print(10 + 0.6 * (43 - 0.6))

    def var(self, x):
        if not self.is_valide(x):
            return None
        m = self.mean(x)
        res = list()
        for i in x:
            res.append(pow(i - m, 2))
        # np.sum((x - self.mean(x)) ** 2)
        return sum(res)/ len(x)

    def std(self, x):
        if not self.is_valide(x):
            return None
        return math.sqrt(self.var(x))

a = [1, 42, 300, 10, 59]
print(TinyStatistician().mean(a)) # Output: # 82.4
print(TinyStatistician().median(a)) # Output: 42.
print(TinyStatistician().quartile(a)) # Output:[10.0, 59.0]
print(TinyStatistician().percentile(a, 10)) # Output: 4.6
print(TinyStatistician().percentile(a, 10)) # Output: 4.6
print(TinyStatistician().var(a)) # Output: 12279.439999999999
print(TinyStatistician().std(a)) # Output: 110.81263465868862