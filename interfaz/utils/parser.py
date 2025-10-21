def parsear_salida(texto):
    
    # Convierte la salida del C++ en diccionarios con los datos
    
    estructuras = {} # se crea un diccionario
    lineas = texto.strip().split('\n') # se auitan los espacios y se divide por líneas
    
    for linea in lineas: # se recorre cada línea
        if 'LIST:' in linea: # si es lista, 
            # debe quedar: "LIST: 1, 2, 3" → [1, 2, 3]
             # quitar el prefijo y los espacios:
            datos_str = linea.replace('LIST:', '').strip()
            # separar con ',' y convertir a int
            datos = [int(x.strip()) for x in datos_str.split(',')] 
            estructuras['LIST'] = datos # guardar en el diccionario con clave LIST
            
        # se repite para stack y queue
        elif 'STACK:' in linea:
            # "STACK: 30, 20, 10" → [30, 20, 10]  
            datos_str = linea.replace('STACK:', '').strip()
            datos = [int(x.strip()) for x in datos_str.split(',')]
            estructuras['STACK'] = datos
            
        elif 'QUEUE:' in linea:
            # "QUEUE: 100, 200, 300" → [100, 200, 300]
            datos_str = linea.replace('QUEUE:', '').strip()
            datos = [int(x.strip()) for x in datos_str.split(',')]
            estructuras['QUEUE'] = datos
            
        elif 'ARRAY:' in linea:
            # "ARRAY: [1000, 2000, 3000]" → [1000, 2000, 3000]
            datos_str = linea.replace('ARRAY:', '').strip()
            # aquí se tienen que quitar los corchetes
            datos_str = datos_str.replace('[', '').replace(']', '')
            datos = [int(x.strip()) for x in datos_str.split(',')]
            estructuras['ARRAY'] = datos
    
    return estructuras # devolver el diccionario