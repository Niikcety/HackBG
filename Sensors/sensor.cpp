//
// Created by nikkie on 10.02.20 г..
//

#include <iostream>
#include "sensor.h"


Sensor::Sensor(std::string str) {
    std::string newX, newY, newData;
    int counter = 0;
    for(int i = 0 ; i < str.length(); i++)
    {
        if(counter == 0){
            if(str[i] == ','){
                counter++;
                continue;
            }else{
                newX.push_back(str[i]);
            }
        }
        else if(counter == 1){
            if(str[i] == ','){
                counter++;
                continue;
            }else{
                newY.push_back(str[i]);
            }
        }else{
            newData.push_back(str[i]);
        }
    }
    x = std::stof(newX);
    y = std::stof(newY);
    data = std::stof(newData);
}

void Sensor::showXY() {
    std::cout << '(' << x <<',' << y <<')' << ' ';
}

float Sensor::getX() {
    return x;
}

float Sensor::getY() {
    return y;
}

float Sensor::getData() {
    return data;
}
