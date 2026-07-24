from FileLoader import FileLoader

def how_many_medals_by_country(df, country):
	by_country = df[(df["City"] == country)]
	years = list(by_country.drop_duplicates("Year")["Year"])
	res = {}
	for year in years:
		medals = by_country.drop_duplicates("Sport")
		g = medals[(medals['Year'] == int(year)) & (medals['Medal'] == "Gold")].shape[0]
		s = medals[(medals['Year'] == int(year)) & (medals['Medal'] == "Silver")].shape[0]
		b = medals[(medals['Year'] == int(year)) & (medals['Medal'] == "Bronze")].shape[0]
		res[year] = {'G': g, 'S': s, 'B': b}
	print(res)

loader = FileLoader()
data = loader.load('../athlete_events.csv')
how_many_medals_by_country(data, 'Paris')
