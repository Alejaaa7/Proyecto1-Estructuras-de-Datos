#include <iostream>
#include <sstream> // para usar ostringstream
#include "node.h"
#include "list.h"
#include "array.h"
#include "stack.h"
#include "queue.h"


// función auxiliar para convertir una lista en texto
// ej: "1, 2, 3"
std::string listToString(const List& list) {
    std::ostringstream out;
	Node* aux = list.getHead(); // se obtiene el puntero al primer nodo
    while (aux != nullptr) {  // mientras que no esté vacío
		out << aux->data; // inserta el valor del nodo actual en el flujo out
        if (aux->next != nullptr) { // si hay un siguiente nodo
            out << ", "; // agrega una coma y espacio
		}
		aux = aux->next; // avanza al siguiente nodo
    }
	return out.str(); // convierte el flujo a string y lo devuelve
}

// para convertir un arreglo en texto
std::string arrayToString(Array& arr) {
    std::ostringstream out;
    out << "["; // se abre el corchete
    for (int i = 0; i < arr.getSize(); i++) { // se empieza a iterar
        out << arr.get(i); // se inserta el actual en el ostringstream
        if (i < arr.getSize() - 1) { // para no poner coma después del último
            out << ", ";
        }
    }
    out << "]";
    return out.str(); // se devuelve la cadena de texto final
}


int main(){

    // PROBAR LA LISTA
    List myList; // se crea una lista vacía

    // insertar elementos al final
    myList.insertAtEnd(1);
    myList.insertAtEnd(2);
    myList.insertAtEnd(3);

    // PROBAR STACK
	Stack myStack;
	myStack.push(10);
	myStack.push(20);
	myStack.push(30);

    // PROBAR QUEUE
	Queue myQueue;
	myQueue.enqueue(100);
	myQueue.enqueue(200);
	myQueue.enqueue(300);

    // PROBAR ARRAY
    Array myArray(3);
    myArray.set(0, 1000);
	myArray.set(1, 2000);
	myArray.set(2, 3000);

    // salida para que Python la pueda leer
    std::cout << "LIST: " << listToString(myList) << std::endl;
    std::cout << "STACK: " << listToString(myStack.getData()) << std::endl;
    std::cout << "QUEUE: " << listToString(myQueue.getData()) << std::endl;
    std::cout << "ARRAY: " << arrayToString(myArray) << std::endl;

}