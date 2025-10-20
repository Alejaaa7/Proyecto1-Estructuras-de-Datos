# include <iostream>
# include "stack.h" // se hace implementando list


// para agregar un elemento a la parte superior
void Stack::push(int value) {
	data.insertAtBeginning(value); // se inserta al inicio un valor
}

// para eliminar el elemento de la parte superior
void Stack::pop() {
	if (data.isEmpty()) { // si est� vac�o
		std::cout << "La pila est� vac�a\n"; // imprime mensaje
		return;
		}

	Node* topNode = data.getHead(); // se obtiene el nodo del tope
	int topValue = topNode->data;
	data.removeValue(topValue); // se elimina el valor
	}

// para obtener el elemento del tope sin eliminarlo
int Stack::peek() {
	if (data.isEmpty()) {
		std::cout << "La pila está vacía\n";
		return -1;
	}

	// nuevamente, se obtiene el nodo del tope usando getHead()
	Node* topNode = data.getHead();
	return topNode->data; // se devuelve su valor
}

// verificar si est� vac�a
bool Stack::isEmpty() {
	return data.isEmpty();
}

// mostrar los elementos de la pila
void Stack::display() {
	std::cout << "STACK (top -> bottom): ";
	data.display();
}

// devolver la lista interna
const List& Stack::getData() {
	return data;
}			
