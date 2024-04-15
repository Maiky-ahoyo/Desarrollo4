import os
class Revista:
    def __init__(self,titulo:str,catalogo:str,sjr:str,
                 q:str,h_index:str,total_citas:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
        self.sjr = float(sjr)
        self.q = q
        self.h_index = int(h_index)
        self.total_citas = int(total_citas)

        def __str__(self):
                return f'{self.titulo}|{self.catalogos}|{self.sjr}|{self.q}|{self.h_index}|{self.total_citas}'

        if __name__ == "__main__":
                os.system('cls')       