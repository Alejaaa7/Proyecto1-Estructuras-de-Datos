#ifndef ARRAY_H
#define ARRAY_H

class Array {
private:
    int* data;
    int size;

public:
    Array(int n);
    ~Array();
    bool isEmpty();
    int getSize();
    void set(int index, int value);
    int get(int index);
    void pushBack(int value);
    void insertAt(int index, int value);
    void removeAt(int index);
    void clear();
    int find(int value);
    void display();
};

#endif