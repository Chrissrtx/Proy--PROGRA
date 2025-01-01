from jugabilidad import ganador
import math
#Esta función nos permitirá hallar las coordenadas correspondientes a cada numero de las casillas de los tavbleros
def obtener_coordenadas(numero, n_formato):
    if n_formato==3:
        coordenadas= [(1, 1), (1, 3), (1, 5),
         (3, 1), (3, 3), (3, 5),
         (5, 1), (5, 3), (5, 5)]
    elif n_formato==4: 
        coordenadas = [
         (1, 1), (1, 3), (1, 5), (1, 7),
         (3, 1), (3, 3), (3, 5), (3, 7),
         (5, 1), (5, 3), (5, 5), (5, 7),
         (7, 1), (7, 3), (7, 5), (7, 7)]
    return coordenadas[numero - 1]
#Este es el algortimo minimax, debido a que para el tablero 3x3 no es de mucha complejidad, se trabaja con el modelo original
def minimax3(tablero, maximus, n_formato, simbolo_maquina, simbolo_jugador):
    ganador_actual = ganador(tablero, n_formato)
    if ganador_actual == simbolo_maquina: 
        return 1  # CASO LA IA GANA
    elif ganador_actual == simbolo_jugador:
        return -1  # CASO EL JUGADOR GANA
    #AHORA VERIFICAMOS EL EMPATE
    coordenadas = [obtener_coordenadas(i, n_formato) for i in range(1, n_formato**2 + 1)]
    # Verificar si hay al menos una casilla vacía (' ')
    hay_casillas_vacias = any(tablero[x][y] == ' ' for x, y in coordenadas)
    if not hay_casillas_vacias:
        return 0
    #Para evaluar los casos que le convienen a la IA
    if maximus:
        mejor_puntaje = -math.inf
        for numero in range(1, n_formato**2 + 1):
            x, y = obtener_coordenadas(numero, n_formato)
            if tablero[x][y]==' ':  # Verificar si la casilla está vacía
                tablero[x][y] = simbolo_maquina
                puntaje = minimax3(tablero, False, n_formato, simbolo_maquina, simbolo_jugador)
                tablero[x][y] = ' '  # Restaurar la casilla
                mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    #Los casos que le convienen al humano
    else:
        mejor_puntaje = math.inf
        for numero in range(1, n_formato**2 + 1):
            x, y = obtener_coordenadas(numero, n_formato)
            if tablero[x][y] == ' ':  # Verificar si la casilla está vacía
                tablero[x][y] = simbolo_jugador
                puntaje = minimax3(tablero, True, n_formato, simbolo_maquina, simbolo_jugador)
                tablero[x][y] = ' '  # Restaurar la casilla
                mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje
#El algoritmo minimax para 4x4 requiere mucho poder computacional por su complejidad, por lo que se usa alpha, beta y profundidad para limitar el algoritmo 
def minimax4(tablero, maximus, n_formato, simbolo_maquina, simbolo_jugador, alpha, beta, profundidad, profundidadMAX):
    ganador_actual = ganador(tablero, n_formato)
    if ganador_actual == simbolo_maquina:
        return 1  # CASO LA IA GANA
    elif ganador_actual == simbolo_jugador:
        return -1  # CASO EL JUGADOR GANA
    if profundidad==profundidadMAX:
        return 0
    #AHORA VERIFICAMOS EL EMPATE
    coordenadas = [obtener_coordenadas(i, n_formato) for i in range(1, n_formato**2 + 1)]
    # Verificar si hay al menos una casilla vacía (' ')
    hay_casillas_vacias = any(tablero[x][y] == ' ' for x, y in coordenadas)
    if not hay_casillas_vacias:
        return 0
    #Casos que le convienen a la IA
    if maximus:
        mejor_puntaje = -math.inf
        for numero in range(1, n_formato**2 + 1):
            x, y = obtener_coordenadas(numero, n_formato)
            if tablero[x][y]==' ':  # Verificar si la casilla está vacía
                tablero[x][y] = simbolo_maquina
                puntaje = minimax4(tablero, False, n_formato, simbolo_maquina, simbolo_jugador, alpha, beta, profundidad+1, profundidadMAX)
                tablero[x][y] = ' '  # Restaurar la casilla
                mejor_puntaje = max(mejor_puntaje, puntaje)
                alpha = max(alpha, mejor_puntaje)
                if beta <= alpha:  # Poda descartando casos de no mucha importancia
                    break
        return mejor_puntaje
    #Casos que le convienen al humano
    else:
        mejor_puntaje = math.inf
        for numero in range(1, n_formato**2 + 1):
            x, y = obtener_coordenadas(numero, n_formato)
            if tablero[x][y] == ' ':  # Verificar si la casilla está vacía
                tablero[x][y] = simbolo_jugador
                puntaje = minimax4(tablero, True, n_formato, simbolo_maquina, simbolo_jugador,alpha,beta, profundidad+1, profundidadMAX)
                tablero[x][y] = ' '  # Restaurar la casilla
                mejor_puntaje = min(mejor_puntaje, puntaje)
                alpha = min(beta, mejor_puntaje)
                if beta<= alpha:  # Poda descartando casos de no mucha importancia
                    break
        return mejor_puntaje
#Permite saber el mejor movimiento para el tablero 3x3 en base al resultado de minimax
def mejor_movimiento3(tablero, n_formato, simbolo_maquina, simbolo_jugador):
    mejor_puntaje = -math.inf
    mejor_mov = None
    for numero in range(1, n_formato**2 + 1):
        x, y = obtener_coordenadas(numero, n_formato)
        if tablero[x][y]==' ':  # Verificar si la casilla está vacía
            tablero[x][y] = simbolo_maquina
            puntaje = minimax3(tablero, False, n_formato, simbolo_maquina, simbolo_jugador)
            tablero[x][y] = ' '  # Restaurar la casilla
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_mov = numero  # Guardar el número de casilla
    return mejor_mov

#Permite saber el mejor movimiento para el tablero 4x4 en base al resultado de minimax
def mejor_movimiento4(tablero, n_formato, simbolo_maquina, simbolo_jugador, profundidadMAX):
    mejor_puntaje = -math.inf
    mejor_mov = None
    for numero in range(1, n_formato**2 + 1):
        x, y = obtener_coordenadas(numero, n_formato)
        if tablero[x][y]==' ':  # Verificar si la casilla está vacía
            tablero[x][y] = simbolo_maquina
            puntaje = minimax4(tablero, False, n_formato, simbolo_maquina, simbolo_jugador, -math.inf, math.inf, 0, profundidadMAX)
            tablero[x][y] = ' '  # Restaurar la casilla
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_mov = numero  # Guardar el número de casilla
    return mejor_mov
