from PIL import Image
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor:

	def load(self, path):
		img = Image.open(path)
		a = np.array(img)
		print(f"Loading image of dimensions {a.shape[0]} x {a.shape[1]}")
		return a

	def display(self, array):
		plt.imshow(array)
		plt.show()

img = ImageProcessor()
arr = img.load("karimou.jpeg")
img.display(arr)
