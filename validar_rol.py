from typing import List


def rol_valido(rol: str) -> bool:
    lista_roles: List[str] = ["carry", "mid", "support", "offlane"]
    if rol in lista_roles:
        return True
    else:
        raise ValueError("El rol del héroe no es válido.")
