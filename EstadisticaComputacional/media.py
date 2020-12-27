import random
import math

# La media es el promedio de valores, es una medida de la tendencia central. 

def media(X):
    return sum(X) / len(X)

if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    
    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
