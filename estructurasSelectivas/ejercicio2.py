CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas compradas: "))
ValorUnitario= int(input("ingrese el total a pagar por las zapatillas: "))
subTotal= CantidadDeZapatillas*ValorUnitario

if CantidadDeZapatillas>=3:
    totalaPagar= subTotal-(subTotal*0.20)  
    print(f"el total a pagar con su descuento del 20% es:{totalaPagar} " )
elif CantidadDeZapatillas<3:
   totalaPagar2 = subTotal-(subTotal*0.10)

   #resultado
   print(f"Total a pagar con el descuento del 10% es:{totalaPagar2} ")
