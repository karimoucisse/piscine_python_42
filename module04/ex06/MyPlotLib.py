import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from FileLoader import FileLoader
class MyPlotLib:

	def histogram(self, data, features):
		if not features:
			return None
		fig, axs = plt.subplots(1, len(features), tight_layout=True)
		for i in range(0, len(features)):
			axs[i].hist(data[features[i]])
			axs[i].set(title=features[i])
			axs[i].grid()
		plt.show()


	def density(self, data, features):
		if not features:
			return None
		fig, axs = plt.subplots()
		for feature in features:
			data[feature].plot(kind='density')
		axs.legend()
		plt.show()

	def pair_plot(self, data, features):
		if not features:
			return None
		num_features = len(features)
		fig, axs = plt.subplots(2, num_features)
		for i in range(0, 2):
			for j in range(0, num_features):
				if i == j:
					axs[i][j].hist(data[features[i]])
				else:
					if j == 1:
						axs[i][j].scatter(data[features[i + 1]], data[features[i]], s=0.5)
					else:
						axs[i][j].scatter(data[features[i - 1]], data[features[i]], s=0.5)
		plt.show()

	def box_plot(self, data, features):
		if not features:
			return None
		fig, axs = plt.subplots()
		s = data[features].dropna()
		axs.boxplot(s)
		plt.show()




loader = FileLoader()
data = loader.load('../athlete_events.csv')

mp = MyPlotLib()
# mp.histogram(data, ["Height", "Weight"])
mp.histogram(data, ["Weight", "Height"])
