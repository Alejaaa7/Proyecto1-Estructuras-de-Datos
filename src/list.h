#ifndef LIST_H
#define LIST_H

#include "node.h"

class List {
private:
    Node* head;
    Node* last;
    int length;

public:
    List();
    ~List();
    void clear();
    bool isEmpty() const;
    int size() const;
    void insertAtEnd(int value);
    void insertAtBeginning(int value);
    bool removeValue(int value);
    bool removeFirst();
    bool find(int value) const;
    void display() const;
    Node* getHead() const;
};

#endif