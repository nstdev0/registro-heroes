from typing import List
from dotenv import load_dotenv
import os

load_dotenv()


# Funcion que retorna True si el input existe en la lista lista_heroes, en caso contrario, retorna False y levanta una excepcion.
def heroe_valido(heroe: str) -> bool:
    lista_heroes: List[str] = os.getenv("LISTA_HEROES", "").split(",")

    if heroe in lista_heroes:
        return True
    else:
        raise ValueError("El nombre del héroe no es válido.")
