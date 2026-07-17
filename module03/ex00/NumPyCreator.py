import numpy as np
from numpy import dtype

class NumPyCreator:
	def from_list(self, lst):
		if type(lst) != list:
			return None
		try:
			np_lst = np.array(lst)
			return np_lst
		except (ValueError, TypeError) as e:
			return None

	def from_tuple(self, tpl):
		if type(tpl) != tuple:
			return None
		try:
			np_tpl = np.array(tpl)
			return np_tpl
		except (ValueError, TypeError) as e:
			return None

	def from_iterable(self, itr):
		return np.array(list(itr))

	def from_shape(self, shape, value = 0):
		return np.full(shape, value)

	def random(self, shape = 0):
		return np.random.random_sample(shape)

	def identity(self, n):
		return np.identity(n)
