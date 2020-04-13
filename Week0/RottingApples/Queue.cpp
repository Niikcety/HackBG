//
// Created by nikkie on 10.02.20 г..
//

#include <stdexcept>
#include "Queue.h"

void Queue::enQueue(cell newCell,int border1, int border2) {
    Node* temp = new Node(newCell);
    if(temp->data.x < 0 || temp->data.y < 0 || temp->data.x >= border1 || temp->data.y >= border2){
        throw std::runtime_error("Invalid data");
    }
    if(last == nullptr){
        front = last = temp;
    }
    else{
        last->next = temp;
        last = temp;
    }
}

cell Queue::deQueue() {
    cell temp(0,0,0);
    if(!isEmpty()){
        Node* tmp = front;
        front = front->next;

        temp.x = tmp->data.x;
        temp.y = tmp->data.y;
        temp.time = tmp->data.time;

        delete tmp;
        if(front == nullptr){
            last = nullptr;
        }
    }
    return temp;
}

bool Queue::isEmpty() {
    return front== nullptr;
}

Queue::Queue(const Queue &rhs, int x, int y): front(nullptr), last(nullptr)
{
    for(auto n = rhs.front; n!= nullptr; n = n->next){
        enQueue(n->data,x, y);
    }
}

