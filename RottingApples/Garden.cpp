//
// Created by nikkie on 10.02.20 г..
//

#include <iostream>
#include "Garden.h"

Garden::Garden(int x, int y, int newTimeToCome, Queue &newRottenCells): rottenCells(newRottenCells), rows(x), columns(y) {
    garden = new char*[x];
    for(int i = 0; i < x; i++){
        garden[i] = new char[y];
    }
    for(int i = 0 ; i < x; i++){
        for(int j = 0 ; j < y ; j++){
            garden[i][j] = 'O';
        }
    }
    timeToCome = newTimeToCome;
}

void Garden::showGarden() {
    spreadTheRot();
    for(int i = 0 ; i < rows; i++){
        for(int j = 0 ; j < columns; j++){
            std::cout << garden[i][j] << ' ';
        }
        std::cout << std::endl;
    }

}

void Garden::spreadTheRot() {
    while(!rottenCells.isEmpty()){
        cell temp = rottenCells.deQueue();
        int a = temp.x, b = temp.y;
        int t = temp.time;
        if(t > timeToCome) { continue;}
        garden[a][b] = 'X';
        if(a -1  >= 0 && b - 1  >= 0 && garden[a-1][b-1] == 'O'){

            rottenCells.enQueue(cell(a-1,b-1,t+3),rows,columns);
        }
        if(a - 1 >= 0 && garden[a-1][b] == 'O'){
            rottenCells.enQueue(cell(a-1,b,t+3),rows,columns);
        }
        if(a - 1 >= 0 && b + 1 < columns && garden[a-1][b+1] == 'O'){

            rottenCells.enQueue(cell(a-1,b+1,t+3),rows,columns);
        }
        if(b - 1 >= 0 && garden[a][b-1] == 'O'){

            rottenCells.enQueue(cell(a,b-1,t+3),rows,columns);
        }
        if(b + 1 < columns && garden[a][b+1] == 'O'){

            rottenCells.enQueue(cell(a,b+1,t+3),rows,columns);
        }
        if(a + 1 < rows && b - 1 >= 0 && garden[a+1][b-1] == 'O'){

            rottenCells.enQueue(cell(a+1,b-1,t+3),rows,columns);
        }
        if(a +1 < rows && garden[a+1][b] == 'O'){

            rottenCells.enQueue(cell(a+1,b,t+3),rows,columns);
        }
        if(a + 1 < rows && b + 1 < columns && garden[a+1][b+1] == 'O'){

            rottenCells.enQueue(cell(a+1,b+1,t+3),rows,columns);
        }
    }
}

Garden::~Garden() {
    for(int i = 0 ; i < rows ; i++){
        delete[] garden[i];
    }
    delete[] garden;
}




