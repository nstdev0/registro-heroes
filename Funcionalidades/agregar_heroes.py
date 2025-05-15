#     Reciba nombre y rol del héroe (input)
from Funcionalidades.validar_heroe import heroe_valido
from Funcionalidades.validar_rol import rol_valido
from typing import List, Dict


# Se define la funcion recibir_heroes, va a retornar una Lista de Diccionarios con valores de tipo string.
def recibir_heroes() -> List[Dict[str, str]]:
    # Se crea una lista de heroes vacia.
    heroes: List[Dict[str, str]] = []

    # Se crea un bucle while, que durara hasta que lo detengamos.
    while True:
        try:
            print("\nIngresa 'menu' para salir del proceso de agregar héroes.")

            nombre: str = input("\nIngresa el nombre del héroe: ")

            # Se convierte el input a minusculas y verificamos si tiene como valor 'menu', en caso coincida, salimos del bucle.
            if nombre.lower() == "menu":
                break
            
            # Se valida si el nombre ingresado esta en la lista de nombres de heroes con la funcion heroe_valido.
            heroe_valido(nombre.lower())
            
            rol: str = input(
                "Ingresa el rol del héroe ('Carry', 'Mid', 'Offlane', 'Support'): "
            )

            # Se convierte el input a minusculas y verificamos si tiene como valor 'salir', en caso coincida, salimos del bucle.
            if rol.lower() == "salir":
                break

            # Se valida si el rol ingresado esta en la lista de roles validos con la funcion rol_valido.
            rol_valido(rol.lower())

            # Se crea un diccionario con los valores del nombre y rol del heroe.
            nuevo_heroe: Dict[str, str] = {"Heroe": nombre.title(), "Rol": rol.title()}

            # Se agrega el diccionario con los datos del heroe a la lista de heroes.
            heroes.append(nuevo_heroe)

            print(
                f"\n> Héroe {nombre.title()} con rol {rol.title()} agregado exitosamente."
            )

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        except KeyboardInterrupt:
            print(f"\nProceso interrumpido por el usuario.")
            break

    return heroes
