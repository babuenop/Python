import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros=[]
    
    for _ in range(numero_de_tiros):
        numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0,00]
        tiro = random.choice(numbers)
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros
    

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    tiros_1 = 0
    for tiro in tiros: 
        if 1 in tiro:
            tiros_1 +=1
    probabilidad_tiros_1 = tiros_1/numero_de_intentos
    print(f'La probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros es = {probabilidad_tiros_1}')

    tiros_2 = 0
    for tiro in tiros: 
        if 2 in tiro:
            tiros_2 +=1
    probabilidad_tiros_1 = tiros_2/numero_de_intentos
    print(f'La probabilidad de obtener por lo menos un 2 en {numero_de_tiros} tiros es = {probabilidad_tiros_1}')

    tiros_3 = 0
    for tiro in tiros: 
        if 3 in tiro:
            tiros_3 +=1
    probabilidad_tiros_1 = tiros_3/numero_de_intentos
    print(f'La probabilidad de obtener por lo menos un 3 en {numero_de_tiros} tiros es = {probabilidad_tiros_1}')



if __name__ == "__main__":
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantos intentos quieres realizar: '))

    main(numero_de_tiros, numero_de_intentos)
   
