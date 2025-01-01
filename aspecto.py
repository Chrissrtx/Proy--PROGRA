def crear_tablero(n):

    tablero=[]
    for f in range(1,2*n+2):
        temp=[]
        if f==1:
            for j in range(1, 2*n+2):
                if j%2==0: temp.append('_')
                else: temp.append(' ')
            tablero.append(temp)
            continue 
        if f==2*n+1:
            for j in range(1, 2*n+2):
                if j%2==0: temp.append('‾')
                else: temp.append(' ')
            tablero.append(temp)
            continue 
        if f%2==0:
            for j in range(1, 2*n+2):
                if j%2==0: temp.append(' ')
                else: temp.append('|')
            tablero.append(temp)
        else: 
            for j in range(1, 2*n+2):
                if j%2==0: temp.append('—')
                else: temp.append('+')
            tablero.append(temp)
    return tablero


def mostrar_tablero(tablero):
    for f in tablero:
        for i in range(len(f)):
            if i == len(f) - 1:
                print(f[i], end='\n')
            else:
                print(f[i], end='  ')