//
// Created by nikkie on 10.02.20 г..
//

#ifndef ROTTINGAPPLES_GARDEN_H
#define ROTTINGAPPLES_GARDEN_H


#include "Queue.h"

class Garden{
public:
    Garden(int x,int y, int newTimeToCome, Queue& newRottenCells);
    ~Garden();

    void showGarden();
private:
    char **garden;
    int timeToCome;
    Queue rottenCells;
    int rows;
    int columns;

    void spreadTheRot();

};


#endif //ROTTINGAPPLES_GARDEN_H
