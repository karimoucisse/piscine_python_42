from sys import argv
import numpy as np
import matplotlib.pyplot as plt

def main():
	if len(argv) != 4:
		return

	array = np.genfromtxt(argv[1], delimiter=",")
	fig = plt.figure(0)
	plt.grid(True)
	plt.scatter(array[:,1], array[:,2], array[:, 3])
	plt.show()
	# print(array[:, 2])

if __name__=="__main__":
	main()
