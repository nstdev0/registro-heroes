#     Los guarde en un archivo
from typing import List, Dict


def guardar_heroes_en_archivo(heroes: List[Dict[str, str]]) -> None:
    if not heroes:
        with open("Lista_de_heroes.txt", "w", encoding="utf-8") as archivo:
            archivo.write("No se han agregado Héroes.")
    else:
        with open("Lista_de_heroes.txt", "w", encoding="utf-8") as archivo:
            for heroe in heroes:
                linea = f"Héroe: {heroe["Heroe"]}, Rol: {heroe["Rol"]}\n"
                archivo.write(linea)
