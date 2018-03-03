import sys
from math import sqrt
from timeit import default_timer

def distance_squared(c1, c2):
	return (c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2

def nearest_neighbor(cities, city):
	neighbors = {}

	for neighbor in cities:
		neighbors[distance_squared(city, neighbor)] = neighbor

	nn = neighbors[min(neighbors)]
	d = int(round(sqrt(min(neighbors))))

	return nn, d

def TSP_NN(cities):
	start = default_timer()
	tour = []
	best_distance = sys.maxint

	for first in cities:
		total = 0
		visited = [first]
		unvisited = []

		for city in cities:
			if city is not first:
				unvisited.append(city)

		while len(unvisited) > 0:
			nn, d = nearest_neighbor(unvisited, visited[-1])
			visited.append(nn)
			unvisited.remove(nn)
			total += d

		total += int(round(sqrt(distance_squared(visited[0], visited[-1]))))

		if total < best_distance:
			tour = visited
			best_distance = total

		if ((default_timer() - start) >= 10):
			return tour, best_distance

	return tour, best_distance

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
	tour, d = TSP_NN(cities)
	end = default_timer()
	print("Runtime: " + str(end-start) + " seconds.")
	
	outFile.write(str(d) + '\n')

	for city in tour:
		outFile.write(str(city['id']) + ' ' + str(city['x']) + ' ' + str(city['y']) + '\n')

	inFile.close()
	outFile.close()


if __name__ == '__main__':
	main()
