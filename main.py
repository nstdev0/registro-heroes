from typing import List, Dict
from menu import mostrar_menu
from agregar_heroes import recibir_heroes
from guardar_heroes import guardar_heroes_en_archivo
from os import system

# Se importa os.system para borrar la terminal.
system("clear")

# Se crea una lista vacia de heroes.
heroes: List[Dict[str, str]] = []

print("Bienvenido al registro de Héroes de Dota 2.")

# Se crea un bucle while.
while True:

    try:

        # Se muestra el menu.
        mostrar_menu()

        opcion = int(input("\nElige una opción: "))

        # Se condiciona la opcion al valor de 1, 2, 3 o 4.
        if opcion not in [1, 2, 3, 4]:
            raise ValueError("-Opción no válida.")

        try:
            
            if opcion == 1:
                # Se llama a la funcion recibir_heroes para agregar heroes.
                heroes_agregados: List[Dict[str, str]] = recibir_heroes()
                # Se agregan los heroes a la lista de heroes.
                heroes.extend(heroes_agregados)

            elif opcion == 2:
                # De haber heroes, se muestran en consola.
                if not heroes:
                    print("\nNo hay héroes agregados.")
                else:
                    print(heroes)

            elif opcion == 3:
                # Llamamos a la funcion guardar_heroes_en_archivo para guardar la lista de heroes en un archivo .txt.
                guardar_heroes_en_archivo(heroes)

            # En caso de que la opcion tenga valor de 4, se termina el programa
            elif opcion == 4:
                print("\nPrograma finalizado por el usuario.")
                break

        except ValueError:
            ("-Opción no válida.")

    except ValueError:
        print("-Opción no válida.")

    except KeyboardInterrupt:
        print("\n-Proceso interrumpido por el usuario.")
        break
