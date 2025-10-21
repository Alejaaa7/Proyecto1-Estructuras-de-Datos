import tkinter as tk

def dibujar_array(canvas, datos, x, y):
    # se configura la paleta que se va a usar
    COLOR_PRINCIPAL = "#005227"    
    COLOR_SECUNDARIO = "#53c7a4"   
    COLOR_FONDO = "#a4fff7"        
    COLOR_TEXTO = "#038554"        
    
    # se calcula el centro
    ancho_elemento = 100
    ancho_total = len(datos) * ancho_elemento
    centro_x = x + ancho_total // 2
    
    # el título:
    canvas.create_text(centro_x, y - 30, text="ARRAY", 
                      font=("Segoe UI", 14, "bold"), fill=COLOR_TEXTO)
    
    if not datos:
        # Array vacío
        vacio_ancho = 300
        canvas.create_rectangle(centro_x - vacio_ancho//2, y, centro_x + vacio_ancho//2, y + 70, 
                              fill=COLOR_FONDO, outline=COLOR_SECUNDARIO, width=3, dash=(4,2))
        canvas.create_text(centro_x, y + 35, text="ARRAY VACÍO", 
                         font=("Segoe UI", 12, "italic"), fill=COLOR_SECUNDARIO)
        return
    
    # dibujar elementos del array
    for i, valor in enumerate(datos):
        elemento_x = x + (i * ancho_elemento)
        
        # elemento del array con fondo claro
        canvas.create_rectangle(elemento_x, y, elemento_x + ancho_elemento, y + 70, 
                              fill=COLOR_FONDO, outline=COLOR_PRINCIPAL, width=3)
        
        # fondo del valor en color fuerte
        canvas.create_rectangle(elemento_x + 8, y + 8, elemento_x + ancho_elemento - 8, y + 42,
                              fill=COLOR_SECUNDARIO, outline=COLOR_PRINCIPAL, width=2)
        
        # valor en blanco sobre el color
        canvas.create_text(elemento_x + ancho_elemento//2, y + 25, text=str(valor), 
                         font=("Segoe UI", 14, "bold"), fill="white")
        
        # índice oscuro
        canvas.create_text(elemento_x + ancho_elemento//2, y + 55, text=f"[{i}]", 
                         font=("Segoe UI", 11, "bold"), fill=COLOR_TEXTO)

    # información del array en gris
    canvas.create_text(centro_x, y + 95, 
                      text=f"Tamaño: {len(datos)} | Acceso directo por índice", 
                      font=("Segoe UI", 10), fill="#666")