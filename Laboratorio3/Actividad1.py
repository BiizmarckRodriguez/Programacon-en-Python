#Carlos Boismarck Rodriguez Rodriguez
#Laboratorio de computo 3
#29/11/2016
#Actividad 1
import math as r
def cos(angulo):
    return r.cos(r.radians(angulo))
def sin(ang):
    return r.sin(r.radians(angulo))
def acos(angulo):
    return r.acos(r.radians(angulo))
x1=float(input ("Introduzca latitud: "))
y1=float(input ("Introduzca longitud: "))
x2=float(input ("Introduzca latitud2: "))
y2=float(input ("Introduzca longitud2: "))
def distancia(x1,y1,x2,y2):
    a=6371.01*r.acos(r.sin(x1)*r.sin(x2)*r.cos(x1)*r.cos(x2)*r.cos(y1-y2))
    print a

