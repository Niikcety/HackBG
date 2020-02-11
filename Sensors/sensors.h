//
// Created by nikkie on 10.02.20 г..
//

#ifndef SENSORS_SENSORS_H
#define SENSORS_SENSORS_H


#include <vector>
#include "sensor.h"

class Sensors{
public:
    Sensors(std::string& fileName, float newDistance, float newMaxError);

    void checkBrokenSensors();
    void showSensors();
    int numberOfNeighbours(int pos);
    bool isItNeighbour(int pos1, int pos2);
private:
    std::vector<Sensor> allSensors;
    std::vector<Sensor> brokenSensors;
    float distance;
    float maxError;
};


#endif //SENSORS_SENSORS_H
