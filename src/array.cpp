#include <iostream>
#include "array.h"

// implementación de array

Array::Array(int n) {
    size = n;
    data = new int[size];
    for (int i = 0; i < size; i++) {
        data[i] = 0;
    }
}

// destructor
Array::~Array() {
    delete[] data;
}

bool Array::isEmpty() {
    return size == 0;
}

int Array::getSize() {
    return size; // nos da el tamaño del arreglo, tomando el atributo size
}

// insertar algún valor en la posición index
void Array::set(int index, int value){
    if (!isEmpty()) { // solo si el arreglo no está vacío
        if (index >= 0 && index < size) { // que el índice sea válido
            data[index] = value; // se asigna el nuevo valor en la posición
            };
        };
};

// extraer los valores dado un índice
int Array::get(int index) {
    if (index < 0 || index >= size ) { //muestra el mensaje si esl índice está fuera del rango 
        std::cout << "Índice fuera de rango" << std::endl; 
        return 0;// devuelve 0 como valor por defecto
    }
    if (!isEmpty()) { // si no está vacío
        return data[index]; // devuelve el valor en esa posición
    }
    return 0;
};

// insertar un valor al final del arreglo, esto lo "alarga" en 1
void Array::pushBack(int value) {
    int* aux = new int[size + 1]; // crear un nuvevo arreglo con una posición más
    for(int i = 0; i < size; i++){
        aux[i] = data[i]; // se copian todos los elementos del arreglo actual al nuevo
    };
    aux[size] = value; // se pone el valor recibido en la nueva última posición
    size++; // y se aumenta el tamaño del arreglo
    delete[] data; // se libera la memoria 
    data = aux; // el puntero data apunta al nuevo arreglo ampliado 
};

//insertar un x valor en un i indice
void Array::insertAt(int index, int value){
    if (index < 0 || index > size) { // nuevamente, se valida que el índice esté en el rango
        std::cout << "Índice fuera de rango\n"; 
        return;
    };
    int* aux = new int[size + 1]; // se crea un arreglo nuevo con una posición más
    for (int i = 0; i < index; i++){ 
        aux[i] = data[i]; // se copian todos los elementos antes de la posición dada
    };
    aux[index] = value; // se coloca el valor en la posición dada
    for (int i = size; i > index; i--) {
        aux[i] = data[i - 1]; // se mueven los elementos restantes una posición hacia la derecha
    };
    size++; // se incrementa el tamaño total
    delete[] data; // se libera la memoria
    data = aux; // data apunta al nuevo arreglo
};


// eliminar un elemento en una posición específica
void Array::removeAt(int index) {
    if (index < 0 || index >= size) { // se verifica que el índice sea válido 
        std::cout << "Índice fuera de rango\n"; // si no, se envía un mensaje
        return;
    };
    int* aux = new int[(size - 1)]; // se crea un nuevo arreglo con una posición menos
    for (int i = 0; i < index; i++) { // para un índice válido, 
        aux[i] = data[i]; // copia los elementos antes del índice
    };
    for (int i = index; i < (size - 1); i++) {
        aux[i] = data[i + 1]; // salta el valor eliminado y mueve los demás hacia la izquierda
    };
    size--; // se reduce el tamaño total
    delete[] data; // se libera memoria
    data = aux; // nuevamente, data apunta al nuevo arreglo reducido
};

// poner todos los elementos del arreglo en 0, sin cambiar su tamaño
void Array::clear() {
    for (int i = 0; i < size; i++) {  
        data[i] = 0; // se asigna cero a cada posición
    };
};

// buscar un valor en el arreglo y devolver su posición si existe
int Array::find(int value){
    for (int i = 0; i < size; i++) {
        if (data[i] == value) { // si se encuentra el valor, 
            return i; // y se devuelve la posición donde se encontró
        }
    }
    //si no se encontró, entonces enviar mensaje
    std::cout << "Valor no encontrado en el arreglo";
    return -1; // -1 para indicar que no existe
};


// imprimir el arreglo de forma legible
void Array::display(){
    std::cout << "["; // se abre el corchete
    for (int i = 0; i < size - 1; i++) {
        std::cout << data[i] << ", "; // imprime cada elemento menos el último separados por comas
    };
    std::cout << data[size-1]; // imprime el último elemento
    std::cout << "]" << std::endl; // cierra el corchete
};
