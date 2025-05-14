from typing import List, Dict
from menu import mostrar_menu
from agregar_heroes import recibir_heroes
from guardar_heroes import guardar_heroes_en_archivo
from os import system

system("clear")

heroes: List[Dict[str, str]] = []

print("Bienvenido al registro de Héroes de Dota 2.")

while True:

    try:

        mostrar_menu()

        opcion = int(input("\nElige una opción: "))

        if opcion not in [1, 2, 3, 4]:
            raise ValueError("-Opción no válida.")

        try:

            if opcion == 1:
                heroes_agregados: List[Dict[str, str]] = recibir_heroes()
                heroes.extend(heroes_agregados)

            elif opcion == 2:
                if not heroes:
                    print("\nNo hay héroes agregados.")
                else:
                    print(heroes)

            elif opcion == 3:
                guardar_heroes_en_archivo(heroes)

            elif opcion == 4:
                break

        except ValueError:
            ("-Opción no válida.")

    except ValueError:
        print("-Opción no válida.")

    except KeyboardInterrupt:
        print("\n-Proceso interrumpido por el usuario.")
        break
