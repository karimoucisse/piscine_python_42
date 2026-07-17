from FileLoader import FileLoader
loader = FileLoader()

def proportion_by_sport(df, year, sport, gender):
    by_gender_sport = df[(df['Year'] == year) & (df['Sport'] == sport) & (df['Sex'] == gender)]
    by_gender_sport_no_duplic = by_gender_sport.drop_duplicates('Name')
    by_gender = df[(df['Year'] == year) & (df['Sex'] == gender)]
    by_gender_no_duplic = by_gender.drop_duplicates('Name')

    calc = (by_gender_sport_no_duplic.shape[0] / by_gender_no_duplic.shape[0]) * 100
    print(float(calc))

data = loader.load('../athlete_events.csv')
proportion_by_sport(data, 2004, 'Tennis', 'F')