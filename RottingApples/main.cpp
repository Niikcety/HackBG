#include <iostream>
#include "Queue.h"
#include "Garden.h"

using namespace std;

void RottingApples(){
    int rows, columns, time, rotten, x, y;
    Queue a;
    std::cout << "Enter number of rows: ";
    std::cin >> rows;
    if(rows <= 0) throw std::runtime_error("Invalid number of rows");
    std::cout << "Enter number of columns: ";
    std::cin >> columns;
    if(columns <= 0) throw std::runtime_error("Invalid number of columns");
    std::cout << "After how many days you will come back: ";
    std::cin >> time;
    if(time < 0) throw std::runtime_error("Invalid time of coming back");
    std::cout << "How many rotten apple are in the garden: ";
    std::cin >> rotten;
    if(rotten < 0 ) throw std::runtime_error("Invalid number of rotten apples");
    while(rotten > 0){
        std::cout << "Enter the row of the rotten apple: ";
        std::cin >> x;
        std::cout << "Enter the column of the rotten apple: ";
        std::cin >> y;
        a.enQueue(cell(x-1,y-1),rows,columns);
        rotten--;
    }
    Garden gar(rows,columns,time, a);
    gar.showGarden();

}




int main() {
    RottingApples();




    return 0;
}
