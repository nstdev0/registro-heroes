import os

def limpiar_consola() -> None:
    """Limpia la consola según el sistema operativo."""
    comando: str = "cls" if os.name == "nt" else "clear"
    os.system(comando)

if __name__ == "__main__":
    limpiar_consola()
