# Abstraccion
# No necesitamos entender como funciona algo internamente como 
# funciona. 
# Ejemplo: No necesitamos saber como funciona electronicamente 
# una calculadora, necesitamos saber como lo podemos utilizar. 
#
# Una de las habilidades mas importantes es la abtraccion para 
# saber como estan desarrolladas ciertas funciones de otros 
# usuarios 

# Descomposicion
# Permite dividir el codigo en componentes que colaboran con un
# fin en comun. 
# Se puede pensar como miniprogramas dentro de un programa mayor.

# Como definir una funcion 

# def <nombre>(<parametros>)
#    <cuerpo>
#    return <expresion>

def aproximaxion():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01 
    paso = epsilon**2
    respuesta = 0.0 

    while abs (respuesta**2 - objetivo) >=epsilon and respuesta <=objetivo:
        respuesta += paso 

    if abs(respuesta**2-objetivo)>=epsilon: 
        print (f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print (f'la raiz cuadrada de {objetivo} es {respuesta}')
    return

def busqueda_binaria():
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.01 
    bajo = 0.0 
    alto = max(1.0 , objetivo)
    respuesta = (alto+bajo) / 2

    while abs(respuesta**2-objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de objetivo es {objetivo} es {respuesta}')


def enumeracion():
    objetivo = int(input('Éscoge un numero entero: '))
    respuesta = 0 

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else: 
        print(f'{objetivo} no tiene raiz cuadrada exacta')

def menu():
    print(f"Seleccione un metodo para realizar el calculo \n (1) Enumeracion \n (2) Busqueda Binaria \n (3) Aproximación.")

    opcion = int(input("Elige una opcion: "))
        
    if opcion==1:
        enumeracion()
    if opcion==2:
        busqueda_binaria()
    if opcion==3:
        aproximaxion()
    else:
        print("Elija una opcion entre 1, 2, o 3")    

if __name__ == '__main__':
    menu()
    




















