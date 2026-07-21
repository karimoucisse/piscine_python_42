class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		return sum([(x[0] * len(x[1])) for x in zip(coefs, words)])

	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		enum_coefs = list(enumerate(coefs))
		enum_words = list(enumerate(words))
		return sum(enum_coefs[x][1] * len(enum_words[x][1]) for x in range(len(enum_coefs)))

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]

print(Evaluator.enumerate_evaluate(coefs, words))
