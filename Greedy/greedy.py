import sys
from math import sqrt
from timeit import default_timer

def d2(c1, c2):
	return (c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2

def get_nn(cities, city):

	neighbors = {}

	for neighbor in cities:
		neighbors[d2(city, neighbor)] = neighbor

	nn = neighbors[min(neighbors)]
	d = int(round(sqrt(min(neighbors))))

	return nn, d

def TSP_nearest_neighbor(cities):
	tour = []
	dMin = sys.maxint

	for first in cities:
		total = 0
		visited = [first]
		unvisited = []

		for city in cities:
			if city is not first:
				unvisited.append(city)

		while len(unvisited) > 0:
			nn, d = get_nn(unvisited, visited[-1])
			visited.append(nn)
			unvisited.remove(nn)
			total += d	

		total += int(round(sqrt(d2(visited[0], visited[-1]))))

		if total < dMin:
			tour = visited
			dMin = total

	return tour, dMin

def main():

	try:
		inFile = open(sys.argv[1], 'r')
		outFile = open(sys.argv[1] + '.tour', 'w')
	except IndexError:
		print("[ERROR] Missing argument for testfile. \n")
		quit()
	except (IOError, OSError):
		print("[ERROR] Testfile not found. \n")
		quit()

	cities = []
	for line in inFile:
		spLine = line.split()
		city = {'id':int(spLine[0]), 'x':int(spLine[1]), 'y':int(spLine[2])}
		cities.append(city)

	start = default_timer()
	tour, d = TSP_nearest_neighbor(cities)
	end = default_timer()
	print("Runtime: " + str(end-start) + " seconds.")
	
	outFile.write(str(d) + '\n')

	for city in tour:
		outFile.write(str(city['id']) + ' ' + str(city['x']) + ' ' + str(city['y']) + '\n')



	inFile.close()
	outFile.close()


if __name__ == '__main__':
	main()
