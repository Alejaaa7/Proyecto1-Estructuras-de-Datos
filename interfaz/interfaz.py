import tkinter as tk # aquí se importan las librerías
from tkinter import ttk
import subprocess # para poder ejecutar el archivo C++
import os # para las rutas
import sys 
import re # expresiones regulares

# se configuran los paths 
# guarda la carpeta del script acual:
current_dir = os.path.dirname(os.path.abspath(__file__)) 
# se agregan rutas al path, al script actual, y a las subcarpetas 
# visualizaciones y utils
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'visualizaciones'))
sys.path.append(os.path.join(current_dir, 'utils'))

try: # para intentar importar los módulos
    # convertir la salida del programa de C++ en estructuras de datos de python
    from utils.parser import parsear_salida 
    # traer las funciones para visualizar gráficamente:
    from visualizaciones.lista_visual import dibujar_lista
    from visualizaciones.pila_visual import dibujar_pila
    from visualizaciones.cola_visual import dibujar_cola
    from visualizaciones.arreglo_visual import dibujar_array
    MODULOS_CARGADOS = True # se verifica que todo esté listo
    # se van a empezar a usar mensajes de depuración para verificar los 
    # procesos y los errores (que no haya, o si hay)
    print("DEBUG: Módulos de visualización cargados correctamente")
except ImportError as e:
    MODULOS_CARGADOS = False
    print(f"DEBUG: Error cargando módulos: {e}")

