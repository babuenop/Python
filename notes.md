
# Scope o Alcance
Tambien podemos enviar funciones como argumentos. 
Frames es como funcionan internamente los lenguajes de 
programacion 
En python leemos de arriba hacia abajo y  de izquierda a 
derecha. 

# Especificaciones del codigo.

Con """ Podemos crear multinineas en python
Para describir una funcion debemos especificar los parametros y
especificar el resultado de la funcion. 


## Recursividad 
 Es una tecnica que una funcion se llama a si misma. 
 Una recursion es una forma de iterar. 

 ### Algoritmica 
 Una forma de crear soluciones utilizando el principio se "divide y venceras"
 ### Programatica 
 Una tecnica programatica mediante la cual una funcion se llama a si misma.

 n! = n*(n-1)!
 
# Funciones como objetos
Una de las caracteristicas mas poderosas de Python es que todo es un objeto, incluyendo las funciones en Python son "ciudadanos de primera clase"

Esto, en sentido amplio, significa que en Python las funciones 
    a. Tienen un tipo
    b. Se pueden pasar como argumentos
    c. Se pueden utilizar en expresiones 
    d. Se pueden incluir en varias estructuras de datos 

# Tipos estructurados, mutabilidad y funciones de alto nivel 

## Tuplas 
Son secuencias inmutables de objetos 
    * A diferencia de las cadenas pueden contener cualquier tipo de objeto.
    * A diferencia de las cadenas pueden contener cualquier tipo de objeto. 
    * Puede utilizarse para devolver varios valores en una funcion. 

  Para definirn una tupla de un solo valor debemos agregar una coma despues del valor
    Ejemplo 
        my_tuple = (1,)

  Nosotros podemos desempaquetar una tupla. 
    Ejemplo
        x, y, z = my_other_tuple 

## Rangos 
    * Representas una secuencia de enteros. 
    * range(comienzo, fin, pasos)
    * Al igual que las cadenas y las tuplas, los rangos son inmutables. 
    * Muy eficientes en uso de memoria y normalmente utilizados en for loops
    * Los rangos nos generan rangos de enteros y podemos operar igualdad de objetos, identificando su ID.  

## Debugging
    * No te molestes con el debugger. Aprende a utilizar el print statement.
    * Estudia los datos disponibles. 
    * Utiliza los datos para crear hipotesis y experimentos. 
    * Ten mente abierta sie entendietas el programa, probablemente no habrian bugs. 
    * Lleva un registro de lo que has tratado prferentemente la forma de test. 
  
  ### Diseño de experimentos
    * Debuggear es un proceso de busqueda. Cada prueba debe acotar el espacio de busqueda.
    * Busqueda binaria con print statements. 
  
  ### Errores comunes
    * Encuentra los sospechosos comunes.
        * Nombre incorrectos
        * Errores de escritura
        * No se inicializaron variables. 
        * Se te ocurrio que una funcion soluciona todo y tienen efectos secundarios. 
        * Generaste un error tipico de script
    * Explicarle el problema a otra persona. De preferencia que no tenga contexto. 
    * Lleva un registro de lo que has tratado, preferentemente en la forma de test. 
    * Vete a dormir
  
## Manejo de excepciones 
  * Las excepciones son muy comunes en la programacion. No tienen nada de excepcional. 

  * Las excepciones de Python normalmente se relaciona con errores de semantica. 

  * Se pueden crear excepciones propias. 

  * Cuando una excepcion no se maneja, el programa termina en error.

### Como manejarlas
  * Las excepciones se manejan con keywords: try, except, finally. 
  * Se pueden utilizar tambien para ramificar programas. 
  * No debe manejarse de manera silencionas(por ejemplo, con rpint statements)
  * para aventar tu propia excepcion utiliza el keyword raise. 

**Excepciones comunes:**
*ImportError:* una importación falla;
*IndexError:* una lista se indexa con un número fuera de rango;
*NameError:* se usa una variable desconocida ;
*SyntaxError:* el código no se puede analizar correctamente
TypeError : se llama a una función en un valor de un tipo inapropiado;
*ValueError:* se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

```py
# Python

def busca_pais(paises, pais):
    """
    Países es un diccionario. País es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None
```

```js
// Javascript

/**
* Paises es un objeto. Pais es la llave.
* Codigo con el principio LBYL.
*/
function buscaPais(paises, pais) {
  if(!Object.keys(paises).includes(pais)) {
    return null;
  }

  return paises[pais];
}
```
## Afirmaciones 
 *  Programacion defensiva
 *  Pueden utilizarse para verificar que los tipos de una funcion sean correctos. 
 *  O en algunos casos sirve para debuggear

## Literales - los datos en si mismos
Ahora que tienes un poco de conocimiento acerca de algunas de las poderosas características que ofrece la función print(), es tiempo de aprender sobre cuestiones nuevas, y un nuevo término - el literal.

**Un literal se refiere a datos cuyos valores están determinados por el literal mismo.**

Debido a que es un concepto un poco difícil de entender, un buen ejemplo puede ser muy útil.

Observa los siguientes dígitos:

```123```

¿Puedes adivinar qué valor representa? claro que puedes - es ciento veintitrés.

Que tal este:

```c```

¿Representa algún valor? Tal vez. Puede ser el símbolo de la velocidad de la luz, por ejemplo. También puede representar la constante de integración. Incluso la longitud de una hipotenusa en el Teorema de Pitágoras. Existen muchas posibilidades.

No se puede elegir el valor correcto sin algo de conocimiento adicional.

Y esta es la pista: 123 es un literal, y c no lo es.

Se utilizan literales para **codificar datos y ponerlos dentro del código**. Ahora mostraremos algunas convenciones que se deben seguir al utilizar Python.

## Notacion Asintotica
Conforme el input se va al infinito.

Crecimiento asintotico
No importan variaciones pequeñas
El enfoque se centra en lo que pasa conforme al tamaño del problema se acerca al infinito

Mejor de los casos, promedio, peor de los casos.

Big O Notation.

Nada mas importa el termino de mayor tamaño

# Algoritmos de busqueda y ordenacion
## Busqueda lineal
Busca en todos los elementos de manera secuencial. ¿Cual es el peor caso?

## Busqueda Binaria
Divide y conquista
El problema se divide en 2 en cada iteracion
Cual es el peor caso?


