from random import *

valorcompra=int(input("ingrese el valor de la compra:"))
balotas=choice(["rojo","verde","otro"])
if balotas=="rojo":
    print(f"te toco el descuento del 15%")
    valorpagar=0.15
    print("el valor de la compra fue:{valorcompra}el color de la boleta fue:{balotas} el valor a pagar es: {valorpagar}")
elif balotas=="verde":
    print(f"te toco el descuento del 20%")
    oferta=valorcompra*0.20
    valorpagar=valorcompra-oferta
    print(f"el valor de la compra fue:{valorcompra}el color de la balota fue: {balotas} el valor a pagar es: {valorpagar}")
elif balotas=="otro":
    print(f"te toco el descuento del 65%")
    oferta=valorcompra*0.65
    valorpagar=valorcompra-oferta

    #resultado
    
    print(f"el valor de la compra fue:{valorcompra} el color de la balota fue: {balotas} el valor a pagar es: {valorpagar}")