class VisualizadorEstructuras: # se crea la clase principal
    def __init__(self, root): # recibe root
        self.root = root # que es la ventana principal del Tkinter
        self.root.title("Visualizador de Estructuras de Datos") # título barra
        self.root.geometry("1600x1200") # tamaño anchoxalto
        
        # Variables de estado
        self.estructura_actual = "LIST"  # Por defecto Lista
        
        # primero canvas de fondo
        self.crear_canvas_fondo() # método imagen de fondo

        # luego crear controles
        self.crear_controles()  # método para los controles
        
        self.actualizar_codigo_ejemplo() # método para los códigos ej
        print("DEBUG: interfaz creada")
            
    def crear_controles(self): 
        # crear las áreas clickeables

        # editor de código (ventana izquierda)
        # se crea widget de tipo text, para escribir varias líneas
        self.editor_codigo = tk.Text(self.root, font=("Consolas", 12),
                                     bg="white", fg="black", insertbackground="black")
        # se ubica en el cuadro del dibujo (el que simula una ventana delgada)
        self.editor_codigo.place(x=105, y=245, width=530, height=365)

        # canvas para visualización (área derecha)
        # se crea un canvas, de fondo blanco
        self.canvas_visual = tk.Canvas(self.root, width=681, height=408,
                                       bg="white", highlightthickness=0)
        # y también se ubica en el cuadro correspondiente
        self.canvas_visual.place(x=753, y=263)

        # etiqueta temporal en el canvas de visualización, mientras no haya 
        # alguna visualización activa
        self.canvas_visual.create_text(343, 207, 
                                      text="Aquí se verán las estructuras\n\nHaz click en EJECUTAR",
                                      font=("Arial", 12), fill="gray", justify=tk.CENTER)

        # entrada de valor, para escribir solo una línea de texto (.Entry)
        # para escribir el valor de añadir o quitar a la estructura
        self.entrada_valor = tk.Entry(self.root, font=("Segoe UI", 12),
                                      width=10, justify="center")
        self.entrada_valor.place(x=305, y=666, width=300, height=20)
        # la inicializa vacía
        self.entrada_valor.insert(0, "")
    
    def crear_canvas_fondo(self): 
        # crear el canvas con imagen que se diseñó para la interfaz
        # se empieza creando un canvas del tamaño de toda la ventana    eliminar borde gris
        self.canvas_fondo = tk.Canvas(self.root, width=1720, height=1080, highlightthickness=0)
        self.canvas_fondo.place(x=0, y=0) # se ubica en la esquina superior izquierda
        
        try: # se va a intentar cargar la imagen de fondo
            # se asegura de usar la línea correcta
            bg_path = os.path.join(current_dir, "diseño_interfazFINAL.png")
            # se dibuja la imagen en el canvas y se ancla a la esquina izquierda arriba
            self.bg_image = tk.PhotoImage(file=bg_path) 
            self.canvas_fondo.create_image(0, 0, anchor="nw", image=self.bg_image)
            print("DEBUG: Imagen cargada correctamente") # confirmar
            
            # ZONAS CLICKEABLES PARA ESTRUCTURAS:

            # se crea un diccionario que asocie cada tipo de estructura con 
            # las coordenadas en pixeles de su área en la imagen, para darle click
            zonas_click = { 
                "LIST": (111, 130, 141, 150), # se ubican correcta y 
                "STACK": (284, 130, 314, 150), # cuidadoamente
                "QUEUE": (472, 130, 502, 150),
                "ARRAY": (690, 130, 717, 150)
            }

            # se crean rectángulos invisibles pero clickeables
            for tipo, coords in zonas_click.items():
                x1, y1, x2, y2 = coords
                rect = self.canvas_fondo.create_rectangle(x1, y1, x2, y2,
                                                          outline="", fill="", width=0)
                # conecta el rectángulo con una función que se ejecuta al hacer click
                self.canvas_fondo.tag_bind(rect, "<Button-1>",
                                          lambda e, t=tipo: self.seleccionar_estructura(t))

            # ZONA CLICKEABLE PARA BOTÓN EJECUTAR
            x_centro = (1377 + 1109) / 2 # para ponerla en el centro
            y_centro = (111 + 170) / 2   # del botón dibujado

            btn_ejec_texto = self.canvas_fondo.create_text(
                x_centro, y_centro,
                text="EJECUTAR", # poner el texto sobre el botón
                fill="#2F025C",
                font=("Impact", 18, "bold")
            )

            self.canvas_fondo.tag_bind( # se une al método
                btn_ejec_texto,
                "<Button-1>",
                lambda e: self.ejecutar_codigo()
            )

            # coordenadas para botones de operaciones
            zonas_operaciones = {
                "AGREGAR": (1027, 688, 1084, 743),
                "ELIMINAR": (1116, 688, 1170, 743),
                "VACIAR": (1204, 688, 1260, 743)
            }

            # crear rectángulos invisibles para los botones de operaciones
            for operacion, coords in zonas_operaciones.items():
                x1, y1, x2, y2 = coords
                rect = self.canvas_fondo.create_rectangle(x1, y1, x2, y2,
                                                          outline="", fill="", width=0)
                self.canvas_fondo.tag_bind(rect, "<Button-1>", 
                                           lambda e, op=operacion: self.ejecutar_operacion_desde_boton(op))

        except Exception as e:
            print(f"DEBUG: Error cargando imagen: {e}")
            self.canvas_fondo.configure(bg="#2c3e50")
            
        self.canvas_fondo.lower('all')
    
    # se ejecuta cuando el usuraio selecciona un tipo de estructura
    def seleccionar_estructura(self, tipo):
        self.estructura_actual = tipo # guarda el tipo de estructura
        # hace que el editor muestre un código ejemplo de la seleccionada
        self.actualizar_codigo_ejemplo()
        print(f"DEBUG: Estructura {tipo} seleccionada")
        self.mostrar_feedback_seleccion(tipo)

    # dibujar un rectángulo alrededor de la seleccionada ( para confirmar)
    def mostrar_feedback_seleccion(self, tipo):
        coords = {
            "LIST": (111, 130, 141, 150),
            "STACK": (284, 130, 314, 150),
            "QUEUE": (472, 130, 502, 150),
            "ARRAY": (690, 130, 717, 150)            
        }

        if hasattr(self, 'feedback_rect'):
            self.canvas_fondo.delete(self.feedback_rect)

        x1, y1, x2, y2 = coords[tipo]
        self.feedback_rect = self.canvas_fondo.create_rectangle(
            x1-5, y1-5, x2+5, y2+5, outline="#FFFFFF", width=2, fill="")
    
    # cargar un código de ejemplo según la estructura que se seleccionó
    def actualizar_codigo_ejemplo(self):
        ejemplos = {
            "LIST": """// Ejemplo de Lista
List miLista;
miLista.insertAtEnd(5);
miLista.insertAtEnd(10);
miLista.insertAtEnd(15);
miLista.display();""",
            
            "STACK": """// Ejemplo de Pila
Stack miPila;
miPila.push(30);
miPila.push(20);
miPila.push(10);
miPila.display();""",
            
            "QUEUE": """// Ejemplo de Cola
Queue miCola;
miCola.enqueue(100);
miCola.enqueue(200);
miCola.enqueue(300);
miCola.display();""",
            
            "ARRAY": """// Ejemplo de Arreglo
Array miArray(3);
miArray.set(0, 1000);
miArray.set(1, 2000);
miArray.set(2, 3000);
miArray.display();"""
        }
        
        # borra el contenido actual:
        self.editor_codigo.delete("1.0", tk.END)
        # e inserta el correspondiente
        self.editor_codigo.insert("1.0", ejemplos[self.estructura_actual])
        print(f"DEBUG: Código ejemplo actualizado para {self.estructura_actual}")

    # dibujar la pila de forma sencilla
    # si no hay datos pone pila vacía
    # esta es una versión por si acaso no se puede la oficial
    def dibujar_pila_simple(self, datos, x, y):
        # Versión simple de pila
        if not datos:
            self.canvas.create_text(x + 50, y + 50, text="PILA VACÍA", 
                            font=("Segoe UI", 10), fill="#42A5F5", style="italic")
            return
        
        # Título
        self.canvas_visual.create_text(x + 50, y - 20, text="PILA", 
                                    font=("Segoe UI", 11, "bold"), fill="#0D47A1")
        
        for i, valor in enumerate(reversed(datos)):
            elem_y = y + (i * 35)
            self.canvas_visual.create_rectangle(x, elem_y, x + 100, elem_y + 30, 
                                            fill="#42A5F5", outline="#1976D2", width=2)
            self.canvas_visual.create_text(x + 50, elem_y + 15, text=str(valor), 
                                        font=("Segoe UI", 10, "bold"), fill="white")

    # lo mismo aquí
    def dibujar_cola_simple(self, datos, x, y):
        """Versión simple de cola aesthetic"""
        if not datos:
            self.canvas_visual.create_text(x + 100, y + 50, text="COLA VACÍA", 
                                        font=("Segoe UI", 10), fill="#42A5F5", style="italic")
            return
        
        # Título
        self.canvas_visual.create_text(x + 150, y - 20, text="COLA", 
                                    font=("Segoe UI", 11, "bold"), fill="#0D47A1")
        
        for i, valor in enumerate(datos):
            elem_x = x + (i * 70)
            self.canvas_visual.create_rectangle(elem_x, y, elem_x + 60, y + 40, 
                                            fill="#42A5F5", outline="#1976D2", width=2)
            self.canvas_visual.create_text(elem_x + 30, y + 20, text=str(valor), 
                                        font=("Segoe UI", 10, "bold"), fill="white")

    # método principal al presionar ejecutar
    # es una visualización sin ejecución, para interpretar el texto y generar 
    # una visualización coherente
    def ejecutar_codigo_usuario(self):
        # Versión OPTIMIZADA que analiza el código sin compilar
        try:
            print("DEBUG: Ejecutando código del usuario (modo rápido)...")
            
            # Limpiar canvas
            self.canvas_visual.delete("all")
            
            # 1. Obtener código del usuario (texto que puso en el editor)
            codigo_usuario = self.editor_codigo.get("1.0", tk.END).strip()
            print(f"DEBUG: Analizando código usuario...")
            
            # 2. Analizar QUÉ quiere hacer el usuario
            acciones = self.analizar_acciones_usuario(codigo_usuario)
            print(f"DEBUG: Acciones detectadas: {acciones}")
            
            # 3. Generar datos de ejemplo BASADOS en el código del usuario
            datos_ejemplo = self.generar_datos_desde_codigo(acciones)
            print(f"DEBUG: Datos generados: {datos_ejemplo}")
            
            # 4. Mostrar visualización INMEDIATA (sin compilar)
            self.mostrar_visualizacion_instantanea(datos_ejemplo)
            
        except Exception as e:
            print(f"DEBUG: Error: {e}")
            self.canvas_visual.create_text(343, 207, 
                text=f"Error: {str(e)}", 
                font=("Arial", 12), fill="red", justify=tk.CENTER)

    # analizar línea por línea lo que escriba el usuario
    # analiza qué estructura usa, qué operaciones se realizan, 
    # y qué valores se agregan o eliminan
    def analizar_acciones_usuario(self, codigo):

        acciones = {
            "LIST": {"operaciones": [], "valores": []},
            "STACK": {"operaciones": [], "valores": []}, 
            "QUEUE": {"operaciones": [], "valores": []},
            "ARRAY": {"operaciones": [], "valores": []}
        }
        
        lineas = codigo.split('\n') # divide el código en líneas
        
        # Variables para rastrear la última estructura declarada
        ultima_estructura = None
        
        for linea in lineas:
            linea = linea.strip()
            
            if not linea or linea.startswith("//"): # elimina los comentarios
                continue
                
            print(f"DEBUG Procesando línea: {linea}")
            
            # Detectar DECLARACIONES de estructuras
            if "List" in linea:
                print(f"DEBUG: Detectada declaración de Lista")
                ultima_estructura = "LIST"
            elif "Stack" in linea:
                print(f"DEBUG: Detectada declaración de Pila")  
                ultima_estructura = "STACK"
            elif "Queue" in linea:
                print(f"DEBUG: Detectada declaración de Cola")
                ultima_estructura = "QUEUE"
            elif "Array" in linea:
                print(f"DEBUG: Detectada declaración de Array")
                ultima_estructura = "ARRAY"
            
            # Detectar OPERACIONES en cualquier línea
            if ultima_estructura == "LIST":
                # busca e identifica los métodos comunes
                if "insertAtEnd" in linea or "insertAtBeginning" in linea or "insert" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None:
                        print(f"DEBUG: Lista - insertar {valor}")
                        acciones["LIST"]["operaciones"].append("insertar")
                        acciones["LIST"]["valores"].append(valor)

                # En la parte de LISTA - agregar feedback
                elif "removeValue" in linea or "removeAt" in linea or "remove" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None:
                        print(f"DEBUG: Lista - intentando eliminar {valor}")
                        if valor in acciones["LIST"]["valores"]:
                            acciones["LIST"]["operaciones"].append("eliminar")
                            acciones["LIST"]["valores"].remove(valor)
                            print(f"DEBUG: Valor {valor} eliminado de lista")
                        else:
                            print(f"DEBUG: Valor {valor} no existe en lista - no se puede eliminar")
                            # Podemos mostrar un mensaje aquí
            
            elif ultima_estructura == "STACK":
                if "push" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None:
                        print(f"DEBUG: Pila - push {valor}")
                        acciones["STACK"]["operaciones"].append("push")
                        acciones["STACK"]["valores"].append(valor)
                elif "pop" in linea:
                    print(f"DEBUG: Pila - pop")
                    acciones["STACK"]["operaciones"].append("pop")
                    if acciones["STACK"]["valores"]:
                        acciones["STACK"]["valores"].pop()
            
            elif ultima_estructura == "QUEUE":
                if "enqueue" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None:
                        print(f"DEBUG: Cola - enqueue {valor}")
                        acciones["QUEUE"]["operaciones"].append("enqueue")
                        acciones["QUEUE"]["valores"].append(valor)
                elif "dequeue" in linea:
                    print(f"DEBUG: Cola - dequeue")
                    acciones["QUEUE"]["operaciones"].append("dequeue")
                    if acciones["QUEUE"]["valores"]:
                        acciones["QUEUE"]["valores"].pop(0)
            
            elif ultima_estructura == "ARRAY":
                if "pushBack" in linea or "set" in linea or "insert" in linea or "add" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None:
                        print(f"DEBUG: Array - insertar {valor}")
                        acciones["ARRAY"]["operaciones"].append("insertar")
                        acciones["ARRAY"]["valores"].append(valor)
                elif "remove" in linea or "delete" in linea:
                    valor = self.extraer_valor(linea)
                    if valor is not None and valor in acciones["ARRAY"]["valores"]:
                        print(f"DEBUG: Array - eliminar {valor}")
                        acciones["ARRAY"]["operaciones"].append("eliminar")
                        acciones["ARRAY"]["valores"].remove(valor)
        
        print(f"DEBUG: Acciones finales: {acciones}")
        return acciones

    # extraer el valor numérico de una línea
    def extraer_valor(self, linea):
        # Extrae el valor numérico de una línea de código
        print(f"DEBUG: Extrayendo valor de: {linea}")
        
        # Buscar números entre paréntesis - como push(100), enqueue(10), etc.
        match = re.search(r'\((.*?)\)', linea)
        if match:
            contenido = match.group(1)
            print(f"DEBUG: Contenido entre paréntesis: '{contenido}'")
            
            # Buscar números en el contenido de los paréntesis
            numeros = re.findall(r'\b\d+\b', contenido)
            if numeros:
                # Tomar el último número encontrado (generalmente es el valor)
                valor = int(numeros[-1])
                print(f"DEBUG: Encontrado número: {valor}")
                return valor
        
        # Buscar números después de = 
        match = re.search(r'=\s*(\d+)', linea)
        if match:
            valor = int(match.group(1))
            print(f"DEBUG: Encontrado después de =: {valor}")
            return valor
            
        # Buscar números sueltos en la línea
        numeros = re.findall(r'\b\d+\b', linea)
        if numeros:
            valor = int(numeros[-1])
            print(f"DEBUG: Encontrado número suelto: {valor}")
            return valor
        
        print(f"DEBUG: No se pudo extraer valor")
        return None

    # convierte las acciones detectadas en listas de valores listas para dibujar
    def generar_datos_desde_codigo(self, acciones):
        # Genera datos de ejemplo basados en las acciones del usuario
        datos = {}
        
        # Para Lista - mantener todos los valores insertados
        if acciones["LIST"]["valores"]:
            datos["LIST"] = acciones["LIST"]["valores"]
        
        # Para Pila (LIFO) - usar directamente los valores después de las operaciones
        if acciones["STACK"]["valores"]:
            datos["STACK"] = acciones["STACK"]["valores"]
    
        # Para Cola (FIFO) - usar directamente los valores después de las operaciones
        if acciones["QUEUE"]["valores"]:
            datos["QUEUE"] = acciones["QUEUE"]["valores"]
        
        # Para Array - mantener todos los valores
        if acciones["ARRAY"]["valores"]:
            datos["ARRAY"] = acciones["ARRAY"]["valores"]
        
        return datos

    # dibuja los datos generados en el canvas según estructura
    def mostrar_visualizacion_instantanea(self, datos):
        # Muestra visualización INMEDIATA sin compilar
        self.canvas_visual.delete("all")
        
        if not datos:
            # Mensaje más atractivo para exposición (textp guía)
            self.canvas_visual.create_text(340, 200,
                text="✨ Escribe código C++ y presiona EJECUTAR\n\nEjemplo básico:\nList miLista;\nmiLista.insertAtEnd(5);\nmiLista.insertAtEnd(10);",
                font=("Arial", 13), fill="#555", justify=tk.CENTER)
            return
        
        # Calcular posición inicial CENTRADA
        total_estructuras = len(datos)
        espacio_total = total_estructuras * 180  # Más espacio entre estructuras
        y_inicio = (400 - espacio_total) // 2
        y_pos = max(80, y_inicio)  # No empezar muy arriba
        
        for tipo, valores in datos.items():
            print(f"DEBUG: Dibujando {tipo} con {valores}")
            
            # Centrar horizontalmente según el tipo de estructura
            if tipo in ["LIST", "ARRAY"]:
                # Para estructuras horizontales, centrar según cantidad de elementos
                ancho_estimado = len(valores) * 150
                x_pos = max(100, (681 - ancho_estimado) // 2)
            else:
                # Para pilas/colas (verticales), centrar fijo
                x_pos = 150
            
            if tipo == "LIST" and MODULOS_CARGADOS:
                dibujar_lista(self.canvas_visual, valores, x_pos, y_pos)
                y_pos += 160
            elif tipo == "STACK":
                if MODULOS_CARGADOS:
                    try:
                        dibujar_pila(self.canvas_visual, valores, x_pos, y_pos)
                    except:
                        self.dibujar_pila_simple(valores, x_pos, y_pos)
                else:
                    self.dibujar_pila_simple(valores, x_pos, y_pos)
                y_pos += 160
            elif tipo == "QUEUE":
                if MODULOS_CARGADOS:
                    try:
                        dibujar_cola(self.canvas_visual, valores, x_pos, y_pos)
                    except:
                        self.dibujar_cola_simple(valores, x_pos, y_pos)
                else:
                    self.dibujar_cola_simple(valores, x_pos, y_pos)
                y_pos += 160
            elif tipo == "ARRAY" and MODULOS_CARGADOS:
                dibujar_array(self.canvas_visual, valores, x_pos, y_pos)
                y_pos += 160

    # versión básica para mostrar texto si los módulos gráficos no están cargados
    def mostrar_visualizacion_simple_fallback(self, datos):
        # Visualización simple si no hay módulos
        y = 50
        for tipo, valores in datos.items():
            self.canvas_visual.create_text(343, y, 
                text=f"{tipo}: {valores}",
                font=("Arial", 12, "bold"), fill="darkblue")
            y += 40

    #
    def ejecutar_codigo(self):
        # EJECUCIÓN RÁPIDA - sin compilación
        self.ejecutar_codigo_usuario()


    def operacion_agregar(self):
        # Agrega una línea de código para insertar elemento
        print("DEBUG: Botón AGREGAR presionado") 
        valor = self.entrada_valor.get()
        if not valor or not valor.isdigit():
            print("DEBUG: Valor inválido")
            return
        
        # agrega cada línea de código según estructura:
        if self.estructura_actual == "LIST":
            nueva_linea = f"miLista.insertAtEnd({valor});\n"
        elif self.estructura_actual == "STACK":
            nueva_linea = f"miPila.push({valor});\n"
        elif self.estructura_actual == "QUEUE":
            nueva_linea = f"miCola.enqueue({valor});\n"
        elif self.estructura_actual == "ARRAY":
            nueva_linea = f"miArray.pushBack({valor});\n"
        
        # añade el código en el texto:
        self.insertar_linea_codigo(nueva_linea)
        self.mostrar_feedback_operacion(f"Agregado: {valor}")

    # eliminar un valor dado
    def operacion_eliminar(self):
        print("DEBUG: Botón ELIMINAR presionado") 
        valor = self.entrada_valor.get()
        
        # verificar que se escribió un número
        if not valor or not valor.isdigit():
            self.mostrar_mensaje_error("Ingresa un número válido para eliminar")
            return
        
        valor_num = int(valor)
        
        # 1. Primero verificar si el valor existe en las estructuras actuales
        codigo_actual = self.editor_codigo.get("1.0", tk.END)
        acciones = self.analizar_acciones_usuario(codigo_actual)
        datos_actuales = self.generar_datos_desde_codigo(acciones)
        
        # Verificar si el valor existe en alguna estructura
        valor_existe = False
        for estructura, valores in datos_actuales.items():
            if valor_num in valores:
                valor_existe = True
                break
        
        if not valor_existe:
            self.mostrar_mensaje_error(f"El valor {valor_num} no existe en la estructura")
            return
        
        # 2. Si existe, agregar la línea de código para eliminarlo
        if self.estructura_actual == "LIST":
            if valor and valor.isdigit():
                nueva_linea = f"miLista.removeValue({valor});\n"
            else:
                nueva_linea = "// removeValue() necesita un valor específico\n"
        elif self.estructura_actual == "STACK":
            nueva_linea = f"miPila.pop();\n"
        elif self.estructura_actual == "QUEUE":
            nueva_linea = f"miCola.dequeue();\n"
        elif self.estructura_actual == "ARRAY":
            if valor and valor.isdigit():
                nueva_linea = f"miArray.removeAt({valor});\n"
            else:
                nueva_linea = "// removeAt() necesita un índice\n"
        
        # 3. Insertar la línea y mostrar feedback CORRECTO
        self.insertar_linea_codigo(nueva_linea)
        
        # 4. Ejecutar automáticamente para ver el cambio
        self.ejecutar_codigo()
        
        # 5. Mostrar mensaje de éxito
        self.mostrar_feedback_operacion(f"Eliminado: {valor}")

    def mostrar_mensaje_error(self, mensaje):
        # Muestra un mensaje de error temporal
        self.canvas_visual.delete("all")
        self.canvas_visual.create_text(340, 200, 
                                    text=f"❌ {mensaje}",
                                    font=("Arial", 12, "bold"), fill="red", 
                                    justify=tk.CENTER)
        
        # El mensaje se quita después de 2 segundos
        self.root.after(2000, self.ejecutar_codigo)

    
    def operacion_vaciar(self):
        # Vacía la estructura actual y limpia el editor
        print("DEBUG: Botón VACIAR presionado")
        
        # 1. PRIMERO limpiar el editor completamente
        self.editor_codigo.delete("1.0", tk.END)
        
        # 2. LUEGO poner solo la declaración básica de la estructura
        codigos_base = {
            "LIST": "List miLista;",
            "STACK": "Stack miPila;", 
            "QUEUE": "Queue miCola;",
            "ARRAY": "Array miArray(5);  // Tamaño inicial 5"
        }
        
        codigo_base = codigos_base.get(self.estructura_actual, "")
        self.editor_codigo.insert("1.0", codigo_base)
        
        # 3. Limpiar la entrada de valor
        self.entrada_valor.delete(0, tk.END)
        self.entrada_valor.insert(0, "0")
        
        # 4. Ejecutar automáticamente para mostrar estructura vacía
        self.ejecutar_codigo()
        
        # 5. Mostrar feedback
        self.mostrar_feedback_operacion(f"Estructura {self.estructura_actual} vaciada")

    # para asegurarse de insertar el código en el lugar correcto del editor
    def insertar_linea_codigo(self, nueva_linea):
        # Inserta una línea de código antes del display()
        codigo_actual = self.editor_codigo.get("1.0", tk.END)
        if "display();" in codigo_actual:
            inicio_display = codigo_actual.find("display();")
            posicion_insercion = f"1.0+{inicio_display}c"
            self.editor_codigo.insert(posicion_insercion, nueva_linea)
        else:
            self.editor_codigo.insert(tk.END, f"\n{nueva_linea}")
        
        print(f"DEBUG: Código agregado: {nueva_linea.strip()}")

    # mostrar confirmación visual cuando una operación funciona
    def mostrar_feedback_operacion(self, mensaje):
        # Muestra feedback visual de la operación
        self.canvas_visual.delete("all")
        
        # Fondo de feedback atractivo
        self.canvas_visual.create_rectangle(150, 150, 530, 250, 
                                        fill="#E8F5E8", outline="#4CAF50", width=3)
        
        # Mensaje más atractivo
        self.canvas_visual.create_text(340, 200, 
                                    text=f"✅ {mensaje}",
                                    font=("Arial", 14, "bold"), fill="#2E7D32", 
                                    justify=tk.CENTER)
        
        # El feedback se quita después de 1.5 segundos y ejecuta el código
        self.root.after(1500, self.ejecutar_codigo)

    # conectar los botones de la imagen con las funciones reales
    def ejecutar_operacion_desde_boton(self, operacion):
        print(f"DEBUG: Botón {operacion} presionado")
        self.mostrar_feedback_operacion_btn(operacion)

        if operacion == "AGREGAR":
            self.operacion_agregar()
        elif operacion == "ELIMINAR":
            self.operacion_eliminar()
        elif operacion == "VACIAR":
            self.operacion_vaciar()
    
    def mostrar_feedback_operacion_btn(self, operacion):
        coords_operaciones = {
            "AGREGAR": (1027, 688, 1084, 743),
            "ELIMINAR": (1116, 688, 1170, 743),
            "VACIAR": (1204, 688, 1260, 743)
        }
        
        if hasattr(self, 'feedback_operacion'):
            self.canvas_fondo.delete(self.feedback_operacion)
        
        x1, y1, x2, y2 = coords_operaciones[operacion]
        self.feedback_operacion = self.canvas_fondo.create_rectangle(
            x1-3, y1-3, x2+3, y2+3, outline="#4CAF50", width=2, fill=""
        )

    # mostrar error si se intenta eliminar uno que no existe
    def mostrar_mensaje_error(self, mensaje):
        """Muestra un mensaje de error temporal"""
        self.canvas_visual.delete("all")
        self.canvas_visual.create_text(340, 200, 
                                    text=f"❌ ERROR\n{mensaje}",
                                    font=("Arial", 12, "bold"), fill="red", 
                                    justify=tk.CENTER)

def main():
    root = tk.Tk()
    app = VisualizadorEstructuras(root)
    root.mainloop()

if __name__ == "__main__":
    main()