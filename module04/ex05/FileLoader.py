import pandas as pd

class FileLoader:
    def load(self, path):
        df = pd.read_csv(path)
        h = df.shape[0]
        w = df.shape[1]
        print(f"Loading dataset of dimensions {h} x {w}")
        return df
    def display(self, df, n):
        if not n % 2:
            return df.iloc[0:n, :]
        else :
            return df.iloc[-(n + 1):-1, :]
