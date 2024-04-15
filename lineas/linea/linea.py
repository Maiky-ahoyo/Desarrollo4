def linea(x, m, b):
    '''
    Funcion que calcula la pendiente de una receta
    '''
    resultado = (m*x) + b
    return resultado  

def calcula_y(X, m, b):
    '''
    Funcion que calcula la pendiente de una receta
    '''

    Y = [linea(x, m, b) for x in X]
    return Y

if __name__ == "__main__":
    X = [x for x in range(10)]
    m = 2
    b = 3
    Y = calcula_y(X, m, b)
    print(X,Y)