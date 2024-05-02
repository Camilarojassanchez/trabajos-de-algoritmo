#declarolas variables
monto= float (input("ingrese el total de la compra: ")) 
 
if monto>50000: 
  compraFinal= (monto*0.55) 
  prestamo_banco= (monto*0.30) 
  creditoFabricante = (monto*0.20) 
else:
   monto<=50000 

#declaramos la compraFinal
   compraFinal= monto+(monto*0.70*0.30)  
   creditoFabricante=(monto*0.30)+(monto*0.20) 
   prestamo_banco=0 

#resultado 
print("la empresainvirtio invirtio", compraFinal, "le solicito prestadoal banco", prestamo_banco,"el valor solicitado del credito del fabricante fue de: ", creditoFabricante)
 