#     Reciba nombre y rol del héroe (input)
from validar_heroe import heroe_valido
from validar_rol import rol_valido
from typing import List, Dict


def recibir_heroes() -> List[Dict[str, str]]:

    heroes: List[Dict[str, str]] = []

    while True:

        try:

            print("\nIngresa 'menu' para salir del proceso de agregar héroes.")

            nombre: str = input("\nIngresa el nombre del héroe: ")

            if nombre.lower() == "menu":
                break

            heroe_valido(nombre.lower())

            rol: str = input(
                "Ingresa el rol del héroe ('Carry', 'Mid', 'Offlane', 'Support'): "
            )

            if rol.lower() == "salir":
                break

            rol_valido(rol.lower())

            nuevo_heroe: Dict[str, str] = {"Heroe": nombre.title(), "Rol": rol.title()}

            heroes.append(nuevo_heroe)

            print(
                f"> Héroe {nombre.title()} con rol {rol.title()} agregado exitosamente."
            )

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        except KeyboardInterrupt:
            print(f"\nProceso interrumpido por el usuario.")
            break

    return heroes
