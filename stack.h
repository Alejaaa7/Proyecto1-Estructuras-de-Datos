#ifndef STACK_H
#define STACK_H

#include "list.h"

class Stack {
private:
    List data;

public:
    void push(int value);
    void pop();
    int peek();
    bool isEmpty();
    void display();
    const List& getData();  // <- CONST para evitar el error
};

#endif