#ifndef QUEUE_H
#define QUEUE_H

#include "list.h"

class Queue {
private:
    List data;

public:
    void enqueue(int value);
    void dequeue();
    bool isEmpty();
    void display();
    const List& getData();  // <- CONST para evitar el error
};

#endif