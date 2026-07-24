from FileLoader import FileLoader
import pandas as pd
class SpatioTemporalData:

	def __init__(self, data):
		self.data = data

	def when(self, location):
		years = self.data[(self.data["City"] == location)]["Year"]
		no_duplicates = list(years.drop_duplicates())
		print(no_duplicates)

	def where(self, date):
		cities = self.data[(self.data["Year"] == int(date))]["City"]
		no_duplicates = list(cities.drop_duplicates())
		print(no_duplicates)


loader = FileLoader()
data = loader.load('../athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15
sp = SpatioTemporalData(data)
sp.where(2016)
