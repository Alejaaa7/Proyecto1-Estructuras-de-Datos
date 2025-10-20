#include <iostream>
#include "list.h" 

// constructor
List::List() {
    head = nullptr;
    last = nullptr;
    length = 0;
}

// el destructor
List::~List(){
    clear(); // se utiliza la siguiente función clear que borre todos los nodos
}

    // se crea clear
void List::clear() {
    while(head != nullptr){ // mientras que el primero no esté vacío
        Node* aux = head; // se crea el puntero aux que apunta al mismo nodo que head
        head = head->next; // ahoar head apunta al siguiente
        delete aux; // se libera memoria del nodo al que aux apuntaba      
    } // todo eso hasta que head llegue a null
    last = nullptr; // para que ya no apunte a algo que se borró
    length = 0; // para actualizar el número de nodos
}

    // se crea isEmpty para decir si la lista es vacía
bool List::isEmpty() const {
    return head == nullptr; // devuelve verdaddero si head está vacío
}

    // size para la el tamaño
int List::size() const {
    return length;
}

    // insertAtEnd para un nuevo nodo al final
void List::insertAtEnd(int value){
    Node* newNode = new Node(value); // se resesrva memoria para un nuevo 
                                         // nodo y se llama al constructor

    if (head == nullptr){
        head = newNode;
        last = newNode; // si está vacía, el neuvo es primero y último
    }
    else{
        last->next = newNode; // el next del que antes era el último apunta al nuevo
        last = newNode; // ahora el último es el newNode
    }
    length++; // se aumenta el que cuenta los nodos
}

    // insertAtBeginning para insertar un nodo al principio
void List::insertAtBeginning(int value){
    Node* newNode = new Node(value); // aquí también se crea el nuevo
        
    if (head == nullptr){
        head = newNode;
        last = newNode; //  nuevamente si está vacía, el nuevo será ambos
    }
    else{
        newNode->next = head;// el siguiente del nuevo es el que era la cabeza
        head = newNode;
    }
    length++;
}

/* removevalue para eliminar cuando aparezca un valor, y devolver true si lo 
eliminó o false si no se encontró */
bool List::removeValue(int value) {
    if (isEmpty()) return false; // si está vacía pues no se encontrará

    // si hay que eliminar el primero
    if (head->data == value){
        Node* aux = head; // se apunta al que se va a borrar
        head = head->next; // la cabeza pasa a ser el que está de segundo
        delete aux; // se borra el que se estaba apuntando

        length--;

        if (head == nullptr){ // si la lista quedó vacía también last 
            last = nullptr;
        }
        return true;
    }

    // si es en general, se debe buscar el nodo que contenga ese valor
    Node* prev = head; // se apunta al primero, el anterior al de revisar
    Node* cur = head->next; // se apunta al segundo, el que se revisa

    while(cur != nullptr){ // que el que se está revisando no esté vacío
        // si el que se está revisando es el que se quiere borrar
        if(cur->data ==  value){
            // el siguiente del revisado pasa a ser el siguiente del anterior
            prev->next = cur->next;

            if (cur == last){ // si el revisado es el último
                last = prev; // el nuevo último nodo es el que era el anterior
            }
            delete cur; // se borra memoria del que se eliminó
            length--;
            return true;
        }
        prev = cur; // mueve el anterior al actual
        cur = cur->next; // mueve el actual al siguiente
    }

    return false; // donde devuelve false si no se encontró
}

    // find devuelve true si un valor está en la lista
bool List::find(int value) const{
    Node* aux = head; // se apunta al primero
    while(aux != nullptr){ // mientras no esté vacío
        if(aux->data == value){
            return true; // devuelve true si el que se mira es el buscado
        }
        aux = aux->next;
    }
    return false; 
}

// display para imprimir la lista en formato legible
void List::display() const {
    std::cout << "LIST: ";
    Node* aux = head; // nuevamente se empieza en la cabeza
    while(aux != nullptr){ // mientras que el actual no esté vacío
        std::cout << aux->data; // se imprime su dato
        if(aux->next != nullptr){ // si el siguiente al actual no es vacío
            std::cout << " -> "; // se imprime con una flecha a su derecha
        }
        aux = aux->next; // el siguiente del actual es el nuevo actual 
    }
    std::cout << std::endl; // nueva línea al final
}

bool List::removeFirst() {
    if(isEmpty()) return false; // verificar que no esté vacía

    Node* aux = head; // se referencia el primer nodo
    head = head->next; // head ahora apunta al segundo nodo
    delete aux; // se borra el nodo referenciado arriba
    length--; // y se disminuye el contador

    if (head == nullptr) { // si la lista queda vacía
        last = nullptr; // last también debe estar vacío
    }
    return true;
}

    //  se crea un getter para obtener el puntero al primer nodo (head)
Node* List::getHead() const { // devuelve el puntero al primer nodo, pero no lo modifica
    return head; // devuelve el valor del puntero head
}
