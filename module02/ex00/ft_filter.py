

def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	for i in range(0, len(iterable)):
		if function_to_apply(iterable[i]):
			yield iterable[i]

x = [1, 2, 3, 4, 5]
res = ft_filter(lambda dum: not (dum % 2), x)
print(list(res))

print(res)


