"""
INTRODUCCION A PYTHON - PARTE 2
FECHA: 11/11/2020
ORGANIZAN: CATEDRA DE ANALISIS NUMÉRICO Y CIMBAGE(IADCOM)
PROFESOR: MARTIN CONOCCHIARI
"""
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
'''Set'''
# Permite almacenar un conjunto heterogéneo de objetos, pero cada uno  debe ser 
# único.
# Es mutable y puede cambiar de tamaño libremente, pero los objetos almacenados 
# deben ser inmutables.

# Creando sets:
s0 = set()
s1=set([1,2,3])
s2={1,2,3}

#operaciones y metodos principales
s1, s2 = {1,2,3}, {2,5,6}

s1 & s2 # Intersección => {2}  
s1 | s2 # Unión => {1,2,3,5,6}
s1 - s2 # Diferencia => {1,3}
s1 > s2 # Chequea si incluye a s2 => False
1 in s1 # True
s1.add(4) # s1 => {1,2,3,4}
s1.remove(2)  # s1 => {1,3,4}
s1.pop() # Elimina y devuelve un elemento

#Ejemplo de utilización
secuencia = [3,8,4,3,2,5,2,5,6,3,7,8,9,2,2,2,1,5,6,7,8,3,8,5,9,0]
print('La secuencia anterior tiene ', len(secuencia), 'elementos')
print('Sien embargo, tiene ', len(set(secuencia)), 'elementos únicos')
#%%
'''Diccionarios'''

# Un diccionario es una colección desordenada, mutable e indexada. 
# Estan definidas igual que los sets, ya que tienen una clave unica entre {}
# Los diccionarios se escriben con llaves y tienen "keys" y "values"
thisdict =	{"marca": "Ford",  "modelo": "Mustang", "año": 1964}
print(thisdict)

#acceder a los valores del diccionario
x = thisdict["modelo"]
x = thisdict.get("modelo")
x
# cambiar alguno valor del diccionario
thisdict["año"] = 2018

#chequeo si alguna key existe
if "modelo" in thisdict:
  print("Si, 'modelo' es una de las llaves del diccionario thisdict") 

# Determino la cantidad de items (pares de key-value) que tiene el diccionario
print(len(thisdict)) 

#agrego un nuevo valor indicando key y value
thisdict["color"] = "azul"
print(thisdict)

# elimino elementos (hay varias maneras)
thisdict.pop("modelo")
print(thisdict) 

del thisdict["modelo"]
print(thisdict) 

del thisdict #si quiero eliminar el diccionario completo

# El metodo popitem() remueve el ultimo item insertado
thisdict.popitem()
print(thisdict) 

# El metodo clear vacia el diccionario
thisdict.clear()
print(thisdict) 

# copiar diccionarios
mydict = thisdict.copy() # no puedo usar mydict = thisdict
print(mydict)

# Diccionarios anidados
# Creo un diccionario que contiene 3 diccionarios
familia = {
  "hijo1" : {
    "nombre" : "A",
    "año" : 2004
  },
  "hijo2" : {
    "nombre" : "B",
    "año" : 2007
  },
  "hijo3" : {
    "nombre" : "C",
    "año" : 2011
  }
} 
print(familia)

# Creo tres diccionarios por separado y luego creo uno que contenga a los tres
hijo1 = {
  "nombre" : "A",
  "año" : 2004
}
hijo2 = {
  "nombre" : "B",
  "año" : 2007
}
hijo3 = {
  "nombre" : "C",
  "año" : 2011
}

familia2 = {
  "hijo1" : hijo1,
  "hijo2" : hijo2,
  "hijo3" : hijo3
}
print(familia2)

# Metodo dict para construir diccionarios
thisdict2 = dict(marca="Ford", modelo="Mustang", año=1964)
print(thisdict2)

