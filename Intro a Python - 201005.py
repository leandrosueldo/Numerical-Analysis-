'''
Nuestro primer comando
'''
"hola mundo"
print("Hola mundo")
hola mundo
#%%
'''Estructuras de datos'''
#Python tiene varias estructuras de datos, que se pueden clasificar a grandes rasgos en tres categorias.

  ## Estructuras atomicas
     ## Representan un único elemento, por ejemplo:
        ## Int representa enteros
        ## String representa caracteres
        ## Float representa números reales (con decimales)
        ## Bool (booleano) representa un valor lógico (True, False)

 ##  Estructuras nativas
    ## Representan a un conjunto de elementos y además no tienen ninguna dependencia externa por fuera de python 
       ## list (Listas) representan un conjunto ordenado y mutable de elementos
       ## tuple (tuplas) representan un conjunto ordenado *no* mutable de elementos
       ## dict (Diccionarios) representan un mapeo entre un conjunto keys con otro conjunto values 
 
 ##  Estructuras que vienen definidas externamente
     ## Representan un conjunto de elementos y dependen de la inicialización de un paquete externo al paquete core de python, por ejemplo:
      ## numpy.array representa arreglos de filas y columnas (e.g. matrices)
      ## torch.Tensor representa arreglos de filas y columnas + un booleano que chequea una condicion (req_grad)
      ## pandas.DataFrame representa una tabla, i.e. un dataframe similar al nativo del lenguaje R

#%%
'''Empezamos con las estructuras atomicas'''
#Se puede conocer el tipo de estructura de un objeto con la funcion type()

type(5)

5+3
type(5+3)

def f(a,b):#a y b son variables locales
    return a+b
f(5,3)

a =10 #estos a y b son variables globales
b = 3
a+b

f(a,b)


#El tipo de un objeto no se define, sino que esta inferido, esto se conoce como duck-typing
# a diferencia x ej de VBA dnd hay que declarar las variables: Dim i as integer

type (5.)

type(3 + 3.5)

X = 3 ; Y = 3 ; Z = X + Y; Z

X = "3" ; Y = "3" ; Z = X + Y; Z

X = "3" ; Y = 3 ; Z= X + Y; Z


'''Strings'''
# Es una secuencia de caracteres
# Para diferenciar entre codigo y texto (conjunto de strings) se debe delimitar 
# el texto con dos conjuntos de doble comillas "Texto" 
# También se pueden usar comillas simples 'Texto'
# Si se tienen varias líneas de textos se usan seis doble comillas """ Texto """


type ("texto")

type ('texto')

"""
Esto es 
una oracion 
que insume 
más de una línea
"""

print("""
Esto es 
una oracion 
que insume 
más de una línea
""")


