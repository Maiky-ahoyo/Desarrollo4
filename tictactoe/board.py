from colorama import Cursor, Fore, Back, Style
tablero = [x for x in range(0,9)] #0,1,2,3...8
tab_dict= {x:str(x) for x in tablero}

def display_tablero(tablero:dict):
    reset = Style.RESET_ALL
    bg = Back.BLACK
    blue = Fore.BLUE
    board_color = Fore.MAGENTA
    x_color = Fore.YELLOW
    o_color = Fore.GREEN
    X = x_color + "X"
    O = o_color + "O"
    BD = board_color + "-------------"
    BS = board_color + "|"
    d = {}
    for k,v in tablero.items():
        if v == "X":
            d[k] =" " + X + " " + BS
        elif v == "O":
            d[k] =" " + O + " " + BS
        else:
            d[k] = blue + " " + str(k) + " " + BS
    print(Cursor.POS(10,2)+f"{bg}{BD}{reset}")
    print(Cursor.POS(10,3)+f"{bg}{BS}{d[0]}{d[1]}{d[2]}{reset}")
    print(Cursor.POS(10,4)+f"{bg}{BD}{reset}")
    print(Cursor.POS(10,5)+f"{bg}{BS}{d[3]}{d[4]}{d[5]}{reset}")
    print(Cursor.POS(10,6)+f"{bg}{BD}{reset}")
    print(Cursor.POS(10,7)+f"{bg}{BS}{d[6]}{d[7]}{d[8]}{reset}")
    print(Cursor.POS(10,8)+f"{bg}{BD}{reset}")
    print(Style.RESET_ALL)

def juega_usuario_X(tab):
    turno_correcto = False
    usuario = input(Cursor.POS(2,12) + "Escoja celda: ")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="X"
            turno_correcto = True
        else:
            print(Cursor.POS(2,13) + f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto   

def juega_usuario_O(tab):
    turno_correcto = False
    usuario = input("Escoja una celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="O"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto