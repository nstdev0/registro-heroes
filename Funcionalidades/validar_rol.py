from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

# Funcion que retorna True si el input existe en la lista lista_roles, en caso contrario, retorna False y levanta una excepcion.
def rol_valido(rol: str) -> bool:
    lista_roles: List[str] = os.getenv("LISTA_ROLES", "").split(",")
    if rol in lista_roles:
        return True
    else:
        raise ValueError("El rol del héroe no es válido.")
