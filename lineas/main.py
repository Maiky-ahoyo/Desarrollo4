from linea import linea
import matplotlib.pyplot as plt

if __name__ == "__main__":
    X = [x for x in range(10)]
    m = 2
    b = 3
    Y = linea.calcula_y(X, m, b)
    plt.plot(X,Y)
    XX = [x for x in range(100)]
    YY = linea.calcula_y(XX, m, b)
    plt.plot(XX,YY)
    plt.show()