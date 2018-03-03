#include <iostream>
#include <fstream>
#include <time.h>
#include <vector>
#include <math.h>

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
    std::vector<city> tour;
    int best_distance = INT_MAX;

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
    std::cout << tourDistance(citylist) << std::endl;
    std::cout << std::endl;

    for(std::vector<city>::iterator it = citylist.begin(); it != citylist.end(); ++it) {
        city neigh = *it;
        
        std::cout << neigh.id << " " << neigh.x << " " << neigh.y << std ::endl;
    }

}

int main(int argc, const char * argv[]) {
    
    std::ifstream infile("tsp_example_3.txt");
//    std::ifstream infile(argv[1]);
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
                std::cout << init.id  << ", " << init.x  << ", " << init.y  << std::endl;
                cities.push_back(init);
		    }
            
            
        }
    }
    else {
        std::cout << "File could not be opened." << std::endl;
    }

    float total = 0;

    clock_t t1, t2;
    t1 = clock();

    print(TSP_NN(cities));
    
    t2 = clock();
    float diff ((float)t2 - (float)t1);     //Total time
    float seconds = diff/CLOCKS_PER_SEC;
    total = total + seconds;
    std::cout << seconds << " seconds." << std::endl;



    return 0;
}
