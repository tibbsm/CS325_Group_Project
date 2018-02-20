# Class: 	CS325 - Winter 2018
# Author: 	Group 45 (Marc Tibbs, Brad Besserman, Michael Chan)
# Project: 	Traveling Sales Man
# Program:	Accepts input from testfiles. 

import sys

def main():

	try:
		inFile = open(sys.argv[1], 'r')
		outFile = open(sys.argv[1] + '.tour', 'w')
	except IndexError:
		print("[ERROR] Missing argument for testfile. \n")
		quit()
	except IOError, OSError:
		print("[ERROR] Testfile not found. \n")
		quit()

	cities = []
	for line in inFile:
		spLine = line.split()
		city = {'id':int(spLine[0]), 'x':int(spLine[1]), 'y':int(spLine[2])}
		cities.append(city)

	for city in cities:
		outFile.write(str(city['id']) + ' ' + str(city['x']) + ' ' + str(city['y']) + '\n')

	inFile.close()
	outFile.close()

main()