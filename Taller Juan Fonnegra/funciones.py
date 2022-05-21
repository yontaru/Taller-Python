from math import *

def sumar(a, b):
    resultado=a+b
    return resultado

def restar(a, b):
    resultado=a-b
    return resultado

def multiplicar(a, b):
    resultado=a*b
    return resultado

def dividir(a, b):
    resultado=a/b
    return round(resultado)

def seno(a):
    resultado=sin(a)
    return resultado

def coseno(a):
    resultado=cos(a)
    return resultado

def tangente(a):
    resultado=tan(a)
    return resultado

def numerospares(a):
    i = 0
    while i <= a:
        resultado=print(i)
        i = i + 2
    return resultado
