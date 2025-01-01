from aspecto import crear_tablero, mostrar_tablero
from random import randint, choice
from jugabilidad import modificar_tablero, ganador, guardar_partida
from Minimax import mejor_movimiento3, mejor_movimiento4

def modo_multijugador(n_formato, tablero=None, jugador1=None, jugador2=None, jugador_actual=None):
    if jugador1==None and jugador2== None: #Valida en caso de ser una partida nueva
        jugador1= {'Nombre':input("Jugador 1 [X], Ingrese su nombre: "), 'Simbolo': 'X'} #Pide le nonmbre a los jugadores
        jugador2= {'Nombre':input("Jugador 2 [O], Ingrese su nombre: "), 'Simbolo': 'O'}
        jugadores = [jugador1]
        quien_inicia= choice(jugadores) #Elige que jugador inicia
    if tablero==None: #Valida en caso de ser una partida nueva
        tablero=crear_tablero(n_formato) #Crea el tablero
        print(f"¡Inicia {quien_inicia['Nombre']}!")
        jugador_actual=quien_inicia
    mostrar_tablero(tablero) #Muestra el tablero
    
    for turno in range(n_formato**2):
        if turno>0:
            print(f"Turno de {jugador_actual['Nombre']}")
        
        while True:
                jugada=input("Ingresa el numero de casilla en el que vas a jugar o Salir[E] o Guardar[S] ")
                try:
                    if jugada=='s' or jugada=='S': #Valida si el jugador desea guardar su partida, para luego salir
                        print("Guardando partida...")
                        guardar_partida(tablero, jugadores, jugador_actual, n_formato)
                        exit()
                    if jugada=='e' or jugada=='E': #Valida si el jugador desea salir, pero antes le pregunta si desea guardar
                        print("\n¿Seguro desea salir sin guardar?")
                        confirmacion=input("[S] Sí / [N] No: ").upper()
                        if confirmacion=="S":
                            print("¡Gracias por jugar! Saliendo del juego...")
                            exit()
                        else:
                            guardar_partida(tablero, jugadores, jugador_actual, n_formato)
                            
                        
                    jugada = int(jugada)  # Intentamos convertir la entrada a entero
                    if 1 <= jugada <= n_formato**2:
                        break  # Salimos del bucle si es válido
                    else:
                        print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                except ValueError: #Controla que no de error en caso el input sea un string
                    print('\n'+"¡Debe ingresar posicion valida!"+'\n')
        
        tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
        if tablero_modificado==0: #Controla que haya echo una jugada en una casilla vacia
            print('\n'+"La casilla está ocupada, ingrese un numero de casilla valido"+'\n')
            while tablero_modificado==0: #Controla el input hasta que se ingrese un numero de casilla valido
                while True:
                    jugada=input("Ingresa el numero de casilla en el que vas a jugar o Salir[E]: ")
                    try:
                        if jugada=='e' or jugada=='E': #Pregunta en cada input si desea salir del juego
                            print("\n¿Seguro desea salir sin guardar?")
                            confirmacion=input("[S] Sí / [N] No: ").upper()
                            if confirmacion=="S":
                                print("¡Gracias por jugar! Saliendo del juego...")
                                exit()
                            else:
                                guardar_partida(tablero, jugadores, jugador_actual, n_formato)
                        jugada = int(jugada)  # Intentamos convertir la entrada a entero
                        if 1 <= jugada <= n_formato**2:
                            break  # Salimos del bucle si es válido
                        else:
                            print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                    except ValueError: #Controla que no de error en caso el input sea un string
                        print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual) #Modifica el tablero
            mostrar_tablero(tablero_modificado) #Muestra el tablero despues de la modicación
            
            if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']:#Valida si hay un ganador
                print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                print("¡Gracias por jugar!")
                break #Si hay un ganador termina el bucle
            if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper()
                    if confirmacion=="S": #Confirma si el jugador desea salir
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
            print('-'*50)
                
        else:
            mostrar_tablero(tablero_modificado) #Mueestra el tablero
            
            if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']: #valida si hay un ganador
                print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                print("¡Gracias por jugar!")
                break #Si hay ganador, rompe el bucle y termina
            if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper()
                    if confirmacion=="S": #Confirma si el jugador desea salir
                        print("¡Gracias por jugar! Saliendo del juego...")
            print('-'*50)
        
        jugador_actual=jugador1 if jugador_actual ==jugador2 else jugador2 #Intercambia de turno
        
