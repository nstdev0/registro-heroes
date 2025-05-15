# Guardar heroes en un archivo txt.
from typing import List, Dict


# Se define la funcion guardar_en_archivo, recibe la lista de heroes guardados que retorna agregar_heroes.py.
def guardar_heroes_en_archivo(heroes: List[Dict[str, str]]) -> bool:
    try:
        # Creamos una condicion para verificar si hay heroes en a lista, si no hay, se crea un archivo .txt con contenido "No se han agregado heroes.".
        if not heroes:
            with open("Lista_de_heroes.txt", "w", encoding="utf-8") as archivo:
                archivo.write("No se han agregado Héroes.")
        # En caso de haber heroes en la lista, se crea el archivo .txt y se agregan los heroes con su rol en lineas separadas.
        else:
            # Se usa with para cerrar el archivo automaticamente, se crea el archivo 'Lista_de_heroes.txt' y lo definimos como 'archivo'.
            with open("Lista_de_heroes.txt", "w", encoding="utf-8") as archivo:
                # Se recorre la lista para cada diccionario en la lista.
                for heroe in heroes:
                    # definimos linea, se accede a cada valor del diccionario. cada linea va a ser igual a un string que contiene el nombre del heroe y su rol.
                    linea = f"Héroe: {heroe["Heroe"]}, Rol: {heroe["Rol"]}\n"
                    # Agregamos el valor de linea al archivo.
                    archivo.write(linea)
        return True
    except Exception:
        return False
