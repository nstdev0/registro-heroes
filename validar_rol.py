from typing import List


# Funcion que retorna True si el input existe en la lista lista_roles, en caso contrario, retorna False y levanta una excepcion.
def rol_valido(rol: str) -> bool:
    lista_roles: List[str] = ["carry", "mid", "support", "offlane"]
    if rol in lista_roles:
        return True
    else:
        raise ValueError("El rol del héroe no es válido.")
