# Proyecto1, Estructuras de Datos

# Visualizador de estructuras de datos

## ¿Cuál es el objetivo del proyecto?

Al comenzar con el estudio de las estructuras de datos, nos dimos cuenta de que resulta bastante difícil formarse una idea clara y visual de cómo funcionan y se ven realmente. A pesar de entender los conceptos teóricos, nos costaba imaginar de manera intuitiva cómo se organizan los datos internamente, cómo se conectan entre sí o cómo cambian a medida que se ejecutan las operaciones.

El proyecto surge como una respuesta a la necesidad de presentar las estructuras de datos de una manera gráfica e intuitiva para facilitar su comprensión y manejo. Como vimos durante las diferentes clases, presentar la estructura de una manera gráfica, clara y concisa, ayuda en gran medida a entender qué operaciones se deben aplicar y de qué manera para dar solución a los requerimientos de los diferentes problemas. 

Es por esto que el proyecto que decidimos desarrollar es visualizador que permite ver de manera gráfica las estructuras de datos que se van utilizando en caulquier tarea. Para esta primera entrega, nos enfocamos en mostrar los arreglos y las listas, con colas y pilas incluídas dentro de estas últimas.

## ¿Cómo se llevó a cabo?

El primer paso en el desarrollo del proyecto fue identificar cuáles estructuras podíamos incluir en el mismo. Para esta primera etapa, las estructuras que podíamos manejar con fluidez y confianza suficiente eran: arreglos, listas, colas y pilas. 

A pesar de no ser necesario, consideramos que realizar nosotros mismos las clases de cada estructura era de grandísima ayuda y utilidad para el proyecto, pues además de ser un ejercicio de repaso, permite crear métodos útiles para los diferentes tipos de estructura y saber a detalle cómo funciona cada estructura a bajo nivel para garantizar que la visualización será fiel a la realidad.

Luego, a fin de facilitar la realización de la interfaz gráfica que permite la visualización de las estructuras, se realizó un esquema de cómo debería verse la ventana en Tkinter, una biblioteca de python que permite realizar ventanas y componentes visuales como botones, cuadros de texto, menús, gráficos y demás.

El siguiente paso fue realizar la "conexión" entre el backend, realizado en c++, y el frontend (interfaz de Tkinter en python). Para llevar esto a cabo, se generó un archivo compilado (.exe) que se ejecuta desde python, de esta manera se permite al ususario acceder y visualizar las estructuras desde la capa visual generada por python sin necesidad de interactuar directamente con la consola.

## Requisitos del Sistema

### Python
- **Versión**: Python 3.8 o superior
- **Bibliotecas necesarias**:
  - `tkinter` (incluido en Python por defecto)
  - `subprocess` (incluido en Python por defecto) 
  - `os` y `sys` (incluidos en Python por defecto)
  - `re` (incluido en Python por defecto)

### C++ 
- **Compilador**: g++ (GCC) o cualquier compilador C++ compatible
- **Sistema**: Windows, Linux o macOS

### Sistema Operativo
- Windows 10/11
- Linux (Ubuntu, Fedora, etc.)
- macOS

## Manual de Usuario

### Inicio Rápido

1. **Ejecutar la aplicación:**
```
cd interfaz
python interfaz.py
```

2. **Seleccionar estructura:** Haz clic en los signos ❕ superiores (Lista, Pila, Cola, Array), para seleccionar una estructura y ver un ejemplo básico de la misma.

3. **Escribir código:** Usa el editor izquierdo para escribir código C++.

4. **Ejecutar:** Presiona el botón **EJECUTAR** para visualizar.

### Funcionalidades Principales

#### Editor de Código
- Escribe código C++ válido usando las estructuras implementadas
- **Ejemplos predefinidos** según la estructura seleccionada
- **Sintaxis resaltada** para mejor legibilidad

#### Botones Interactivos
- **➕ AGREGAR:** Inserta elemento (usa el valor del campo numérico)
- **✖️ ELIMINAR:** Remueve elemento (verifica existencia primero)
- **🔄️ VACIAR:** Limpia la estructura actual completamente
- **EJECUTAR:** Procesa y visualiza todo el código actual

