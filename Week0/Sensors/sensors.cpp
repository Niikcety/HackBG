//
// Created by nikkie on 10.02.20 г..
//

#include <fstream>
#include <iostream>
#include "sensors.h"
#include "cmath"

Sensors::Sensors(std::string& fileName, float newDistance, float newMaxError): distance(newDistance), maxError(newMaxError){
    std::ifstream file(fileName);
    std::string str;
    while (std::getline(file, str)) {
        allSensors.push_back(Sensor(str));
    }
    file.close();
}

int Sensors::numberOfNeighbours(int pos) {
    int sensSz = allSensors.size();
    int ctr = 0;
    for(int i = 0 ; i < sensSz; i++){
        float sth = pow((allSensors[pos].getX()-allSensors[i].getX()),2) + pow(allSensors[pos].getY()-allSensors[i].getY(),2);
        float d = sqrt(sth);
        if(d <= distance) ctr++;
    }
    return ctr-1;
}




void Sensors::checkBrokenSensors() {
    int sensSz = allSensors.size();
    int numberOfBroken = 0;
    int nOS = 0;
    while(nOS < sensSz){
        int nOn = numberOfNeighbours(nOS);
        for(int i = 0 ; i < sensSz; i++){
            if(isItNeighbour(i,nOS) && abs(allSensors[nOS].getData() - allSensors[i].getData()) > maxError) numberOfBroken++;
        }
        if(nOn == numberOfBroken && nOn != 0 ) brokenSensors.push_back(allSensors[nOS]);
        nOS++;
        numberOfBroken = 0;
    }

}

void Sensors::showSensors() {
 /*   std::cout<< "Check Sensors: ";*/
    if(brokenSensors.empty()){
        std::cout << "All sensors are OK"<<std::endl;
    }else{
        std::cout << "Check sensors: ";
        for(auto& brokenSensor : brokenSensors){
            brokenSensor.showXY();
        }
    }
}

bool Sensors::isItNeighbour(int pos1, int pos2) {
    float sth = pow((allSensors[pos2].getX()-allSensors[pos1].getX()),2) + pow(allSensors[pos2].getY()-allSensors[pos1].getY(),2);
    float d = sqrt(sth);
    return (d <= distance && d > 0);
}


