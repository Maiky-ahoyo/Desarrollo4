'''
20/02/2024
Arroyo Lopez Miguel Angel
222214253
'''

class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
    
    def __str__(self):
        return f'{self.titulo} - {self.catalogos}'
    
    if __name__ == '__main__':
        pass