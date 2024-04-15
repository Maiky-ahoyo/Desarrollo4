from jugador import Jugador
from tablero import Tablero

class Juego:
    def __init__(self, tablero:Tablero,
                 jugador_a:Jugador,
                 jugador_b:Jugador) -> None:
        self.tablero = tablero
        self.jugador_a = jugador_a
        self.jugador_b = jugador_b
        self.turnos = 0

    def jugar(self, moviendo:Jugador, esperando:Jugador):
        ganador = False
        mov = False
        while mov == False:
            print(f"Turno de {moviendo.nombre}")
            mov = self.tablero.juega_usuario(moviendo)
        self.tablero.display()
        if (self.tablero.revisa_linea_ganadora()):
            moviendo.juegos["ganados"] += 1
            esperando.juegos["perdidos"] += 1
            ganador = True
            print(f"Ganó {moviendo.nombre}")
            
        self.turnos += 1    
        return ganador

    def inicia_juego(self):
        self.tablero.reset_tablero()
        mov = False
        while self.turnos < 9:
            self.tablero.display()
            g = self.jugar(moviendo = self.jugador_a, esperando = self.jugador_b)
            if (g != True):
                g = self.jugar(moviendo = self.jugador_b, esperando = self.jugador_a)
                if (g == True):
                    self.turnos = 9
            else:         
                self.turnos = 9

if __name__ == "__main__":
    lista = ["X","O"]
    a = Jugador("Bob","X",lista)
    b = Jugador("Patrick","O",lista)
    tab = Tablero()
    juego = Juego(tab,a,b)
    juego.inicia_juego()