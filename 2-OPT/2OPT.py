import sys
from math import sqrt
from timeit import default_timer

def distance(c1, c2):
	return int(round(sqrt(abs((c1['x'] - c2['x'])**2 + (c1['y'] - c2['y'])**2))))

def route_distance(route):
	dist = 0
	prev = route[-1]
	for node in route:
		dist += distance(node, prev)
		prev = node
	return dist

def swap_2opt(route, i, k):
	new_route = route[0:i]
	new_route.extend(reversed(route[i:k + 1]))
	new_route.extend(route[k+1:])
	return new_route


def run_2opt(route):
	improvement = True
	best_route = route
	best_distance = route_distance(route)
	
	while improvement: 
		improvement = False
		for i in range(len(best_route) - 1):
			for k in range(i+1, len(best_route)):
				new_route = swap_2opt(best_route, i, k)
				new_distance = route_distance(new_route)
				if new_distance < best_distance:
					best_distance = new_distance
					best_route = new_route
					improvement = True
					break #improvement found, return to the top of the while loop
			if improvement:
				break
	return best_route, best_distance

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
