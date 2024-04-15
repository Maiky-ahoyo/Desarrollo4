'''
Lógica del programa del gato
'''
import random
import board
import os
from colorama import Cursor

tablero = [x for x in range(0,9)] 
tab_dict= {x:str(x) for x in tablero}
lista_combinaciones = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
jugadores = {'Jugador/a X' : '','Jugador/a O' : ''}

def ia(board:dict):
    ocuppied = True
    while ocuppied == True:
        r = random.choice(list(board.keys()))
        if board[r] == str(r): # Si está libre
            board[r] = "O"
            ocuppied = False 

def check_winner(tab,lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
            return True
    return False

def solo_game(tab:dict):
    diccionario = {'ganador':''}
    turnos = 0
    while turnos < 9:
        os.system("cls")
        board.display_tablero(tab)
        correcto = board.juega_usuario_X(tab)
        if correcto:
            turnos +=1
            gana = check_winner(tab,lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = jugadores['Jugador/a X']
                break
            if not turnos == 9:
                ia(tab)
                gana = check_winner(tab,lista_combinaciones)
                if gana == True:
                    diccionario['ganador'] = jugadores['Jugador/a O']
                    break
                turnos += 1
            else:
                gana = check_winner(tab,lista_combinaciones)
                break    
    board.display_tablero(tab)
    return diccionario

def multiplayer_game(tab:dict):
    diccionario = {'ganador':''}
    turnos = 0
    while turnos < 9:
        os.system("cls")
        board.display_tablero(tab)
        correcto = board.juega_usuario_X(tab)
        if correcto:
            turnos +=1
            gana = check_winner(tab,lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = jugadores['Jugador/a X']
                break
            if not turnos == 9:
                os.system("cls")
                board.display_tablero(tab)
                correcto = board.juega_usuario_O(tab)
                if correcto:
                    turnos +=1
                    gana = check_winner(tab,lista_combinaciones)
                    if gana == True:
                        diccionario['ganador'] = jugadores['Jugador/a O']
                        break
            else:
                gana = check_winner(tab,lista_combinaciones)
                break    
    board.display_tablero(tab)
    return diccionario

def jugar_otra_vez():
    continuar = True
    otra_vez = input(Cursor.POS(2,16) + "¿Quieres jugar otra vez? (s/n): ")  
    otra_vez = otra_vez.upper()
    if (otra_vez != 'S'):
        continuar = False
        print(Cursor.POS(2,18) + "¡Gracias por jugar!")
    return continuar    

def display_score(s:dict, d:dict):
    if d['ganador'] != '':
        print(Cursor.POS(2,14) + f"Ganó: {d['ganador']}")
        s[d['ganador']] += 1
    else:
        print(Cursor.POS(2,14) + "¡Empate!")
        s['Empate'] += 1
    print(Cursor.POS(2,15) + "Marcador: " + str(s))    

def game_cycle():
    os.system("cls")
    print("1. Jugar contra la máquina")
    print("2. Jugar contra otra persona")
    print("3. Salir")
    opcion = input("Escoja una opción: ")
    if opcion == "1":
        jugadores['Jugador/a X'] = input("Nombre del jugador X: ")
        jugadores['Jugador/a O'] = "IA"
        score = {jugadores['Jugador/a X'] :0,jugadores['Jugador/a O'] :0,'Empate':0}
        continuar = True
        while continuar:
            tab_dict = {x:str(x) for x in tablero}
            d = solo_game(tab_dict)
            display_score(score,d)
            continuar = jugar_otra_vez()
    elif opcion == "2":
        jugadores['Jugador/a X'] = input("Nombre del jugador X: ")
        jugadores['Jugador/a O'] = input("Nombre del jugador O: ")
        score = {jugadores['Jugador/a X'] :0,jugadores['Jugador/a O'] :0,'Empate':0}
        continuar = True
        while continuar:
            tab_dict = {x:str(x) for x in tablero}
            d = multiplayer_game(tab_dict)
            display_score(score,d)
            continuar = jugar_otra_vez()
    elif opcion == "3":
        print("¡Gracias por jugar!")
    else:
        print("Opción inválida")
        game_cycle()        