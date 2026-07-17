from FileLoader import FileLoader

def youngest_fellah(df, year):
    m = df[(df['Sex'] == 'M') & (df['Year'] == year)]['Age'].min()
    f = df[(df['Sex'] == 'F') & (df['Year'] == year)]['Age'].min()
    dict_youngest = {
        'f' : float(f), 'm' : float(m)
    }
    print(dict_youngest)

def test():
    file = FileLoader()
    data = file.load("../athlete_events.csv")
    youngest_fellah(data, 2004)

test()