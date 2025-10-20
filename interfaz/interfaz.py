import tkinter as tk
from tkinter import ttk
import subprocess
import os

class VisualizadorEstructuras:
    def __init__(self, root):
        # constructor de la clase, root es la ventana principal de Tkinter
        self.root = root

        # para configurar la ventana principal
        self.root.title("Visualizador de Estructuras de Datos")
        self.root.geometry("800x600") # ancho x alto

        # crear un frame principal para organizar los widgets
        main_frame = ttk.Frame(root, padding="10") # se le da un margen con padding
        # se usa la cuadrícula para posicionarlo, se usa sticky para que ocupe todo
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # botón para ejecutar el programa C++
        self.btn_ejecutar = ttk.Button(
            main_frame, # el botón debe estar dentro del main_frame que se creó
            text="Ejecutar C++ y Visualizar", 
            command=self.ejecutar_y_visualizar # cuando se haga click llamaría a esta función
        )

        self.btn_ejecutar.grid(row=0, column=0, pady=10) # se ubica y se rellena

        # Área de texto para mostrar los resultados del programa C++
        self.texto_resultados = tk.Text(
            main_frame, # otra vez dentro de este
            width=80,
            height=20, # se le define tamaño
            font=("Consolas", 20) # esta fuente para mejor formato
        )
        # colocarlo en la segunda fila, primera columna y rellenar
        self.texto_resultados.grid(row=1, column=0, pady=10)

        # Scrollbar para navegar el texto por si es largo
        scrollbar = ttk.Scrollbar(
            main_frame,
            orient="vertical",
            command=self.texto_resultados.yview 
            # para que al mover la barra, se controle la vista vertical de la 
            # caja de texto
        )

        # colocarlo en la segunda fila, segunda columna y pegarlo al borde 
        # superior e inferior 
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.texto_resultados.configure(yscrollcommand=scrollbar.set)
        # para ir actualizando la posición del thumb
        
    def ejecutar_y_visualizar(self):

        # para ejecutar el programa C++ y mostrar su salida en el área de texto

        try: # se le añaden excepciones
            # limpiar el área de texto antes de mostrar nuevos resultados:
            self.texto_resultados.delete(1.0, tk.END) # del primero al útlimo

            # verificar que el archivo main.exe exista en el mismo directorio
            if not os.path.exists("main.exe"):
                self.texto_resultados.insert(tk.END, "ERROR: " \
                "No se encuentra main.exe\n")
                return
            
            """ ejecutar el programa C++ y capturar su salida, aquí: 
                - subprocess.run ejecuta un comando del sistema
                - capture_output=True: captur la salida estándar y errores
                - text=True devuelve strings en lugar de bytes
                - shell=True usa el shell del sistema para ejecutar el comando"""
            
            resultado = subprocess.run(["../main.exe"], capture_output=True,
                                        text=True, shell=True)
            
            # mostrar  la salida estándar del programa C++ (lo que se ve en consola)

            if resultado.stdout: # si hay contenido en la salida
                # agregar texto en el widget Text
                self.texto_resultados.insert(tk.END, "=== SALIDA DEL PROGRAMA C++ ===\n")
                self.texto_resultados.insert(tk.END, resultado.stdout)

            # mostrar errores si el programa C++ generó
            if resultado.stderr:
                self.texto_resultados.insert(tk.END, "\n=== ERRORES ==\n")
                self.texto_resultados.insert(tk.END, resultado.stderr)

            # mostrar el código de retorno (0 es éxito, los otros son errores)
            if resultado.returncode != 0:
                self.texto_resultados.insert(tk.END, f"\n El programa terminó \
                                             con código: {resultado.returncode}")

        except Exception as e:
            # capturar cualquier error inesperado y mostrarlo
            self.texto_resultados.insert(tk.END, f"ERROR: {str(e)}")

# función que inicia la aplicación
def main():
    # crear la ventana principal de Tkinter
    root = tk.Tk()

    # crear una instancia de la aplicación
    app = VisualizadorEstructuras(root)

    # iniciar el loop principal de Tkinter (la aplicación se queda ejecutando)
    root.mainloop()

# punto de entrada del programa
if __name__ == "__main__":
    main()