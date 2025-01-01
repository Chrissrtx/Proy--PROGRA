import ast

def modificar_tablero(tablero, posicion, jugador):
    coordenadas_3x3=[
        (1, 1), (1, 3), (1, 5),
        (3, 1), (3, 3), (3, 5),
        (5, 1), (5, 3), (5, 5)
    ]
    
    coordenadas_4x4=[
    (1, 1), (1, 3), (1, 5), (1, 7),
    (3, 1), (3, 3), (3, 5), (3, 7),
    (5, 1), (5, 3), (5, 5), (5, 7),
    (7, 1), (7, 3), (7, 5), (7, 7)
    ]
    coordenadas=coordenadas_3x3 if len(tablero)==7 else coordenadas_4x4

    x, y=coordenadas[posicion-1]

    if tablero[x][y]!=' ':
        return 0

    tablero[x][y]=jugador['Simbolo']
    return tablero

def ganador(tablero, n_formato):
    if n_formato==3:
        for i in range(1, 6, 2):  
            if tablero[i][1] == tablero[i][3] == tablero[i][5] != " ":
                return tablero[i][1]
        
        for j in range(1, 6, 2):  
            if tablero[1][j] == tablero[3][j] == tablero[5][j] != " ":
                return tablero[1][j]

        if tablero[1][1] == tablero[3][3] == tablero[5][5] != " ":
            return tablero[1][1]

        if tablero[1][5] == tablero[3][3] == tablero[5][1] != " ":
            return tablero[1][5]
    else:
        for i in range(1, 8, 2):
            if tablero[i][1] == tablero[i][3] == tablero[i][5] == tablero[i][7]!= " ":
                return tablero[i][1]
        
        for j in range(1, 8, 2):
            if tablero[1][j] == tablero[3][j] == tablero[5][j] == tablero[7][j] != " ":
                return tablero[1][j]

        if tablero[1][1] == tablero[3][3] == tablero[5][5] == tablero[7][7] != " ":
            return tablero[1][1]

        if tablero[1][7] == tablero[3][5] == tablero[5][3] == tablero[7][1] != " ":
            return tablero[1][7]
    for fila in range(1, len(tablero), 2):  
        for col in range(1, len(tablero[fila]), 2):  
            if tablero[fila][col] == " ":
                return None  
    return "EMPATE"
def guardar_partida(tablero, jugadores, turno_actual, n,archivo="partida_guardada.txt"):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            # Escribir dimensiones del tablero
            f.write(f"{n}"+'\n')
            # Escribir turno actual
            f.write(f"{turno_actual}"+'\n')
            # Escribir jugadores
            for jugador in jugadores:
                f.write(f"{jugador['Nombre']},{jugador['Simbolo']}\n")
            f.write("-" * 10 + "\n")
            # Escribir tablero
            f.write(f"{tablero}"+'\n')
        print("\nLa partida se guardó con éxito!!!")
    except Exception as e:
        print(f"\nError al guardar la partida: {e}")

def cargar_partida(archivo):
    archivo="partida_guardada.txt"
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            # Leer dimensiones del tablero
            n = int(f.readline().strip())
            # Leer turno actual
            turno_actual = ast.literal_eval((f.readline().strip()))
            # Leer jugadores
            jugadores = []
            while True:
                linea = f.readline().strip()
                if linea == "-" * 10:
                    break
                nombre, simbolo = linea.split(",")
                jugadores.append({"Nombre": nombre, "Simbolo": simbolo})
            # Leer tablero
            tablero=ast.literal_eval((f.readline().strip()))
        print("\nLa partida se ha cargado correctamente.")
        return tablero, jugadores, turno_actual
    except FileNotFoundError:
        print("\nNo se encontró ninguna partida guardada.")
        return None, None, None
    except Exception as e:
        print(f"\nError al cargar la partida: {e}")
        return None,None,None