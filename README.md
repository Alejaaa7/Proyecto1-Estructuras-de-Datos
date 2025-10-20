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

*AGREGAR FOTICO DE LA ESQUEMATIZACIÓN DE LA INTERFAZ *

El siguiente paso fue realizar la "conexión" entre el backend, realizado en c++, y el frontend (interfaz de Tkinter en python). Para llevar esto a cabo, se generó un archivo compilado (.exe) que se ejecuta desde python, de esta manera se permite al ususario acceder y visualizar las estructuras desde la capa visual generada por python sin necesidad de interactuar directamente con la consola.

*AGREGAR FOTO DE LA INTERFAZ YA LINDA *