type ("
texto
")
#aca arroja error porque lee por linea y esta incompleto


type("""
T
e
x
t
o
""")

# Los booleanos evaluan a un numero True = 1, False = 0

type(True)

type(true)

type(False) 

#los booleanos evaluan a enteros (int)
True + True

type(False + True)

'''
Operadores
'''
#Para operaciones: +, -, *, /, **, %, //
#Para comparacion: >, <, >=, <=, ==, !=
#Para lógica: and, or, not
#Para : =, +=, -=, */=, %=, **=
#Especiales: in, not in, is, not is

# Si quiero comparar dos valores uso el operador == que también devuelve un booleano

True == 1

True + True == 2

True + False == False + True

# operador asignacion
x = 5
x

# El operador == compara valores sin importar su tipo

5 == 5.

# El operador is compara si es el mismo objeto en memoria. Es mas restrictivo que ==

5 is 5.

# También se puede negar

not True


True is not False


# El operador ==, y el operador is pueden comparar cualquier cosa, no hace 
# falta que el argumento sea una estructura atomica

# Aca estamos comparando el resultado (output) de dos funciones

type(5) == type(3)

type(3)

type(3) is type("5")

type("5")

# También se puede setear el tipo de un objeto con algunas funciones en particular, int(), float(), str()

str(5)
int(5.5)

type(float(5))

float("5")

float("a")

# Todas las estructuras atomicas vienen definidas con algunas operaciones.

# El operador + opera como suma

5 + 3

# El operador + opera como concatenacion

"Ho" + "la"

"Ho" + 5

"Ho" + str(5)

5 + "la"

# El operador * opera como multiplicación

5*3.5

# El operador * opera como repetición

"Hola " * 5

# Tambien tenemos exponenciación

3**2

# División

5/2

# // division entera

5//2

# Resto entero de una division

5%2

# Existen más estructuras atomicas
#x ej los numeros complejos que son parte real y parte imaginaria
x = complex(1, 2)
x
y = complex(2, 1)
y
x * y

'''Estructuras nativas de Python '''
# Mas alla de las estructuras atomicas estan las estructuras nativas de python

'''Tuplas'''
# Se pueden definir pasandole a un nombre una sucesion de valores separados por comas 
# o una sucesion de elementos agrupados con ()
# no tiene restriccion de tipo de datos

# Es una estructura de datos inmutable, es decir, no pueden ser editadas

tupla1 = (5,3,4,2) #tupla1 es el nombre de esta tupla de 4 elementos

type(tupla1)
tupla1
# Se puede llamar a un elemento en particular de la tupla a partír de un indice númerico y corchetes, []
# Este tipo de indexación se llama slicing
# En python la indexación siempre empieza en el cero

# el "[0]" es un indice. Python empieza en 0
(5,3,4,2)[0]
tupla1[2]

tupla1[-2]
tupla1[2]
tupla1[-5]

# Si quiero varios elementos consecutivos puedo pasar dos números mediados por el operador :
# Primeros dos elementos
tupla1[-1:]

#ultimos 2
tupla1[-2:]

#primeros 2
tupla1[:-2]

# primeros 4 elementos (en este caso es igual a todos los elementos)
tupla1[:3]
tupla1[0:4]#->[0;1) intervalo abierto

len(tupla1)

tupla1[0:4] == tupla1

# Del segundo al último

tupla1[1:]

tupla1[3]


# Los strings también aceptan este tipo de indexación (slice)

a = "Esto es un string"

a[3]
a[-6:]
a[4:10]


palabra = ("palabra1", "palabra2")
palabra[0] #me traigo primer elemento
palabra[0][4] # indexacion multiple

#podria hacer tupla de tuplas
palabras=(("palabra1", "palabra2"),5)
palabras[0][0][2:]
palabras[1]#no puedo seguir indexando

# es inmutable, no puedo borrar
del palabra[1]

# es inmutable, no puedo agregar nuevos elementos
palabra.append("hola")

#OJO: si puedo sobreescribir el nombre de la variable, pero eso no significa
# que este mutando lo original
palabra = ("palabra8", "palabra9")
palabra

# La función len() cuenta los elementos de una estructura de datos iterable 
# (que admite este tipo de indexación)
len(a)

len(palabra)

len(palabras)

len(tupla1)


# Podemos llenar una tupla con objetos heterogeneos (de distinto tipo)

mitupla = ( 3, "hola", complex(3,2) )

mitupla

# Podemos asignar varias variables (nombres) a cada elemento de la tupla

primer_elemento, segundo_elemento, tercer_elemento = mitupla

primer_elemento

#es equivalente a decir:
primer_elemento = mitupla[0]
segundo_elemento = mitupla[1]
tercer_elemento = mitupla[2]

mitupla

primer_elemento

# el operador "del" nos permite borrar de memoria un objeto

del primer_elemento #borra la variable, no el objeto
del mitupla

mitupla

primer_elemento

segundo_elemento

tercer_elemento

# Los elementos que constituyen una tupla no tienen por que ser elementos atomicos.
mitupla[1][3]

tupla2 = ((3,2,5),(1,25))

tupla2[1][-1]

len(tupla2[1])

type(tupla2[1])

# Como el primer elemento de esta tupla también es una tupla admite indexación múltiple
tupla2[0][0]

# Otra caracteristica importante de las tuplas es que una vez que estan creadas son inmutables, 
# no se pueden redefinir sus elementos
tupla2
tupla2 [1] = 5

tupla2
x=[1,25]
x
# Que pasa aca? Tengo una tupla compuesta por una tupla y una lista
tupla3 = ((3,2,5),[1,25])
type(tupla3)
type(tupla3[1])

tupla3 [1][0]= 3

# recordar que tupla3 = ((3,2,5),[1,25])
tupla3

type(tupla3[1])

tuple(tupla3[1])

tupla3


'''Listas'''
# La segunda estructura de datos nativa de python son las listas. 
# Son ordenadas como las tuplas, y admiten el mismo tipo de indexación pero son mutables


numeros = [5,3,3,4]

type(numeros)

len (numeros)

a,b,c,d = numeros

a

# Las listas vienen equipadas con un conjunto de funciones que le son especificas, se llaman 
# de una forma particular y tienen un nombre aparte, son los métodos

# Un ejemplo de método es el .append() que le agrega a una lista un valor o conjunto de valores al final
numeros.append("Esto va al final")

numeros

# Nota: importa el orden en que se llevan a cabo las líneas en el interpretador
lista=numeros
lista

a = len(lista)
b = len(lista)
lista.append(9)
a == b

a == len(lista)

len(lista)

a = len(lista)
lista.append(9)
b = len(lista)
a == b


# slicing en listas 
lista_larga = [4,5,6,7,2,3,4,8,3,6,2]
lista_larga[-0] 
lista_larga[-2:]
lista_larga[-4:-1]


# Otra cosa a tener en cuenta es la posibilidad de pisar el nombre de una variable 
# tanto en listas como en tuplas, xq el nombre se puede pisar

tupla = (2,3)
tupla = ["otra", "cosa"]

# No siempre el método append funciona como esperamos

pares = [2,4,6]

maspares = [8,10]

pares.append(maspares)

pares

pares[3][0]#si quiero acceder al 8 por ej

pares = [2,4,6]

maspares = [8,10]

pares + maspares

# Para esto hay otro metodo .extend()
pares = [2,4,6]

maspares = [8,10]

pares.extend(maspares)

pares


# Hay varios métodos de listas adicionales
pares.remove(10)
pares

#elimino utilizando indexación
del pares[1:3]
pares

pares = [2, 4, 6, 8, 10]

pares [0] = 30
pares [1] = 36
pares

pares.sort()
pares

pares.sort(reverse=True)
pares

#otros comandos
pares = [2, 4, 6, 8, 10, 10]
pares.insert(3,0) #agrego el elemento 0 en la 3era posicion
pares
pares.count(5) # cuenta la cant de veces que aparece un elemento
pares.index(0) # devuelve la posición del valor indicado
pares.reverse() #invierte el orden de aparición, no es un ordenamiento
pares
pares.clear() #borra todo el contenido
pares

pares = [2, 4, 6, 8, 10, 10]
del pares
pares

#Puedes convertir listas a tuplas y viceversa. Ejemplo:
a = [1, 2, 3]
type(a)
a = tuple(a)
type(a)

a=(1, 2, 3)
type(a)
a = list(a)
type(a)


'''Condicionales'''
# Condicionales, if

# Algunos de los operadores  admisibles son:
 # < "Menor a"
 # <= "Menor o igual a"
 # > "Mayor a"
 # >=  "Mayor o igual a"
 # ==  "igual a"
 # !=  "Distinto a"
 # is  "es el mismo objeto que"
 # is not "no es el mismo objeto que"

'''Las condiciones son la base de la programación en cualquier lenguaje. Estas 
quieren decir que si se cumple determinada condición pasa algo. Y en el caso 
de que no se cumpla, ocurre otra cosa.'''
# Se usa la indentación (sangría) para saber cuando empieza y cuando termina el 
# bloque de codigo cuya ejecución es condicional.

a = 34
b = 20

if b>a:
    print('b es mayor que a')

if b>a:
    print('b es mayor que a')
else:
    print('b no es mayor que a')   

if b>a:
    print('b es mayor que a')
elif a==b:
    print('a es igual a b')
else:
    print('a es mayor que b')  


x = 5
if x>5:
    x = x + 3
    #x += 3
elif x<5:
    x = x - 2
else:
    x +=1  
x

x = 8
if x: #aca no le estoy poniendo ninguna condicion, solo que x exista
    x +=3
x


x = 4
if x>5:
    y = 3
    z = 4
    x = y+z
print(x)


# Esto hace que anidar bloques condicionales (lo cuál es muy común) sea muy legible en python 

# si x es un entero entre 5 y 10, sumarle 6
x = 7
if type(x) == type(2):
    if x > 5:
        if x < 10:
            x = x + 6
x

if type(x) == type(2):
    if 5 < x <10 :
        x += 6
x

# si x es un entero mayor a 5, sumarle 3, si el número resultante es menor a 10, sumarle 4
x = 8
if type(x) == type(2):
    if x > 5:
        x += 3
        print(x)
        if x < 12:
            x += 4        
x

# si x es un número mayor a 5 printear x, caso contrario printear x+5
x = 1
if x > 5:
    print (x)
else:
    print (x+5)
    
# if x pregunta si x existe
if x:
    print(1)


#Statement Pass
# Si por algún motivo en cualquier estructura queremos identificar una situación
# en que no se desea hacer nada se utiliza pass

x=-20
# Valor absoluto de x
if x > 0:
    pass #si >0 no se hace nada
else:
    x *= -1 #si <0 cambio de signo. Es lo mismo que poner x=x*-1
x   


'''Range'''
range(5)
range (50)

for x in range(50):
    print(x)

#iteracion por valores
lista
for x in range(len(lista)):
    print(x)
    
#iteracion por indices
lista
for x in range(len(lista)):
    print(lista[x])
    
#bucles multiples
for i in range(2):
    print(i)
    for j in range(2):
        print(j*2)
        for k in range(2):
            print(k*3)

'''Estructuras de control'''
'''Iteracion definida, for'''
# La sintaxis es 
# for __ in iterable:
   ##  Bloque de instrucciones
   ## El fín del for esta inferido por la identación.
# En general si hay un bloque de código con sangría, esto significa que 
# este bloque depende de la instrucción inmediatamente arriba

# La funcion print() imprime un valor

lista = [3,5,6,2,2]

valor_que_quiero_calcular = 0

for iterador in range(len(lista)):
    valor_que_quiero_calcular += iterador *2
valor_que_quiero_calcular

valor_que_quiero_calcular = 0

for i in lista:
    valor_que_quiero_calcular += i *2
valor_que_quiero_calcular

range(len(lista))

# En este esquema elem no significa nada, se puede reemplazar con cualquier cosa

lista = [3,5,6,2,2]

for _ in lista:
    print (_)


# Notese dos cosas importantes del ciclo for:
  # El for recorre el iterable y termina cuando no hay más elementos 
  # (en ningún momento le avisamos cuantas veces queremos que itere)
  # Se esta iterando por los valores de la lista, *no* por los *índices* de la lista

#1

lista = [3,5,6,2,2]
lista2 = [3,5,6,2,2]
for _ in lista:
    
    lista2.append(1)
    print (_)
lista2

lista2

#2

lista = [3,5,6,2,2]

for x in range(len(lista)):
    print (x)


'''Iteracion definida, while'''
# funciona con una condición y un iterador explicito

i = 0
while i <100:
    i += 1
    print(i)

i =1
while i >0:
    i = i + 1
i

# Si me olvido del iterador entro en un loop infinito

i = 0 

while i <100:
    print(3 + i)
    i = i+1


'''Funciones'''
# Más alla de las funciones construidas en python (print, range, len, etc) el usuario puede definir sus propias funciones
# Todas las funciones nativas estan aca https://docs.python.org/2/library/functions.html
# Toman argumentos genericos y hacen operaciones con ellos
# La sintaxis es similar a un bloque condicional
# La palabra clave return me dice que quiero que la función me devuelva


def funcion (arg1, arg2=1):
    if type(arg1) == type(2) or type(arg1) == type(2.):
        if type(arg2) == type (2) or type(arg2)==type(2.):
            return float(arg1) + float(arg2)
    else:
        print("error de tipo")


# Esta funcion toma dos argumentos, de los cuáles el segundo es opcional, 
# tomando el valor base de 3 si no se cambia.

# Cuando se llama a una funcion se pueden invocar los argumentos de manera posicional 
# (en el mismo orden que vienen definidos) o con los nombres de los argumentos

#arg1 = 2, arg2 = 3

funcion(2)

#Como el tipado es debil en python mi función puede tener un comportamiento no previsto
#arg1 = "2", arg2 = "3"

funcion("2", "3")


funcion(arg2 = 50, arg1 = 2)


# Podemos meter un condicional adentro de la definicion de la función 

def f(x):
    if x < 0:
        return "número negativo"
    return "número no-negativo"

f("3")


f(-1)

# Es una buena costumbre documentar funciones (especialmente si son largas) con un 
" string al inicio de la funcion

def Sumarsi(valor1, valor2, condicion):
    
    """Esta función suma dos valores si se cumple una condicion"""
    
    if condicion:
        valor1 + valor2

help(Sumarsi)

import numpy as np

help(np.mean)


# Python sabe que el string es la definición de la función, puedo pedir información 
# de la función con "?"

get_ipython().run_line_magic('pinfo', 'Sumarsi')

# ejemplo funcion mal indentada, no siempre la mala indentacion tira un error

def Suma_o_Resta(valor1, valor2, esSuma):
    
    resultado = 0
    
    if esSuma == True:
        resultado = valor1 + valor2
    elif esSuma == False:
        resultado = valor1 - valor2
    else:
        print("esSuma debe ser un booleano")
    return resultado

valor = Suma_o_Resta(3,4,None)
print(valor)

None is False

def f(lista, valor):

    for elem in range(len(lista)):

        lista[elem] = lista[elem] + valor
        
    return lista



a = f([1,2,3,7,8,9,7,6], 5)


print (a)


# Comprehensión de listas, permite crear listas con una regla rápidamente

[x ** 2 for x in range (9)]


def sumar_numero_a_lista(lista, valor):
    return [elem + valor for elem in lista]
print(sumar_numero_a_lista([3,3,3], 3))


# Recursividad, puedo llamar repetidamente a una función cambiando sus argumentos, 
# tener cuidado con esto

def llegarA0 (cantidad):
    if cantidad == 0 :
        return "llegue"
    else:
        return llegarA0(cantidad-1)

llegarA0(3.5)

