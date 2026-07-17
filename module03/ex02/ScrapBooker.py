import numpy as np

class ScrapBooker:

	def crop(self, array, dim, position=(0,0)):
		try:
			s = array[dim[1]:dim[0] + 1, position[1]:position[0]]
			return s
		except Exception as ex:
			return None

	def thin(self, array, n, axis):
		if axis == 1:
			new_axis = 0
		elif axis == 0:
			new_axis = 1
		try:
			s = np.delete(array, list(range(n - 1, array.shape[1], n)), axis=new_axis)
			return s
		except Exception as ex:
			return None

	def juxtapose(self, array, n, axis):
		try:
			s = array
			for i in range(0, n - 1):
				s = np.concatenate((s, array), axis = axis)
			return s
		except Exception as ex:
			return None

	def mosaic(self, array, dim):
		try:
			a = self.juxtapose(array, dim[0], 0)
			a = self.juxtapose(a, dim[1], 1)
			return a
		except Exception as ex:
			return None

spb = ScrapBooker()
n = spb.mosaic(arr1, (2, 2))
print(n)
