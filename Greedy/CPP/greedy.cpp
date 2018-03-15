#include <iostream>
#include <fstream>
#include <time.h>
#include <vector>
#include <math.h>
#include <string>
#include <limits.h>

struct city {
    int id, x, y;
};

int distance(city c1, city c2){
    return round(pow(pow((c1.x - c2.x),2) + pow((c1.y - c2.y),2),.5));
}

int tourDistance(std::vector<city> tour){
	int tourDistance = 0;

	for(int i = 1; i < tour.size(); i++){
		tourDistance += distance(tour.at(i-1),tour.at(i));
//		std::cout << tourDistance << std::endl;
	}
	
	tourDistance += distance(tour.front(), tour.back());

	return tourDistance;
}

double nearest_neighbor(std::vector<city> clist, city curr){
    std::vector<city>::iterator nn;
    int minDistance = INT_MAX;
    
    for(std::vector<city>::iterator it = clist.begin(); it != clist.end(); ++it) {
        city neigh = *it;
        
        if (minDistance > distance(curr, neigh)){
            nn = it;
            minDistance = distance(curr, neigh);
        }
    }
    
    return std::distance(clist.begin(),nn);
}

std::vector<city> TSP_NN(std::vector<city> cities){
    std::vector<city> tour = cities;
    // int best_distance = INT_MAX;
    int best_distance = tourDistance(cities);

    clock_t timeStart = clock();

    for(std::vector<city>::iterator it = cities.begin(); it != cities.end(); ++it) {
        std::vector<city> visited;
        std::vector<city> unvisited;
        visited.clear();
        unvisited.clear();
        int total = 0;
        visited.push_back(*it);
        
        for(std::vector<city>::iterator it2 = cities.begin(); it2 != cities.end(); ++it2) {
            if (it != it2)
                unvisited.push_back(*it2);
        }
        
            while (!unvisited.empty()){
                double nn = nearest_neighbor(unvisited, visited.back());
                
                total += distance(visited.back(), unvisited.at(nn));
    
                visited.push_back(unvisited.at(nn));
                unvisited.erase(unvisited.begin()+nn);                
            }
            
            total += distance(visited.front(), visited.back());
            
            if (total < best_distance){
                tour = visited;
                best_distance  = total;
            }

        if ((clock() - timeStart) / CLOCKS_PER_SEC >= 170) // time in seconds
            return tour;
    }
    
    return tour;
}

void print (std::vector<city> citylist){
    // std::cout << tourDistance(citylist) << std::endl;
    // std::cout << std::endl;

    for(std::vector<city>::iterator it = citylist.begin(); it != citylist.end(); ++it) {
        city neigh = *it;
        
        std::cout << neigh.id << " " << neigh.x << " " << neigh.y << std ::endl;
    }
}

int main(int argc, const char * argv[]) {
    
    // std::ifstream infile("tsp_example_2.txt");
    std::ifstream infile(argv[1]);
    std::ofstream outfile(std::string(argv[1])+".tour");
    std::vector<city> cities;

    if(infile.is_open()){
        //Begin loop to go through all rows of text file
        while(infile.good()){  
                
            //city struct
            city init;
            int a;
            // Put city ID, start & finish time into new struct
            while (infile >> a) {
    	        init.id = a;
                infile >> init.x;
                infile >> init.y;
                // std::cout << init.id  << ", " << init.x  << ", " << init.y  << std::endl;
                cities.push_back(init);
		    }
        }
    }
    else {
        std::cout << "File could not be opened." << std::endl;
    }
    infile.close();

    float total = 0;

    clock_t t1, t2;
    t1 = clock();
	
	// std::cout << tourDistance(cities) << std::endl;
    // print(TSP_NN(cities));
	// std::cout << tourDistance(cities) << std::endl;

    cities = TSP_NN(cities);
    int best_distance = tourDistance(cities);

    outfile << best_distance << std::endl;

    for(std::vector<city>::iterator it = cities.begin(); it != cities.end(); ++it) {
        city neigh = *it;
        outfile << neigh.id << " " << neigh.x << " " << neigh.y << std::endl;
    }
    
    t2 = clock();
    float diff ((float)t2 - (float)t1);     //Total time
    float seconds = diff/CLOCKS_PER_SEC;
    total = total + seconds;
    std::cout << seconds << " seconds." << std::endl;


    // outfile.close();


    return 0;
}
