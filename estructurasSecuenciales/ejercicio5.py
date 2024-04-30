
costodelproducto=int(input("Digite el valor de la compra : "))
rebaja=int(input("Digite la rebaja : "))

descuentoCompra=rebaja / 100 

rebaja=rebaja * costodelproducto

valorFinal=costodelproducto-descuentoCompra

#resultado
print("La compra fue",costodelproducto,"rebaja",descuentoCompra ,"%","valor final es",valorFinal)