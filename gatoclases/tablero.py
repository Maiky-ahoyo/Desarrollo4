from colorama import Fore, Back, Style, Cursor
from jugador import Jugador

class Tablero:
    def __init__(self,color_fondo=Back.WHITE,color_rayas=Fore.LIGHTCYAN_EX,
                 color_numeros=Fore.BLUE,color_x=Fore.RED,color_o=Fore.GREEN) -> None:
        self.lista_numeros = [x for x in range(0,9)]
        self.dicc_posiciones={x:str(x) for x in self.lista_numeros}
        self.combos_ganadores= [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        self.color = {"rayas":color_rayas,
                      "fondo":color_fondo,
                      "numeros":color_numeros,
                      "X":color_x,
                      "O":color_o
        }
        
    def display(self):
        tablero = self.dicc_posiciones
        reset = Style.RESET_ALL
        bg = self.color["fondo"]   #Back.WHITE
        blue = self.color["numeros"] #Fore.BLUE
        board_color = self.color["rayas"] #Fore.LIGHTCYAN_EX
        x_color = self.color["X"] #Fore.RED
        o_color = self.color["O"] #Fore.GREEN
        X = x_color + "X"
        O = o_color + "O"
        BD = board_color + "-------"
        BS = board_color + "|"
        d = {}
        for k,v in tablero.items():
            if v == "X":
                d[k] = X + BS
            elif v == "O":
                d[k] = O + BS
            else:
                d[k] = blue + str(k) + BS
        print(Cursor.POS(10,5)+f"{bg}{BD}{reset}")
        print(Cursor.POS(10,6)+f"{bg}|{d[0]}{d[1]}{d[2]}{reset}")
        print(Cursor.POS(10,7)+f"{bg}{BD}{reset}")
        print(Cursor.POS(10,8)+f"{bg}|{d[3]}{d[4]}{d[5]}{reset}")
        print(Cursor.POS(10,9)+f"{bg}{BD}{reset}")
        print(Cursor.POS(10,10)+f"{bg}|{d[6]}{d[7]}{d[8]}{reset}")
        print(Cursor.POS(10,11)+f"{bg}{BD}{reset}")
        print(Style.RESET_ALL)
    
    def reset_tablero(self):
        self.dicc_posiciones={x:str(x) for x in self.lista_numeros}

    def revisa_linea_ganadora(self):
        tab = self.dicc_posiciones
        lista_lineas = self.combos_ganadores
        for cmb in lista_lineas:
            if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
                return True
            else:
                return False
    
    def juega_usuario(self, jugador:Jugador):
        tab = self.dicc_posiciones # Tablero
        turno_correcto = False
        usuario = input(Cursor.POS(10,11)+"Escoja celda:")
        usuario = int(usuario)
        if usuario in tab:
            if tab[usuario] == str(usuario):
                tab[usuario]= jugador.simbolo
                turno_correcto = True
            else:
                print(f"Posición {usuario} ocupada")
                print("Eliga otra opción")
        return turno_correcto   
    
if __name__ == "__main__":
    t = Tablero()
    t.dicc_posiciones[0] = "X"
    t.dicc_posiciones[4] = "X"
    t.dicc_posiciones[8] = "X"
    t.display()
    print(f"Gana:{t.revisa_linea_ganadora()}")
    t.reset_tablero()
    t.display()
    lista_simbolos = ["X","O"]
    A = Jugador("Spongebob","X",lista_simbolos)
    t.juega_usuario(A)
    t.display()