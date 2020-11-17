# desafio.py
import random


def run():
    contador=0
    nombre=input('Ingresa tu nombre: ')
    numero_aleatorio=random.randint(1,100)
    numero_elegido=int(input('Elige un numero de 1 a 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido<numero_aleatorio:
            print('Busca un numero mas grande')
            contador = contador+1
        else:
            print('Busca un numero mas pequeño')
            contador = contador+1
        numero_elegido=int(input('Elige otro numero: '))
    print(nombre+' ¡Ganaste con '+ str(contador) +' intentos!')
    

if __name__ == "__main__":
    run()    