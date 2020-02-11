//
// Created by nikkie on 10.02.20 г..
//

#ifndef SENSORS_SENSOR_H
#define SENSORS_SENSOR_H


#include <string>

class Sensor{
public:
    Sensor(): x(0), y(0), data(0){}
    Sensor(std::string string);

    void showXY();
    float getX();
    float getY();
    float getData();

private:
    float x;
    float y;
    float data;
};


#endif //SENSORS_SENSOR_H
