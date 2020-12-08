# Ordenamiento de burbuja
# El ordenamiendo de burbuja es un algoritmo que recorre
# rapidamente una lista que necesita ordenarse.
# Compara elementos adyacentes y los intercambia si estan
# en el orden incorrecto.
# Este procedimiento se repite hasta que no se requieren
# mas intercambios, lo que indica que la lista se encuentra
# ordenada.

import random

def ordenamiendo_de_burbuja (lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1): # 0(n) * 0(n) = 0(n**2)
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista?'))

    lista = ([random.randint(0, 100) for i in range (tamano_lista)])
    print(lista)

    lista_ordenada = ordenamiendo_de_burbuja(lista)
    print(lista_ordenada)