#### Visualizaciones
- **Cada estructura** tiene su propia paleta de colores.
- **Elementos centrados** automáticamente.
- **Títulos descriptivos** y comportamiento visual claro.

### Ejemplos de Uso

#### Lista Enlazada
```
List miLista;
miLista.insertAtEnd(10);
miLista.insertAtEnd(20);
miLista.insertAtEnd(30);
```

#### Pila (LIFO)
```
Stack miPila;
miPila.push(100);
miPila.push(200);
miPila.push(300);
```

#### Cola (FIFO)
```
Queue miCola;
miCola.enqueue(50);
miCola.enqueue(60);
miCola.enqueue(70);
```

#### Array
```
Array miArray(3);
miArray.set(0, 500);
miArray.set(1, 600);
miArray.set(2, 700);
```

### Mensajes y Errores

- **✅ Operación exitosa:** Mensaje verde de confirmación (al hacer una operación).
- **❌ Error:** Mensaje rojo explicando el problema.
- **⚠️ Valores inválidos:** Se notifica si intentas eliminar elementos inexistentes.

## Características Principales

### Visualizaciones Aesthetic
- **Lista Enlazada**: Nodos con división DATA/NEXT + flechas conectivas
- **Pila (LIFO)**: Elementos apilados verticalmente + indicador TOPE
- **Cola (FIFO)**: Elementos en fila + labels FRENTE/FINAL  
- **Array**: Cajas contiguas con índices + acceso directo

### Interfaz Intuitiva
- **Editor de código C++ integrado**
- **Botones interactivos**: Agregar, Eliminar, Vaciar, Ejecutar
- **Análisis en tiempo real** del código del usuario
- **Feedback visual inmediato** de todas las operaciones

### Tecnologías Utilizadas
- **Backend**: C++ (implementación de estructuras)
- **Frontend**: Python + Tkinter (interfaz gráfica)
- **Visualización**: Canvas de Tkinter + algoritmos de dibujo
- **Comunicación**: Análisis inteligente de código (sin compilación)

## Estructura del Proyecto

```
PROYECTO - Estructuras/
├── interfaz/
│   ├── interfaz.py              # Interfaz gráfica principal
│   ├── diseño_interfazFINAL.png # Diseño visual
│   ├── utils/
│   │   └── parser.py            # Analizador de salida C++
│   └── visualizaciones/
│       ├── lista_visual.py      # Visualización de lista
│       ├── pila_visual.py       # Visualización de pila
│       ├── cola_visual.py       # Visualización de cola
│       └── arreglo_visual.py    # Visualización de array
├── src/
│   ├── main.cpp                 # Programa principal C++
│   ├── list.h/cpp               # Implementación de lista
│   ├── stack.h/cpp              # Implementación de pila
│   ├── queue.h/cpp              # Implementación de cola
│   └── array.h/cpp              # Implementación de array
└── README.md
```

## Estructuras de Datos Implementadas

### Lista Enlazada
- **Inserción**: `insertAtEnd()`, `insertAtBeginning()`
- **Eliminación**: `removeValue()`, `removeAt()`
- **Búsqueda**: `find()`
- **Visualización**: Nodos conectados con punteros

### Pila (LIFO)
- **Operaciones**: `push()`, `pop()`, `peek()`
- **Comportamiento**: Último en Entrar, Primero en Salir
- **Visualización**: Elementos apilados verticalmente

### Cola (FIFO)  
- **Operaciones**: `enqueue()`, `dequeue()`, `getFront()`
- **Comportamiento**: Primero en Entrar, Primero en Salir
- **Visualización**: Elementos en fila horizontal

### Array Dinámico
- **Operaciones**: `set()`, `get()`, `pushBack()`, `removeAt()`
- **Característica**: Acceso directo por índice O(1)
- **Visualización**: Cajas contiguas con índices

## Autores
- [Andrea Alejandra Suárez]
- [Manuel Arturo Fajardo]

## Licencia
Este proyecto es con fines educativos para el curso de Estructuras de Datos.

---

**¡Listo! Solo copia y pega TODO esto en tu README.md** y tendrás la documentación completa ✅
