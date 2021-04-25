#********* PROYECTO 1 TIC-TAC-TOE ***********

import random   #libreria para generar numeros aleatorios



def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    tablero=board
    for i in range(3):
        print("+-------+-------+-------+")
        for j in range(5):
            if j==2:
                if i==0:
                    print("|  ",tablero[i][i],"  |  ",tablero[i][i+1],"  |  ",tablero[i][i+2],"  |")
                if i==1:
                    print("|  ",tablero[i][i-1],"  |  ",tablero[i][i],"  |  ",tablero[i][i+1],"  |")
                if i==2:
                    print("|  ",tablero[i][i-2],"  |  ",tablero[i][i-1],"  |  ",tablero[i][i],"  |")

            print("|       |       |       |")
    print("+-------+-------+-------+")



def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    tablero=board
    num=int(input("¿que casilla quieres tirar?  __"))
    if num==1:
        tablero[0][0]="O"
    elif num==2:
        tablero[0][1]="O"
    elif num==3:
        tablero[0][2]="O"
    elif num==4:
        tablero[1][0]="O"
    elif num==6:
        tablero[1][2]="O"
    elif num==7:
        tablero[2][0]="O"
    elif num==8:
        tablero[2][1]="O"
    elif num==9:
        tablero[2][2]="O"
    return tablero




def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    tablero=board
    registro=[]
    for i in range(3):
        for j in range(3):
            if tablero[i][j]=="X" or tablero[i][j]=="O":
                continue
            registro.append((i,j))
    return registro




def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    tablero=board
    if sign=="X":
        if ((tablero[0][0]=="X" and tablero[0][1]=="X" and tablero[0][2]=="X") or 
            (tablero[1][0]=="X" and tablero[1][1]=="X" and tablero[1][2]=="X") or 
            (tablero[2][0]=="X" and tablero[2][1]=="X" and tablero[2][2]=="X") or 
            (tablero[0][0]=="X" and tablero[1][0]=="X" and tablero[2][0]=="X") or 
            (tablero[0][1]=="X" and tablero[1][1]=="X" and tablero[2][1]=="X") or 
            (tablero[0][2]=="X" and tablero[1][2]=="X" and tablero[2][2]=="X") or 
            (tablero[0][0]=="X" and tablero[1][1]=="X" and tablero[2][2]=="X") or 
            (tablero[0][2]=="X" and tablero[1][1]=="X" and tablero[2][0]=="X")):
            print("HAS PERDIDO")
            return True

    elif sign=="O":
        if ((tablero[0][0]=="O" and tablero[0][1]=="O" and tablero[0][2]=="O") or 
            (tablero[1][0]=="O" and tablero[1][1]=="O" and tablero[1][2]=="O") or 
            (tablero[2][0]=="O" and tablero[2][1]=="O" and tablero[2][2]=="O") or 
            (tablero[0][0]=="O" and tablero[1][0]=="O" and tablero[2][0]=="O") or 
            (tablero[0][1]=="O" and tablero[1][1]=="O" and tablero[2][1]=="O") or 
            (tablero[0][2]=="O" and tablero[1][2]=="O" and tablero[2][2]=="O") or 
            (tablero[0][0]=="O" and tablero[1][1]=="O" and tablero[2][2]=="O") or 
            (tablero[0][2]=="O" and tablero[1][1]=="O" and tablero[2][0]=="O")):
            print("HAS GANADO")
            return True
    else:
        return False





def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    tablero=board
    casillalibre=MakeListOfFreeFields(tablero)
    tableroApoyo=[]
    for i,j in casillalibre:
        tableroApoyo.append(tablero[i][j])

    num=random.choice(tableroApoyo)

    if num==1:
        tablero[0][0]="X"
    elif num==2:
        tablero[0][1]="X"
    elif num==3:
        tablero[0][2]="X"
    elif num==4:
        tablero[1][0]="X"
    elif num==6:
        tablero[1][2]="X"
    elif num==7:
        tablero[2][0]="X"
    elif num==8:
        tablero[2][1]="X"
    elif num==9:
        tablero[2][2]="X"
    return tablero






tablero=[1,2,3],[4,"X",6],[7,8,9]
conta=0
a=False
DisplayBoard(tablero)
while a!=True:
    tablero=EnterMove(tablero)
    DisplayBoard(tablero)
    a=VictoryFor(tablero,"O")
    if a==True:
        break
    tablero=DrawMove(tablero)
    DisplayBoard(tablero)
    a=VictoryFor(tablero,"X")
    if a==True:
        break
    conta+=2
    if conta==8:
        a=True
        print("EMPATE")



