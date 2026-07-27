from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter:

	def invert(self, array):
		new_array = array.copy()
		print(new_array)
		row = len(array)
		col = len(array[0])
		for i in range(0, row):
			for j in range(0, col):
				for k in range(0, 3):
					new_array[i, j, k] = 255 - new_array[i, j, k]

		return new_array

	def to_blue(self, array):
		array_copy = array.copy()
		array_copy[:,:,2] = 255

		red_array = array_copy[:,:,0]
		green_array = array_copy[:,:,1]
		blue_array = array_copy[:,:,2]

		end = np.dstack((red_array, green_array ,blue_array))
		return end

	def to_green(self, array):
		new_array = array.copy()
		print(new_array.shape)
		row = len(array)
		col = len(array[0])
		for i in range(0, row):
			for j in range(0, col):
				new_array[i, j, 1] = 255
		return new_array

	def to_red(self, array):
		green = self.to_green(array)
		blue = self.to_blue(array)
		red = array.copy()
		red[:,:,0] = 255
		return red
	def to_celluloid(self, array):


c = ColorFilter()
v = ImageProcessor()
a = v.load("elon.png")
# k = c.invert(a)
# k =  c.to_blue(a)
# k = c.to_green(a)
k = c.to_red(a)
v.display(k)