def tutorial(n_formato): #Imprime un tutorial para guiar al jugador
    print("Para indicar la casilla que desea jugar puede guiarse del siguiente ejempplo, en el caso del formato 4x4, sigue la misma logica hasta 16")
    tablero=crear_tablero(n_formato)
    coordenadas_3x3=[
        (1, 1), (1, 3), (1, 5),
        (3, 1), (3, 3), (3, 5),
        (5, 1), (5, 3), (5, 5)
    ]
    coordenadas=coordenadas_3x3
    for posicion in range(1, len(coordenadas)+1): #Gnera e imprime el tablero con numeros guia
        x, y=coordenadas[posicion-1]
        tablero[x][y]=posicion
    
    mostrar_tablero(tablero)

#El modo de juego local tradicional pero ahora la IA hace jugadas optimas y estrategicas
def modo_localhard(n_formato,tablero=None, jugador1=None, jugador2=None, jugador_actual=None):
    if jugador1==None and jugador2== None: #Valida en caso de ser una partida nueva
        jugador1= {'Nombre':input("Jugador 1 [X], Ingrese su nombre: "), 'Simbolo': 'X'}
        jugador2= {'Nombre': 'La maquina', 'Simbolo': 'O'}
        jugadores = [jugador2]
        quien_inicia= choice(jugadores)
    if tablero==None: #Valida en caso de ser una partida nueva
        tablero=crear_tablero(n_formato)
        print(f"¡Inicia {quien_inicia['Nombre']}!")
        jugador_actual=quien_inicia
    mostrar_tablero(tablero)
    
    for turno in range(n_formato**2):
        if turno>0:
            print(f"Turno de {jugador_actual['Nombre']}")
        
        if jugador_actual==jugador1:
            while True:
                jugada=input("Ingresa el numero de casilla en el que vas a jugar o Salir[E] o Guardar[S]: ")
                try:
                    if jugada=='s' or jugada=='S': #Valida si el jugador desea guardar su partida, para luego salir
                        print("Guardando partida...")
                        guardar_partida(tablero, jugadores, jugador_actual, n_formato)
                        exit()
                    if jugada=='e' or jugada=='E': #Valida si el jugador desea salir, pero antes le pregunta si desea guardar
                        print("\n¿Seguro desea salir sin guardar?")
                        confirmacion=input("[S] Sí / [N] No: ").upper()
                        if confirmacion=="S":
                            print("¡Gracias por jugar! Saliendo del juego...")
                            exit()
                        else:
                            guardar_partida(tablero, jugadores, jugador_actual, n_formato)
                            exit()
                    jugada = int(jugada)  # Intentamos convertir la entrada a entero
                    if 1 <= jugada <= n_formato**2:
                        break  # Salimos del bucle si es válido
                    else:
                        print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                except ValueError: #Controla que no de error en caso el input sea un string
                    print('\n'+"¡Debe ingresar posicion valida!"+'\n')
            tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
            if tablero_modificado==0: #Controla que haya echo una jugada en una casilla vacia
                print('\n'+"La casilla está ocupada, ingrese un numero de casilla valido"+'\n')
                while tablero_modificado==0: #Controla el input hasta que se ingrese un numero de casilla valido
                    while True:
                        jugada=input("Ingresa el numero de casilla en el que vas a jugar o Salir[E]: ")
                        try:
                            if jugada=='e' or jugada=='E': #Pregunta en cada input si desea salir del juego
                                print("¡Gracias por jugar! Saliendo del juego...")
                                exit()
                            jugada = int(jugada)  # Intentamos convertir la entrada a entero
                            if 1 <= jugada <= n_formato**2:
                                break  # Salimos del bucle si es válido
                            else:
                                print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                        except ValueError: #Controla que no de error en caso el input sea un string
                            print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                    tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual) #Modifica el tablero
                mostrar_tablero(tablero_modificado) #Muestra el tablero despues de la modicación
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']: #Valida si hay un ganador
                    print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                    print("¡Gracias por jugar!") 
                    break #Si hay un ganador termina el bucle
                if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper() 
                    if confirmacion=="S": #Confirma si el jugador desea salir
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
                print('-'*50)
                    
            else:
                mostrar_tablero(tablero_modificado) #Mueestra el tablero
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']: #valida si hay un ganador
                    print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                    print("¡Gracias por jugar!")
                    break #Si hay ganador, rompe el bucle y termina
                if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper()
                    if confirmacion=="S": #Confirma si el jugador desea salir
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
                print('-'*50)
        else:
            if n_formato==3: #Controla que algoritmo de minimax va a usar
                mov = mejor_movimiento3(tablero, n_formato, jugador2['Simbolo'], jugador1['Simbolo']) #Obtiene el movimiendo mas optimo
                tablero_modificado=modificar_tablero(tablero, mov, jugador_actual) #modifica el tablero
                mostrar_tablero(tablero_modificado) #Muestra el tablero ya modificado
                if ganador(tablero_modificado, n_formato) == jugador_actual['Simbolo']: #Verifica si la maquina ha ganado
                    print ('Ha ganado la maquina, perdiste. Mejor suerte la proxima vez')
                    print("¡Gracias por jugar!")
                    break #Rompe el bucle si ha ganado
                if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    exit()
            else:
                profundidad_algoritmo=5 #En caso de ser la matriz 4x4, se limita la complejidad de ejecución con 4
                mov = mejor_movimiento4(tablero, n_formato, jugador2['Simbolo'], jugador1['Simbolo'], profundidad_algoritmo) #Se obtiene el movimiento mas optimo
                tablero_modificado=modificar_tablero(tablero, mov, jugador_actual) #modifica el tablero
                mostrar_tablero(tablero_modificado) #Muestra el tablero ya modificado
                if ganador(tablero_modificado, n_formato) == jugador_actual['Simbolo']:  #Verifica si la maquina ha ganado
                    print ('Ha ganado la maquina, perdiste. Mejor suerte la proxima vez')
                    print("¡Gracias por jugar!")
                    break #Rompe el bucle si ha ganado
                if ganador(tablero_modificado, n_formato)=='EMPATE': #Controla si hay un empate
                    print("!Es un empate")
                    exit()
        jugador_actual=jugador1 if jugador_actual ==jugador2 else jugador2 #Intercambia de turno

