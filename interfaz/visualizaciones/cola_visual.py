import tkinter as tk

def dibujar_cola(canvas, datos, x, y):
    # paleta lila
    COLOR_PRINCIPAL = "#4b1c71"    
    COLOR_SECUNDARIO = "#b57edc"   
    COLOR_FONDO = "#fff0ff"        
    COLOR_TEXTO = "#7f4ca5"        
    
    # se calcula el centro
    ancho_elemento = 100
    espacio_entre = 15
    ancho_total = len(datos) * (ancho_elemento + espacio_entre) - espacio_entre
    centro_x = x + ancho_total // 2
    
    # título
    canvas.create_text(centro_x, y - 30, text="COLA (FIFO)", 
                      font=("Segoe UI", 14, "bold"), fill=COLOR_TEXTO)
    
    if not datos:
        # cola vacía
        vacio_ancho = 300
        canvas.create_rectangle(centro_x - vacio_ancho//2, y, centro_x + vacio_ancho//2, y + 70, 
                              fill=COLOR_FONDO, outline=COLOR_SECUNDARIO, width=3, dash=(4,2))
        canvas.create_text(centro_x, y + 35, text="COLA VACÍA", 
                         font=("Segoe UI", 12, "italic"), fill=COLOR_SECUNDARIO)
        return
    
    # se dibujan los elementos de la cola
    for i, valor in enumerate(datos):
        elem_x = x + (i * (ancho_elemento + espacio_entre))
        
        canvas.create_rectangle(elem_x, y, elem_x + ancho_elemento, y + 60, 
                              fill=COLOR_SECUNDARIO, outline=COLOR_PRINCIPAL, width=3)
        
        canvas.create_rectangle(elem_x + 3, y + 3, elem_x + ancho_elemento - 3, y + 57,
                              fill="#CE93D8", outline="")
        
        canvas.create_text(elem_x + ancho_elemento//2, y + 30, 
                         text=str(valor), font=("Segoe UI", 14, "bold"), fill="white")
        
        # indicar frente
        if i == 0:
            canvas.create_text(elem_x + ancho_elemento//2, y + 85, text="FRENTE",
                             font=("Segoe UI", 10, "bold"), fill=COLOR_TEXTO)
        
        # indicar final
        if i == len(datos) - 1:
            canvas.create_text(elem_x + ancho_elemento//2, y + 85, text="FINAL",
                             font=("Segoe UI", 10, "bold"), fill=COLOR_TEXTO)

    # leyenda de flujo
    canvas.create_text(centro_x, y + 110, text="enqueue → → → dequeue",
                     font=("Segoe UI", 11), fill="#666")