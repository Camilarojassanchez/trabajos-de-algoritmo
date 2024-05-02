#declaro variables
cantidad_neta = int(input("Ingresa la cantidad de llantas que desea comprar: ")) 

#cantidad de neta y su total a pagar 
if cantidad_neta < 5:
    precio = 300
    total_a_pagar = cantidad_Comprada * precio
elif cantidad_neta<= 10:
    precio = 250
    total_a_pagar = cantidad_neta * precio
elif cantidad_neta > 10:
    precio = 200
    total_a_pagar = cantidad_neta * precio


#resultado total a pagar de llantas 
print(f"El costo por cada llanta es de {precio}")
print(f"El total a pagar por {cantidad_neta} llantas es de $ {total_a_pagar}")

