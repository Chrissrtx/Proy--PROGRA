from modos import modo_multijugador, tutorial, modo_localhard
from jugabilidad import cargar_partida
from aspecto import mostrar_tablero

def menu_principal():
    while True:
        print("¡Bienvenidos al TicTacToe del grupo 2!"+'\n')
        print('•'*30+' MENU PRINCIPAL '+'•'*30)
        print("[1] Nuevo juego")
        print("[2] Cargar juego")
        print("[3] Salir")

        while True:
            try:
                opcion=int(input("Digite opción: "))
                if opcion==3:
                    print("¡Gracias por jugar! Saliendo del juego...")
                    exit()
                if opcion not in [1,2,3]:
                    print("Debe ingresar una opción valida\n")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")      


        if opcion==1:
            print("¡Bienvenidos al TicTacToe del grupo 2!"+'\n')
            print('•'*30+' MENU PRINCIPAL '+'•'*30)
            print("Modos de juego: ")
            print("[1] Multiplayer")
            print("[2] Local")
            
            while True:
                modo_de_juego=input("Ingrese el modo [Solo 1 o 2]: ")
                try:
                    modo_de_juego = int(modo_de_juego)  # Intentamos convertir la entrada a entero
                    if modo_de_juego==1 or modo_de_juego==2:
                        break  # Salimos del bucle si es válido
                    else:
                        print(  "Debe ingreser un modo de juego valido"+'\n')
                except ValueError:
                    print(  "Debe ingreser un modo de juego valido"+'\n')
            
            print('•'*30+'MENU PRINCIPAL'+'•'*30)
            while True:
                n=input("Ingrese el formato del tablero [Solo 3 o 4]: ")
                try:
                    n = int(n)  # Intentamos convertir la entrada a entero
                    if n==3 or n==4:
                        break  # Salimos del bucle si es válido
                    else:
                        print("Formato no valido"+'\n')
                except ValueError:
                    print("Formato no valido"+'\n')
            
            print("\n¿Desea ver el tutorial antes de iniciar?")
            ver_tutorial=input("[S] Sí / [N] No: ").upper()
            if ver_tutorial=="S":
                tutorial(3)
                input("Presione Enter para continuar...\n")

            tablero2 = [[" " for _ in range(n)] for _ in range(n)]
            if modo_de_juego == 1:
                modo_multijugador(n)
            else:
                modo_localhard(n)

            # Guardar la partida cuando el jugador termina
            #guardar_partida(tablero2,jugadores,turno,"multijugador" if modo_de_juego==1 else "local") 
            
        elif opcion==2:
            tablero,jugadores, turno_actual=cargar_partida("multijugador")
            if tablero is None:
                print("No se pudo cargar la partida")
                continue
            print("Partida carga con éxito. ¡Retomando el juego!\n")
            print("Estado del tablero:")
            mostrar_tablero(tablero)
            print("\nTurno actual: ", turno_actual['Nombre'])
             # Continuar el juego con la partida cargada
            if turno_actual['Simbolo']=='X' and turno_actual['Simbolo']!='O':
                modo_localhard(len(tablero)//2,tablero,jugadores[0], jugadores[1], turno_actual)
            else:
                modo_multijugador(len(tablero)//2,tablero,jugadores[0], jugadores[1], turno_actual)

menu_principal()