import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		try:
			s = array[dim[1]:dim[0] + 1, position[1]:position[0]]
			return s
		except (ValueError, TypeError) as e:
			return None

	def thin(self, array, n, axis):
		# try:
			s = np.delete(array, list(range(n - 1, array.shape[1], n)), axis=n)
			return s
		# except (ValueError, TypeError) as e:
		# 	return None

	def juxtapose(self, array, n, a):
		try:
			s = array
			for i in range(n - 1):
				s = np.append(s, array, axis = a)
			return s
		except (ValueError, TypeError) as e:
			return None

	# def mosaic(self, array, dim):


spb = ScrapBooker()
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,0))