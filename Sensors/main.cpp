#include <iostream>
#include "sensor.h"
#include "sensors.h"

void sensors(){
    std::string name;
    float distance, maxError;
    std::cout << "Filename:" << std::endl;
    getline(std::cin, name);
    std::cout << "Neighbour distance" << std::endl;
    std::cin>>distance;
    std::cout << "Max error:" << std::endl;
    std::cin >> maxError;

    Sensors a(name,distance,maxError);
    a.checkBrokenSensors();
    a.showSensors();

}

int main() {

    sensors();


    return 0;
}
