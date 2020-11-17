# Estructuras de datos
Las estructuras de datos son una forma eficiente de almacenar y organizar la información de nuestro programa. Existen diferentes estructuras que vamos a estudiar durante el curso, es muy importante trabajar con una buena estructura que nos ayude a resolver nuestros problemas de la mejor manera posible.

Podemos clasificar las estructuras en dos grandes grupos:

## Lineales: 
La información se guarda de forma secuencial y podemos personalizar el orden en que se guardan. Por ejemplo, de acuerdo a las fecha, relevancia de la información, entre otras.

## No lineales: (Arboles y grafos)
No toda la información está al mismo nivel o almacenada con un orden especifico. Por ejemplo, en la estructura de árbol tenemos un tronco principal con diferentes ramificaciones que surgen a partir de este o, también, la estructura de grafos donde tenemos puntos de información dispersos pero interconectados entre sí.

# Que es un Algoritmo 
* Una serie de instrucciones o reglas establecidas que, por medio de una sucesión de pasos, permiten arribar a un resultado o solución.
* En programación, un algoritmo establece, de manera genérica e informal, la secuencia de pasos o acciones que resuelve un determinado problema y, para representarlo, se utiliza, fundamentalmente, dos tipos de notación: pseudocódigo y diagramas de flujo.
  
## Metodologia para la contruccion de un algoritmo
Los pasos recomendados para desarrollar un algoritmo son los siguientes:

* Definición del problema
* Análisis del problema
* Diseño del algoritmo
* Verificación o pruebas

Para la definición del problema debemos obtener los siguientes elementos:

* **Entradas:** ¿Qué se necesita para realizar los pasos?
* **Salidas:** ¿Qué se obtiene al final del algoritmo?
* **Tipos de datos involucrados:** Textos, números, listas, etc.

## User defined data types
Los User Defined DataTypes son tipos de datos creados por los desarrolladores de software para realizar múltiples acciones.

Estos datos pueden estar compuestos por otro tipo de datos previamente definidos pero, por defecto, no son parte del sistema. Además, dependiendo del lenguaje de programación que manejes, deberás tener claro (o no) el consumo de memoria.

Por ejemplo, las aplicación de cobranzas necesitan un tipo de dato personalizado para las personas con deudas.

**Tipo de dat abstracto**
Repesenta un set particular de comportamientos. 
    * Podemos definir con precision lo que hara un ADT
      * Un Stack es una lista que implementa una politica "LIFO" en elementos agregados o eliminados"
    * Una estructura de datos es mas correcta. Tipicamente es una tecnica o estrategia para implementar un ADT. 
      * Por ejemplo podemos utilizar una Linked List o en un Array(estructura de datos) para implementar un Stack(ADT)
    * Algunos de los ADT mas comunes que debes conocer como programador preparado son: 
      * Stack(pila), Queue(cola), PriorityQueue(Cola de prioridades), Diccionarios, Trees(arboles), Graphs(grafos).
    * Algunas de las estructuras de datos usadas para implementar esos ADTs son:
      * Array, linked list, hash tables.
      * Trees

**List ADT**
Una lista es un tipo de datos abstracto utilizado para representar un número contable de valores ordenados. El mismo valor puede existir más de una vez, esta es la implementación computacional del concepto matemático de secuencia finita, la lista.

A continuación te comparto las operaciones disponibles en este ADT:

get() – Retorna un elemento de la lista en cualquier posición especificada.
insert() – Inserta un elemento en cualquier posición de la lista.
remove() – Remueve la primera aparición de cualquier elemento en una lista no-vacía.
removeAt() – Remueve el elemento que se encuentre en la posición especificada en una lista que no esté vacía.
replace() – Reemplaza un elemento en cualquier posición por otro elemento.
size() – Retorna el número de elementos contenidos en la lista.
isEmpty() – Retorna true si la lista está vacía, si no, regresa false.
isFull() – Retorna true si la lista está llena, si no, regresa false.

**Stack ADT**
Un Stack es un tipo de datos abstracto que sirve como una colección de elementos con dos operaciones principales:
Push: agrega un elemento a la colección
Pop remueve el elemento que se añadió más recientemente y que no ha sido removido, el orden en el que esto funciona como hemos visto en clases sigue la lógica LIFO (last in, first out) que en español sería “último o más reciente en entrar, primero en salir”

A continuación te comparto las operaciones disponibles en este ADT:

push() – Inserta un elemento en un extremo de la pila denominado “cima”.
pop() – Remueve y retorna el elemento en la cima de la pila, si el stack no está vació.
peek() – Retorna el elemento en la cima del stack sin removerlo, si el stack no está vacío.
size() – Retorna el número de elementos en el stack.
isEmpty() – Retorna true si el stack está vacío, si no, retorna false.
isFull() – Retorna true si la lista está llena, si no, regresa false.

**Queue ADT**
Una cola es un ADT que sirve para almacenar datos en el orden en el que los datos van llegando, sigue una lógica del tipo FIFO o “primero en llegar, primero en salir” como es en la mayoría de supermercados.

A continuación te comparto las operaciones disponibles en este ADT:

enqueue() – Inserta un nuevo elemento al final de la cola.
dequeue() – Remueve y retorna el primer elemento de la cola si la cola no está vacía.
peek() – Retorna el primer elemento de la cola sin removerlo.
size() – Retorna el número de elementos almacenados en la cola.
isEmpty() – Retorna true si la cola está vacía, si no, retorna false.
isFull() – Retorna true si la cola está vacía, si no, retorna false.

## TRABAJAREMOS CON QUEUE:
### PASOS:

Crear un pointer para saber que hay en el front y rear
Colocar estos valores en -1 al inicializar
Incrementar en 1 el valor de rear cuando agreguemos algún elemento
Retornar el valor de front al quitar algún elemento, y incrementar en 1 el valor de front al usar dequeue
Ante de agregar algún elemento revisar si hay espacio (ISEMPTY()) importante, ya que si no revisamos se puede estar perdiendo información importante.
Antes de remover algún elemento revisamos que existan elementos (ISEMPTY()) se debe revisar, ya que al no haber elementos nos dirá que removió algún elemento cuando realmente no ha hecho nada
Asegurarnos de que al remover todos los elementos resetear nuestro front y rear a -1. Importantísimo, ya que si no reseteamos cuando retomemos algún valor nos puede dar 5, el cual no existe, ya que tenemos solo 5 posiciones iniciando en cero (0,1,2,3,4).
Este queue lo vamos a realizar con un Array, ya que sabemos el numero de elementos que se van a guardar en el Array.
Lo mejor es inicializar en -1, ya que siempre en programación se utiliza la posición 0 (cero).
