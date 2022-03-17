#%%
###################################################################################
"""BISECCION"""
# Algoritmo de Bisección con la lógica del burden
#PASO 1: defino la funcion y los inputs
def f(x):
    return 3*x**3 + 5*x**2 - 2*x + 1
a=-2
b=-1
tol=0.01
n0=7
i=1
fa=f(a)
fb=f(b)
#PASO 2
while i<=n0:
    #PASO 3
    p=(a+b)/2
    fp=f(p)
    #PASO 4
    if fp==0 or (b-a)/2<tol:
        print("La solucion es ",p,"despues de ",i,"iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    if fa*fp>0:
        a=p
        fa=fp
    else:
        b=p
        fb=fp
#PASO 7
if i>=n0:
    print("El método fracasó después de",n0,"iteraciones")
    print("El método fracasó después de "+str(n0)+" iteraciones")

#%%
#ALGORITMO DE BISECCION QUE VA A DEVOLVER NO SOLO EL VALOR DE LA RAIZ, 
#SINO TAMBIEN CADA ITERACION HISTORICA Y VA A GENERAR UN GRAFICO
import numpy as np     #Funciona, uso este para Biseccion 
def f(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

def biseccion(f,a,b,TOL,N0):

    if f(a)*f(b) >= 0:
        print("No existe una raiz en el intervalo")
        return 
    p_anterior = a
    i = 1
    while i <= N0:
        p = a+(b-a)/2
        if (f(p) == 0) or ((b-a) /2 < TOL):
            return p, i 
            break
        i = i + 1  
        if f(a)*f(p) > 0: # No hay nada a la izquierda.
            a = p
        else: # No hay nada a la derecha.
            b = p
            p_anterior = p        
    print("No convergió.")
    return

# Paramentros de la configuracion
tolerancia = 0.01
a = -2
b = -1.11
nMax = 7

raiz,nIteraciones = biseccion(f,a,b,tolerancia,nMax)
print("La raiz encontrada es: ", raiz, " usando N = ", nIteraciones, "iteraciones")
print("-------------------------------")

''' -------------------------------------------------------------------------
código para ver como fue evolucionando el algoritmo
--------------------------------------------------------------------------'''
def biseccionConHistoria(f,a,b,TOL,N0):

    if f(a)*f(b) >= 0:
        print("No puede existir una raiz en el intervalo dado.")
        return

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

# CREO GRÁFICO
historia=np.array(historia)
import matplotlib.pyplot as plt
xi = historia[:,1]
yi = historia[:,2]

# ordena los puntos para el gráfico
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)#creo las lineas del gráfico
plt.plot(xi,yi,'r+',markersize=10) #le agrego puntos al gráfico

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisección en f(x)')
plt.grid(True)
plt.show()

#%%
#METODO DE BISECCION HECHO CON LA LIBRERIA SCIPY (ES EL MAS FACIL, ACCESO DIRECTO AL RESULTADO)
fy = lambda y: 3*y**3 + 5*y**2 - 2*y + 1
import scipy.optimize as opt
raiz=opt.bisect(fy,-3,-2,xtol=0.000001)
print(raiz)
#%%
###################################################################################
"""PUNTO FIJO"""
#METODO DE PUNTO FIJO CON LA LOGICA DEL BURDEN
#PASO 1: defino la funcion G y las variables
import math

def g(x):
    y= (x**2 - 6*x + 7)*math.exp(x) - x - 6
    return y
p0=-6
tol=0.0001
n0=7
i=1
#PASO 2
while i<=n0:
    #PASO 3
    p=g(p0)
    #PASO 4
    if abs(p-p0)<tol:
        print("El punto fijo es ",p," despues de ",i," iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    p0=p
#PASO 7
if i>n0:
    print("El método fracasó después de",n0,"iteraciones")
#%%
#ALGORITMO DE PUNTO FIJO QUE VA A DEVOLVER NO SOLO EL VALOR DEL PUNTO FIJO, 
#SINO TAMBIEN CADA ITERACION 
def fixedPoint(g,p0,TOL,N0):   #Funciona para Punto fijo
    i = 1
    while i <= N0:
        p = g(p0)

        if abs(p-p0) < TOL:
            return p, i
        i = i + 1
        p0 = p

    print("******** No convergió ********")
    return p0,-1

def g(x):
    return (x**2 - 6*x + 7)*math.exp(x) - 6

# Paramentros de la configuracion
p0 = -6
tolerance = 0.0001
maxNumberIterations = 7

root,iterations = fixedPoint(g,p0,tolerance,maxNumberIterations)
print("La raiz encontrada es: ", root, " usando N = ", iterations, "iteraciones")
print("-------------------------------")
print("Llamamos usando la expresión lambda")
root,iterations = fixedPoint(g,p0,tolerance,maxNumberIterations)
print("La raiz encontrada es: ", root, " usando N = ", iterations, "iteraciones")
print("-------------------------------")

''' -------------------------------------------------------------------------
Y si queremos ver cómo fue convergiendo el algoritmo?
-----------------------------------------------------------------------------'''
def fixedPointWithHistory(g,p0,TOL,N0):
    # Una lista vacia
    history = []

    # (iteracion,valor_estimado)
    history.append((0,p0))

    i = 1
    while i <= N0:
        p = g(p0)
        history.append((i,p))

        if abs(p-p0) < TOL:
            return p, i,history
        i = i + 1
        p0 = p

    print("******** No convergió ********")
    return p0,-1,history

print("Creamos una tabla con la historia de cómo se fue convergiendo:")

root,iterations,history = fixedPointWithHistory(g,p0,tolerance,maxNumberIterations)

print("-----------------------------------------------------------------")
print("Iteración", "\t", "Raiz", "\t\t", "Tolerancia usada: ", tolerance)
print("-----------------------------------------------------------------")
for element in history:
    print(element[0], "\t\t", element[1])
print("-----------------------------------------------------------------")
#%%
#METODO DE PUNTO FIJO HECHO CON LA LIBRERIA SCIPY
fz = lambda z: (1/2)*(10-z**3)**(1/2)
import scipy.optimize as opt
root=opt.fixed_point(fz,1.5,xtol=0.000001)
print(root)
#%%
###################################################################################
"""NEWTON RAPHSON"""
#METODO DE NEWTON RAPHSON CON LA LOGICA DEL BURDEN
#PASO 1: defino la funcion, su derivada y las variables
import math                 #Funciona para Newton 
math.cos(0)
def f(x):
    y=-x**3 - math.cos(x)
    return y
def fp(x):
    y=-3*x**2 + math.sin(x)
    return y
p0=-1
tol=0.1
n0=2
i=1
#PASO 2
while i<=n0:
    #PASO 3
    p=p0-f(p0)/fp(p0)
    #PASO 4
    if abs(p-p0)<tol:
        print("La solucion es ",p," despues de ",i," iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    p0=p
#PASO 7
if i>=n0:
    print("El metodo no converge ")

#%%
#OTRA FORMA
def func(x): 
    return x**5+2*x-1
def derivFunc( x ): 
    return 5*x**4+2 
  
#Creo metodo
def newtonRaphson(x): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
        x = x - h 
      
    print("El valor de la raiz es : ","%.15f"% x) 
  
x0 = 1 #Valor inicial 
newtonRaphson(x0) 
#%%
#HECHO CON LA LIBRERIA SCIPY
fy = lambda y: y**5+2*y-1
fz = lambda z: 5*z**4+2
import scipy.optimize as opt
raiz=opt.newton(fy,x0=1,fprime=fz,tol=0.000001)
print(raiz)
#%%
###################################################################################
"""SECANTE"""
# Algoritmo de la secante con la lógica del burden
#PASO 1: defino la funcion y los inputs
def f(x):     #Uso este para secante 
    y=230*x**4 - 18*x**3 + 9*x**2 - 221*x - 9
    return y
p0=-1
p1=0
tol=0.00001
n0=5
i=2
q0=f(p0)
q1=f(p1)
#PASO 2
while i<=n0:
    #PASO 3
    p=p1-(q1*(p1-p0)/(q1-q0))
    #PASO 4
    if abs(p-p1)<tol:
        print("La solucion es ",p,"despues de ",i,"iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    p0=p1
    q0=q1
    p1=p
    q1=f(p)
#PASO 7
if i>=n0:
    print("El método fracasó después de",n0,"iteraciones")
    print("El método fracasó después de "+str(n0)+" iteraciones")
#%%
#OTRA FORMA
def Secante(x0,x1,tol,N,f):
    i=1 
    while i<=N:
        x= x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))  

        if abs(x-x1)<tol:
            return x
        i=i + 1
        x0=x1    # redefinir x0
        x1=x     #redefinir x1
    print('El metodo fracaso despues de %d iteraciones' %N)   
   
f=lambda x: x**3 + 4*x**2 - 10
x0=-1
x1=0
tol=0.0001
N=4
    
x=Secante(x0,x1,tol,N,f)

print("La solucion es ",x,"despues de ",i,"iteraciones")
#%%
#HECHO CON LA LIBRERIA SCIPY
#si no se define la derivada en newton, python utiliza el metodo de la secante
fy = lambda y: y**3 + 4*y**2 - 10
import scipy.optimize as opt
root=opt.newton(fy,x0=1,tol=0.000001)
root

#%%
###################################################################################
"""FALSA POSICION"""
# Algoritmo de la falsa posicion con la lógica del burden
#PASO 1: defino la funcion y los inputs
def f(x):
    y=x**2 - 6              #Uso este metodo para posicion falsa
    return y
p0=3
p1=2
tol=0.1
n0=3
i=2
q0=f(p0)
q1=f(p1)
#PASO 2
while i<=n0:
    #PASO 3
    p=p1-(q1*(p1-p0))/(q1-q0)
    #PASO 4
    if abs(p-p1)<tol:
        print("La solucion es ",p,"despues de ",i,"iteraciones")
        break
    #PASO 5
    i=i+1
    q = f(p)
    #PASO 6
    if q * q1 <0:
        p0=p1
        q0=q1
    #PASO 7
    p1=p
    q1=q
#PASO 8
if i>=n0:
    print("El método fracasó después de",n0,"iteraciones")
    print("El método fracasó después de "+str(n0)+" iteraciones")
#%%
"""Calculo de TIR de un bono con los distintos métodos"""

#BISECCION
#PASO 1: defino la funcion y las variables
def f(x):
    y=44*(1+x)**-3+224*(1+x)**-2+35*(1+x)**-1-200
    return y
a=0
b=1
tol=0.0001
n0=25
i=1
fa=f(a) 
fb=f(b)
#PASO 2
while i<=n0:
    #PASO 3
    p=a+(b-a)/2
    fp=f(p)
    #PASO 4
    if fp==0 or (b-a)/2<tol:
        print("Bisección: La solucion es ",p,"despues de ",i,"iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    if fa*fp>0:
        a=p
        fa=fp
    else:
        b=p
        fb=fp
#PASO 7
if i>=n0:
    print("El metodo no converge ")

############################################################################

#%%
#SECANTE
def f(x):
    y=44*(1+x)**-3+224*(1+x)**-2+35*(1+x)**-1-200
    return y
p0=0
p1=1
tol=0.0001
n0=25
i=2
q0=f(p0)
q1=f(p1)
#PASO 2
while i<=n0:
    #PASO 3
    p=p1-(q1*(p1-p0)/(q1-q0))
    #PASO 4
    if abs(p-p1)<tol:
        print("Secante: La solucion es ",p,"despues de ",i,"iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    p0=p1
    q0=q1
    p1=p
    q1=f(p)
#PASO 7
if i>=n0:
    print("El método fracasó después de",n0,"iteraciones")
#%%
#NEWTON RAPHSON
def f(x):
    y=44*(1+x)**-3+224*(1+x)**-2+35*(1+x)**-1-200
    return y
def fp(x):
    y=-132*(1+x)**-4 -448*(1+x)**-3-35*(1+x)**-2
    return y
p0=0
tol=0.0001
n0=100
i=1
#PASO 2
while i<=n0:
    #PASO 3
    p=p0-f(p0)/fp(p0)
    #PASO 4
    if abs(p-p0)<tol:
        print("Newton Raphson: la solucion es ",p," despues de ",i," iteraciones")
        break
    #PASO 5
    i=i+1
    #PASO 6
    p0=p
#PASO 7
if i>=n0:
    print("El metodo no converge ")
    
############################################################################
#%%
#CON LIBRERIAS Y PARA 2 BONOS
import pandas as pd
import numpy as np

project1_cf = pd.DataFrame({"Year":np.arange(0,4), #con esto me muestra el flujo de fondos
"cf": [-200,35,224,44]})
project2_cf = pd.DataFrame({"Year":np.arange(0,4),
"cf": [-200,50,222.5,27.5]})
print(project1_cf)
print(project2_cf)  

irr1 = np.irr(project1_cf["cf"]) #esta libreria me trae la TIR
irr2 = np.irr(project2_cf["cf"])
irr_df = pd.DataFrame({"Name":["Project1", "Project2"],
                      "IRR":[irr1, irr2]})
print(irr_df)