def modo_local(n_formato):
    jugador1= {'Nombre':input("Jugador 1 [X], Ingrese su nombre: "), 'Simbolo': 'X'}
    jugador2= {'Nombre': 'La maquina', 'Simbolo': 'O'}

    tablero=crear_tablero(n_formato)
    mostrar_tablero(tablero)
    print(f"¡Inicia {jugador1['Nombre']}!")
    jugador_actual=jugador1
    for turno in range(n_formato**2):
        if turno>0:
            print(f"Turno de {jugador_actual['Nombre']}")
        if jugador_actual==jugador1:
            while True:
                jugada=input("Ingresa el numero de casilla en el que vas a jugar o Salir[E]")
                if jugada=='e' or jugada=='E':
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
                try:
                    jugada = int(jugada)  # Intentamos convertir la entrada a entero
                    if 1 <= jugada <= n_formato**2:
                        break  # Salimos del bucle si es válido
                    else:
                        print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                except ValueError:
                    print('\n'+"¡Debe ingresar posicion valida!"+'\n')
            tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
            if tablero_modificado==0:
                print('\n'+"La casilla está ocupada, ingrese un numero de casilla valido"+'\n')
                while tablero_modificado==0:
                    while True:
                        jugada=input("Ingresa el numero de casilla en el que vas a jugar: ")
                        try:
                            jugada = int(jugada)  # Intentamos convertir la entrada a entero
                            if 1 <= jugada <= n_formato**2:
                                break  # Salimos del bucle si es válido
                            else:
                                print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                        except ValueError:
                            print('\n'+"¡Debe ingresar posicion valida!"+'\n')
                    tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
                mostrar_tablero(tablero_modificado)
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']:
                    print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                    print("¡Gracias por jugar!")
                    break
                if ganador(tablero_modificado, n_formato)=='EMPATE':
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper()
                    if confirmacion=="S":
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
                print('-'*50)
                    
            else:
                mostrar_tablero(tablero_modificado)
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']:
                    print (f'Ha ganado {jugador_actual['Nombre']}. ¡FELICIDADES!')
                    print("¡Gracias por jugar!")
                    break
                if ganador(tablero_modificado, n_formato)=='EMPATE':
                    print("!Es un empate")
                    print("\nDesea salir?")
                    confirmacion=input("[S] Sí / [N] No: ").upper()
                    if confirmacion=="S":
                        print("¡Gracias por jugar! Saliendo del juego...")
                        exit()
                
                print('-'*50)
            jugador_actual=jugador1 if jugador_actual ==jugador2 else jugador2
        else: 
            jugada=randint(1,(n_formato**2))
            tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
            if tablero_modificado==0:
                while tablero_modificado==0:
                    jugada=randint(1,(n_formato**2))
                    tablero_modificado=modificar_tablero(tablero, jugada, jugador_actual)
                mostrar_tablero(tablero_modificado)
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']:
                    print (f'Ha ganado la maquina, perdiste. Mejor suerte la proxima vez')
                    print("¡Gracias por jugar!")
                    break
                print('-'*50)
                    
            else:
                mostrar_tablero(tablero_modificado)
                print('-'*50)
                if ganador(tablero_modificado, n_formato)==jugador_actual['Simbolo']:
                    print (f'Ha ganado la maquina, perdiste. Mejor suerte la proxima vez')
                    print("¡Gracias por jugar!")
                    break
            jugador_actual=jugador1 if jugador_actual ==jugador2 else jugador2
        if turno==n_formato**2:
            print("¡Es un empate!")
