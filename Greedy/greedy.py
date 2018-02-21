import sys
from math import sqrt

def d2(c1, c2):
	return (c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2

def getNN(cities, city):

	neighbors = {}

	for neighbor in cities:
		neighbors[d2(city, neighbor)] = neighbor

	nn = neighbors[min(neighbors)]
	d = int(round(sqrt(min(neighbors))))

	return nn, d

def greedy(cities):
	tour = []
	dMin = []

	for first in cities:
		total = 0
		visited = [first]
		unvisited = []

		for city in cities:
			if city is not first:
				unvisited.append(city)

		while len(unvisited) > 0:
			nn, d = getNN(unvisited, visited[-1])
			visited.append(nn)
			unvisited.remove(nn)
			total += d	

		total += int(round(sqrt(d2(visited[0], visited[-1]))))

		if dMin is [] or total < dMin:
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

	tour, d = greedy(cities)
	
	outFile.write(str(d) + '\n')

	for city in tour:
		outFile.write(str(city['id']) + ' ' + str(city['x']) + ' ' + str(city['y']) + '\n')



	inFile.close()
	outFile.close()


if __name__ == '__main__':
	main()
