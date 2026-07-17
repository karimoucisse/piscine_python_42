import numpy as np
from FileLoader import FileLoader
loader = FileLoader()
def how_many_medals(df, name):
    medal = df[(df['Name'] == name)]
    years = list(medal.drop_duplicates('Year')['Year'])
    output = dict()
    for year in years:
        g = medal[(medal['Year'] == int(year)) & (medal['Medal'] == "Gold")].shape[0]
        s = medal[(medal['Year'] == int(year)) & (medal['Medal'] == "Silver")].shape[0]
        b = medal[(medal['Year'] == int(year)) & (medal['Medal'] == "Bronze")].shape[0]
        output[year] = {'G': g, 'S': s, 'B': b}
    print(output)
data = loader.load('../athlete_events.csv')
how_many_medals(data, 'Kjetil Andr Aamodt')