import tkinter as tk

def dibujar_pila(canvas, datos, x, y):
    # dibuja una pila 
    
    # título
    canvas.create_text(x + 150, y - 50, text="PILA (LIFO)", 
                      font=("Segoe UI", 18, "bold"), fill="#c93384")
    
    if not datos:
        # pila vacía 
        canvas.create_rectangle(x + 40, y, x + 260, y + 60, 
                              fill="#F6E3FD", outline="#e44f9c", width=3, dash=(4,2))
        canvas.create_text(x + 150, y + 30, text="PILA VACÍA", 
                         font=("Segoe UI", 12, "italic"), fill="#ff69b4")
        return
    
    # base de la pila (más ancha)
    canvas.create_rectangle(x + 20, y + 250, x + 280, y + 265, 
                          fill="#8819D2", outline="#c93384", width=3)
    
    # se dibujan los elementos de la pila
    altura_elemento = 45
    for i, valor in enumerate(reversed(datos)):
        elem_y = y + (len(datos) - i - 1) * altura_elemento
        
        canvas.create_rectangle(x + 50, elem_y, x + 250, elem_y + altura_elemento, 
                              fill="#ff69b4", outline="#e44f9c", width=3)
        
        # se añde sombra interior para efecto 3D
        canvas.create_rectangle(x + 52, elem_y + 2, x + 248, elem_y + altura_elemento - 2,
                              fill="#ff97d9", outline="")
        
        canvas.create_text(x + 150, elem_y + altura_elemento//2, 
                         text=str(valor), font=("Segoe UI", 14, "bold"), fill="white")
        
        # se indica tope en el último elemento
        if i == 0:
            canvas.create_text(x + 255, elem_y + altura_elemento//2, text="← TOPE",
                             font=("Segoe UI", 10, "bold"), fill="#e44f9c", anchor="w")

    canvas.create_line(x + 150, y - 15, x + 150, y, 
                     arrow=tk.LAST, width=3, fill="#c93384")
    canvas.create_text(x + 150, y - 30, text="push/pop", 
                     font=("Segoe UI", 10), fill="#666")