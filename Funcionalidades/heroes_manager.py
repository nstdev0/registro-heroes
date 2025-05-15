from typing import List, Dict, Optional
from .config import HEROES_VALIDOS, ROLES_VALIDOS, MENSAJES, ARCHIVO_HEROES


class HeroesManager:
    def __init__(self):
        self.heroes: List[Dict[str, str]] = []

    def validar_heroe(self, nombre: str) -> bool:
        """Valida si el héroe existe en la lista de héroes válidos."""
        if nombre.lower() not in HEROES_VALIDOS:
            raise ValueError(MENSAJES["heroe_invalido"])
        return True

    def validar_rol(self, rol: str) -> bool:
        """Valida si el rol es válido."""
        if rol.lower() not in ROLES_VALIDOS:
            raise ValueError(MENSAJES["rol_invalido"])
        return True

    def heroe_existe(self, nombre: str) -> bool:
        """Verifica si el héroe ya existe en la lista."""
        return any(h["Heroe"].lower() == nombre.lower() for h in self.heroes)

    def agregar_heroe(self, nombre: str, rol: str) -> None:
        """Agrega un nuevo héroe a la lista."""
        nombre = nombre.lower()
        rol = rol.lower()

        self.validar_heroe(nombre)
        self.validar_rol(rol)

        if self.heroe_existe(nombre):
            raise ValueError(MENSAJES["heroe_duplicado"])

        self.heroes.append({
            "Heroe": nombre.title(),
            "Rol": rol.title()
        })

    def obtener_heroes(self) -> List[Dict[str, str]]:
        """Retorna la lista de héroes."""
        return self.heroes

    def guardar_en_archivo(self) -> bool:
        """Guarda la lista de héroes en un archivo."""
        try:
            with open(ARCHIVO_HEROES, "w", encoding="utf-8") as archivo:
                if not self.heroes:
                    archivo.write(MENSAJES["no_heroes"])
                else:
                    for heroe in self.heroes:
                        linea = f"Héroe: {heroe['Heroe']}, Rol: {heroe['Rol']}\n"
                        archivo.write(linea)
            return True
        except Exception:
            return False 