'''
Method 	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

nombres = ['Martin','Jose','Juan']
apellidos = ['A','B','C']

info_alumnos = {'Nombre':nombres,'Apellido':apellidos}
edad = [20,25,30]
promedio = [8,9,7]
carrera = ['Adm','Cdor','Act']
info_alumnos['Edad'] = edad
info_alumnos['Promedio'] = promedio
info_alumnos['Carrera'] = carrera
info_alumnos

#%%
'''zip'''
#Para unir elemento por elemento dos secuencias en paralelo
zip([1,2,3], [4,5,6])	# (1,4),(2,5),(3,6)

Nombre = ['Martin','Jose','Juan']
DNI = [123,456,789]
list(zip(Nombre, DNI))
#%%
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

a = 34
b = 20
if b>a:
    print('b es mayor que a')
else:
    print('b no es mayor que a')   

a = 20
b = 20
if b>a:
    print('b es mayor que a')
elif a==b:
    print('a es igual a b')
else:
    print('a es mayor que b')  

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

#Puede existir el caso en que realizar un if compuesto sea poco práctico
Strike=60
Price=40

if Strike > Price:
    payoff = Strike - Price
else:
    payoff = 0

# Dichos casos pueden simplificarse
payoff = Strike - Price if Strike > Price else 0

#%%
'''Estructuras de control'''
'''Iteracion definida, for'''
# Se utiliza para iterar sobre una secuencia (lista, tupla, diccionario, string, etc.)
# La sintaxis es 
# for __ in iterable:
   ##  Bloque de instrucciones

frutas = ["manzana", "pera", "naranja"]
type(frutas)
for i in frutas:
    print(i)
   
cuenta = [1, 2, 3, 4, 5, 6]
for i in cuenta:
    if i<=4:
        print(i)

for i in 'hola':
    print(i)
    
#loop sobre un diccionario
#Print de todas las keys names del diccionario
for x in thisdict:
  print(x) 
#Print de todos los values del diccionario 
for x in thisdict:
  print(thisdict[x])   

for x in thisdict.values():
  print(x) 

# loop a traves de keys y values del diccionario, usando el metodo items()
for x, y in thisdict.items():
  print(x, y) 


'''Range y len'''
# La función range se utiliza para generar números de manera sucesiva. Se escribe 
# de la siguiente manera: range(comienzo, final [, pasos]) EL FINAL DEL RANGO ES ABIERTO
# comienzo: desde donde empieza la secuencia. Por defecto se inicia en 0
# final: hasta donde debe correr la secuencia
# pasos: este parámetro es opcional. Por defecto, es 1

range(5)
range (50)
len(cuenta)
n=len(range(50))
for x in range(n):
    print(x)

#calcula e imprime el valor y su potencia al cuadrado
for i in range(5, 8):
    print(i, i ** 2)

for num in range(5,26,5):
  print(num)

resultado = 0
n = 5
for i in range(1, n + 1):
    resultado += i   # resultado = resultado + i
print(resultado)
'''
#paso a paso de esta funcion
1er step: 0+1=1
2do step: 1+2=3
3er step: 3+3=6
4to step: 6+4=10
5to step: 10+5=15
'''
#iteracion por valores
lista = [3,5,6,2,2]

for x in lista:
    print(x)
    
for x in range(len(lista)):
    print(x)

range(len(lista))
    
#iteracion por indices
lista
for x in range(len(lista)):
    print(lista[x])
    
for x in range(6):
  print(x)
else:
  print("Finalmente terminó!") 

valor_que_quiero_calcular = 0
for iterador in range(len(lista)):
    valor_que_quiero_calcular += iterador *2
valor_que_quiero_calcular
'''
1er step: 0+0*2=0
2do step: 0+1*2=2
3er step: 2+2*2=6
4to step: 6+3*2=12
5to step: 12+4*2=20
'''

valor_que_quiero_calcular = 0
for i in lista:
    valor_que_quiero_calcular += i *2
valor_que_quiero_calcular
'''
1er step: 0+3*2=6
2do step: 6+5*2=16
3er step: 16+6*2=28
4to step: 28+2*2=32
5to step: 32+2*2=36
'''

Nombre = ['Martin', 'Lisandro']
DNI = [123456789, 987654321]
for i in zip(Nombre,DNI):
  print(f"La variable i es {i}. Donde '{i[0]}' es el Nombre y '{i[1]}' el DNI")
list(zip(Nombre,DNI))

#bucles multiples
for i in range(2):
    print(i)
    for j in range(2):
        print(j*2)
        for k in range(2):
            print(k*3)

'''Iteracion indefinida, while'''
# funciona con una condición y un iterador explicito
# No tiene una variable incremental por defecto

i = 0
while i <100:
    i += 1
    print(i)

#Ejemplo de loop infinito
i = 1
while i >0:
    i = i + 1
i

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i ya no es menor a 6")
  
'''Break y continue'''
# Para controlar manualmente cualquier loop existen los statements
# break: Detiene la ejecución del for/while y sale afuera del mismo
# continue: Detiene la ejecución de la iteración actual y sigue en la próxima

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#%%
'''Funciones'''
# Más alla de las funciones construidas en python (print, range, len, etc) el usuario puede definir sus propias funciones
# Todas las funciones nativas estan aca https://docs.python.org/3/library/functions.html
# Toman argumentos genericos y hacen operaciones con ellos
# La sintaxis es similar a un bloque condicional
# La palabra clave return me dice que quiero que la función me devuelva

#De forma de hacer que nuestro código sea de fácil comprensión, además de la utilización de
#comentarios (anteponiendo #), se suele documentar. Esta documentación se refleja en el help
# de nuestro IDE.  
# Es una buena costumbre documentar funciones (especialmente si son largas) con un 
""" string al inicio de la funcion"""

"""
Las funciones pueden admitir como input cualquier tipo de datos  siempre y cuando los 
statements que se encuentren dentro de la  función puedan ser ejecutados para dichos objetos.
El chequeo de esta condición se realiza durante la ejecución, no antes.
Esta ejecución condicional al tipo de datos de los inputs se denomina  polimorfismo.
"""

#defino la funcion
def mi_funcion():
  print("Hola")
#la llamo
mi_funcion()
# la llamo y el resultado lo puedo asignar a una variable
respuesta = mi_funcion()

def cuadrado(a):  
    """
    Calcula el cuadrado de un número  Parámetros:
        a : Número a elevar
    Uso:
        >>> cuadrado(2)
    """
    return a * a

help(cuadrado)

def promedio(a, b):
    """
    Calcula el promedio entre dos valores.
    Parametros:
        a : Numero
        b : Numero
    """
    return (a + b) / 2

def suma(a,b):
    """
    Calcula la suma entre dos valores.
    Parametros:
        a : Numero
        b : Numero
    """
    return a+b

# Podemos incluir un condicional adentro de la definicion de la función 
def f(x):
    if x < 0:
        return "número negativo"
    return "número no-negativo"

f(-1)
f("3")

def f(lista, valor):
    for elem in range(len(lista)):
        lista[elem] = lista[elem] + valor      
    return lista

lista=[1,2,3,7,8,9,7,6]
valor=5
f(lista,valor)

def calcular_nums(x,y,calculo):
  if calculo == 'suma':
    return x + y
  elif calculo == 'resta':
    return x-y
  elif calculo == 'multiplicacion':
    return x*y
  elif calculo == 'division':
    return x/y
  elif calculo == 'potenciacion':
    return x ** y
  elif calculo == 'radicacion':
    return x ** (1/y)
  else:
    print("Aclarar calculo correcto")

suma_final = calcular_nums(5,4,'resta')

# argumentos arbitrarios
# Si no se sabe de antemnao la cantidad de argumentos que se le ingresaran a la funcion,
# se agrega un "*" o "**" antes del nombre del parametros en la definicion de la funcion
# de esta manera la funcion va a recibir una tupla o diccionario de argumentos


# *args (Non Keyword Arguments) ->tupla
# **kwargs (Keyword Arguments) -> diccionario

def adder(x,y,z):
    print("sum:",x+y+z)
adder(10,12,13)

def adder(x,y,z):
    print("sum:",x+y+z)
adder(5,10,15,20,25)

def adder(*num):
    sum = 0
    for h in num:
        sum = sum + h
    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Nombre="Martin", Apellido="Conocchiari", Age=31, Phone=1234567890)
intro(Nombre="Lisandro", Apellido="lopez", Email="lichalopez@gmail.com", Pais="Argentina", Edad=37)


# Comprehensión de listas, permite crear listas con una regla rápidamente
[x ** 2 for x in range (9)]

'''Utilizacion de funciones lambda
Es una funcion anonima
Es pequeña y limitada a solo una linea
Puede tener multiples argumentos con UNA SOLA expresion
Posee 3 partes: la palabra clave "lambda", los parametros y el cuerpo de la funcion
La sintaxis es: lambda p1, p2,...,pn: expression
'''
def add(a,b):
    return a+b
print(add(4,5))

add = lambda x, y : x + y 
print(add(4,5))


#%%
import math

def conversion_tasas(tasa, frecuencia, continua_a_discreta=True):
    """
    Convierte una tasa anual de continua a discreta y vicersa.
    Parametros:
        tasa                : Tasa a convertir
        frecuencia          : Frecuencia de la capitalizacion por año
        continua_a_discreta : Convertir de continua a discreta o al reves.
    """
    if continua_a_discreta:
        return (math.exp(tasa) ** (1 / frecuencia) - 1) * frecuencia
    else:
        return math.log((1 + tasa / frecuencia) ** frecuencia)

conversion_tasas(0.1,12,True)    

def tabla_de_equivalencias(tea, incrementos_meses_enteros=True):
    """
    Imprime tabla de equivalencia de TEA en TNAs de diversas frecuencias.
    Parametros:
        tea         : Tasa Efectiva Anual
        incrementos : (default = True) Solo acepta incrementos que correspondan
                      con multiplos de meses enteros.
    """
    for i in range(1, 13):
        if incrementos_meses_enteros and 12 % i != 0:
            continue
        tna = ((1. + tea) ** (1. / i) - 1.) * i
        print('TNA', i, 'veces/año ->', tna)

tabla_de_equivalencias(0.1,True)


#%%
'''Ejercicios
Defina una función que dado un número decida si es par o impar
Defina una función que dada una edad decida si puede votar, manejar o ambas
Defina una función que dada una lista y un valor, decida si el valor se encuentra en el tercer puesto de la lista
Defina una función que dado una lsta de invitados y un nombre, decide si el individio puede entrar a la fiesta
'''
def parImpar (num):
    if num%2==0:
        return "par"
    else: 
        return "impar"

parImpar(5)

def votarManejar (edad):
    if edad < 16:
        return "no puede ni votar ni manejar"
    else:
        if edad >= 18:
            return "Puede votar y manejar"
        else:
            return "Solo puede votar"
votarManejar(25)  

def tercerPuesto(lista, valor):
    if len(lista) < 3:
        return "la lista no tiene tercer puesto"
    else:
        if lista[2] == valor:
            return "está en el tercer puesto"
        else:
            return "No está en el tercer puesto"
        
        
def seguridad(invitados, nombre):
    if nombre in invitados:
        return "puede pasar"
    else:
        return "no puede pasar"

#%%
'''Metodo Format'''
# Nos permite trabajar con str de forma avanzada
a = 0.1
b = 4
'x = {}'.format(a) 			    # 'x = 0.1'
'x = {}, y = {}'.format(a, b) 		    # 'x = 0.1, y = 4'
'x = {1}, y = {0}'.format(a, b)	    # 'x = 4, y = 0.1'
'x = {v1}, y = {v2}'.format(v1=a, v2=b)  # 'x = 0.1, y = 4’
'x = {:.2f}.'.format(a) 		    # 'x = 0.1’
'x ={:.2%}'.format(a) 		    # 'x = 10.00%’
'x ={:.2f}'.format(b*1000) 		    # 'x = 4,000.00’

#%%
'''APLICACION DE TODO LO VISTO: FUNCIONES, ESTRUCTURAS DE CONTROL, LISTAS Y METODOS EN EL
METODO DE BISECCION'''
def biseccionConHistoria(f,a,b,TOL,N0):

    #Creo una lista vacia llamada historia que la voy a ir llenando
    historia = []
    p_anterior = a

    i = 1
    while i <= N0:
        p = a+(b-a)/2
        historia.append((i,p,f(p))) #list.append(element)

        if (f(p) == 0) or ((b-a) /2 < TOL):
            return p, i,historia
            break
        i = i + 1 
        if f(a)*f(p) > 0: # No tengo nada a la izquierda.
            a = p
        else: # No tengo nada a la derecha.
            b = p
            p_anterior = p
        
    print("No convergió.")
    return

# Paramentros de la configuracion
def f(x):
    return 3*x**3 + 5*x**2 - 2*x + 1

tolerancia = 0.000001
a = -3
b = -2
nMax = 25


print("Creamos una tabla con la historia de cómo se fue convergiendo:")
raiz,nIteraciones,historia = biseccionConHistoria(f,a,b,tolerancia,nMax)

print("-----------------------------------------------------------------")
print("Iteración", "\t", "Raiz","\t", "f(p)")
print("-----------------------------------------------------------------")
for elemento in historia:
    print(elemento[0], "\t\t\t", elemento[1],"\t\t\t", elemento[2])
print("-----------------------------------------------------------------")
print("Tolerancia: ", tolerancia)
print("-----------------------------------------------------------------")
