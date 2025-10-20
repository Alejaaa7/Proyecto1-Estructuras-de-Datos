# include <iostream>
#include "queue.h" // nuevamente se incluye list

// para agregar un elemento al final de la cola
void Queue::enqueue(int value) {
	data.insertAtEnd(value); // entra al final
}

// para eliminar el elemento del frente de la cola (porque es FIFO)
void Queue::dequeue() {
	if (data.isEmpty()) {
		std::cout << "La cola est� vac�a\n"; // avisar que est� vac�a
	}

	Node* frontNode = data.getHead(); // se obtiene el del frente con getHead
	int frontValue = frontNode->data; // frontValue es el data del del frente
	data.removeValue(frontValue); // y se elimina frontValue
}

// para comprobar si est� vac�a
bool Queue::isEmpty() {
	return data.isEmpty(); // llama a isEmpty de la lista para determinarlo
}

// para mostrar los elemento en el orden correcto, de frente a atr�s, FIFO
void Queue::display() {
	std::cout << "QUEUE(front -> back): ";
	data.display(); // llama al m�todo display de la lista data
}

const List& Queue::getData() {
	return data;
}
