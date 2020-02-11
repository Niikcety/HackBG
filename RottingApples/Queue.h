//
// Created by nikkie on 10.02.20 г..
//

#ifndef ROTTINGAPPLES_QUEUE_H
#define ROTTINGAPPLES_QUEUE_H

struct cell{
    int x;
    int y;
    int time;
    cell(int newX, int newY, int newTime = 0): x(newX), y(newY), time(newTime){}
};

struct Node{
    cell data;
    Node* next;

    Node(cell newData):data(newData),  next(nullptr){
    }
};


class Queue {
public:
    Queue(): front(nullptr), last(nullptr){}
    Queue(const Queue& rhs, int x, int y);

    void enQueue(cell newCell, int border1, int border2);
    cell deQueue();
    bool isEmpty();
private:
    Node* front;
    Node* last;
};


#endif //ROTTINGAPPLES_QUEUE_H
