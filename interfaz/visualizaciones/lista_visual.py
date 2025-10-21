import tkinter as tk

def dibujar_lista(canvas, datos, x, y):
    # se dibuja una lista enlazada
    
    # título
    canvas.create_text(x + 200, y - 30, text="LISTA ENLAZADA", 
                      font=("Arial", 18, "bold"), fill="#1565C0")
    

    ancho_nodo = 120    
    alto_nodo = 60      
    espacio_entre_nodos = 150
    
    for i, valor in enumerate(datos):
        nodo_x = x + (i * espacio_entre_nodos)

        # rectángulo principal del nodo
        canvas.create_rectangle(nodo_x, y, nodo_x + ancho_nodo, y + alto_nodo, 
                              fill="#9fffff", outline="#00cbcc", width=3)
        
        # división: parte DATA (izquierda)
        canvas.create_rectangle(nodo_x, y, nodo_x + ancho_nodo//2, y + alto_nodo, 
                              fill="#9fffff", outline="#00cbcc", width=2)
        
        canvas.create_text(nodo_x + (ancho_nodo//4), y + (alto_nodo//2), 
                         text=str(valor), font=("Arial", 16, "bold"), fill="#0D47A1")
        
        # división: parte NEXT (derecha)
        canvas.create_rectangle(nodo_x + ancho_nodo//2, y, nodo_x + ancho_nodo, y + alto_nodo, 
                              fill="#9fffff", outline="#00cbcc", width=2)
        
        # flecha o NULL
        if i < len(datos) - 1:

            canvas.create_text(nodo_x + ancho_nodo//2 + ancho_nodo//4, y + (alto_nodo//2),
                             text=" ", font=("Arial", 18, "bold"), fill="#00cbcc")
            
            # línea conectando 
            canvas.create_line(nodo_x + ancho_nodo, y + (alto_nodo//2),
                             nodo_x + espacio_entre_nodos, y + (alto_nodo//2),
                             arrow=tk.LAST, width=3, fill="#00e5e5")
        else:
            # NULL
            canvas.create_text(nodo_x + ancho_nodo//2 + ancho_nodo//4, y + (alto_nodo//2),
                             text="NULL", font=("Arial", 10, "bold"), fill="#666")