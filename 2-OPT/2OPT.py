import sys
from math import sqrt
from timeit import default_timer

def distance(c1, c2):
	return int(round(sqrt(abs((c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2))))

def tour_distance(cities):
	distance = 0
	previous = cities[-1]
	for city in cities:
		distance += distance(city, previous)
		previous = city
	return distance

def swap(cities, i, j):
	alt_tour = cities[0:i]
	alt_tour.extend(reversed(cities[i:j + 1]))
	alt_tour.extend(cities[j+1:])
	return alt_tour

def run_2opt(cities):
	improvement = True
	best_tour = cities
	best_distance = tour_distance(cities)
	
	while improvement: 
		improvement = False
		for i in range(len(best_tour) - 1):
			for j in range(i+1, len(best_tour)):
				alt_tour = swap(best_tour, i, j)
				alt_distance = tour_distance(alt_tour)
				if alt_distance < best_distance:
					best_distance = alt_distance
					best_tour = alt_tour
					improvement = True
					break
			if improvement:
				break
	return best_tour, best_distance

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
	tour, d = run_2opt(cities)
	end = default_timer()
	print("Runtime: " + str(end-start) + " seconds.")

	outFile.write(str(d) + '\n')

	for city in tour:
		outFile.write(str(city['id']) + ' ' + str(city['x']) + ' ' + str(city['y']) + '\n')

	inFile.close()
	outFile.close()

if __name__ == '__main__':
	main()
