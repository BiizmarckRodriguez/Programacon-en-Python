#Carlos Boismarck Rodriguez Rodriguez
#Laboratorio de computo 3
#29/11/2016
#Actividad 1
from math import sin,cos,sqrt,asin,acos,pi
def cos(angulo):
    return r.cos(r.radians(angulo))
def sin(angulo):
    return r.sin(r.radians(angulo))
def acos(angulo):
    return r.acos(r.radians(angulo))
    x1=input ("Latitud 1:")
    y1=input ("longitud 1:")
    x2=input ("Latitud 2:")
    y2=input ("longitud 2:")
def distancia(puntosgeograficos):
    distancia=6371*acos(sin(x1)sin(x2)+cos(x1)cos(x2)cos(y1-y2))
