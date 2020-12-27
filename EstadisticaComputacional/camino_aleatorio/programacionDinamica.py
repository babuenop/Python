# Optimizacion de Fibonacci
# Existen la forma basica para ejecutar los numeros de fibonacci,
# sin embargo, es bastante ineficiente, veremos en este archivo
# la tecnica de Memoization.
import sys 
def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo)+fibonacci_dinamico(n-2)
        memo[n]=resultado
        print(memo)

        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n= int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
    

